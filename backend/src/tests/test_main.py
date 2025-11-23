import pytest
import uuid
from httpx import AsyncClient

def random_suffix():
    return str(uuid.uuid4())[:8]

@pytest.mark.asyncio
async def test_health(ac: AsyncClient):
    resp = await ac.get("/health")
    assert resp.status_code == 200
    assert resp.json()["style"] == "neo-brutalism"

@pytest.mark.asyncio
async def test_register_success(ac: AsyncClient):
    login = f"user_{random_suffix()}"
    payload = {"login": login, "password": "Strong!Pass1"}
    
    resp = await ac.post("/api/register", json=payload)
    
    assert resp.status_code == 201
    assert resp.json()["message"] == "User created successfully"

@pytest.mark.asyncio
async def test_weak_password(ac: AsyncClient):
    payload = {"login": f"weak_{random_suffix()}", "password": "weak"}
    resp = await ac.post("/api/register", json=payload)
    assert resp.status_code == 422

@pytest.mark.asyncio
async def test_duplicate_login(ac: AsyncClient):
    login = f"dupe_{random_suffix()}"
    payload = {"login": login, "password": "Strong!Pass1"}
    
    # 1. Успех
    resp1 = await ac.post("/api/register", json=payload)
    assert resp1.status_code == 201
    
    resp2 = await ac.post("/api/register", json=payload) 
    assert resp2.status_code == 409
