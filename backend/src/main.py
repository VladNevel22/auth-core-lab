from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_session
from src.models import User, UserCreate, UserPublic
from src.security import hash_pass, validate_complexity

app = FastAPI(title="Neo Auth API")

@app.get("/health")
async def health():
    return {"status": "alive", "style": "neo-brutalism"}

@app.post("/api/register", response_model=UserPublic, status_code=201)
async def register(user_in: UserCreate, session: AsyncSession = Depends(get_session)):
    # 1. Валидация логина (regex)
    import re
    if not re.match(r"^[a-zA-Z0-9_.-]+$", user_in.login):
        raise HTTPException(422, detail="Login format invalid")

    # 2. Валидация пароля
    if not validate_complexity(user_in.password):
        raise HTTPException(422, detail="Password too weak (min 8 symbols: needs A-Z, a-z, 0-9, special)")

    # 3. Проверка дубликата
    statement = select(User).where(User.login == user_in.login)
    result = await session.execute(statement)
    if result.scalar_one_or_none():
        raise HTTPException(409, detail="Login taken")

    # 4. Создание
    new_user = User(
        login=user_in.login,
        password_hash=hash_pass(user_in.password)
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    
    return new_user
