import uuid
from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional

class UserBase(SQLModel):
    login: str = Field(index=True, unique=True, min_length=3, max_length=32)

class User(UserBase, table=True):
    __tablename__ = "users_table"

    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class UserCreate(UserBase):
    password: str
    
class UserPublic(UserBase):
    id: uuid.UUID
    message: str = "User created successfully"
