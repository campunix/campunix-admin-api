import os
import sys
import pytest
from httpx import AsyncClient
from src.main import app

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

@pytest.fixture(scope="module")
def event_loop():
    import asyncio
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="module")
async def test_user_data():
    return {
        "username": "testuser",
        "email": "testuser@example.com",
        "full_name": "Test User",
        "password": "1234",
        "confirm_password": "1234"
    }

@pytest.fixture(scope="module")
async def bearer_token(client: AsyncClient, test_user_data):
    await client.post("/register", json=test_user_data)
    login_data = {
        "username": test_user_data["username"],
        "password": test_user_data["password"]
    }
    response = await client.post("/token", data=login_data)
    assert response.status_code == 200
    token = response.json()["access_token"]
    return f"Bearer {token}"

@pytest.fixture(scope="module")
async def client(event_loop):
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.fixture(scope="module")
async def authorized_client(event_loop, bearer_token):
    async with AsyncClient(app=app, base_url="http://test") as client:
        client.headers.update({"Authorization": bearer_token})
        yield client


def pytest_collection_modifyitems(session, config, items):
    first_file = "test_auth_routes.py"
    first_items = [item for item in items if first_file in str(item.fspath)]
    other_items = [item for item in items if first_file not in str(item.fspath)]
    items[:] = first_items + other_items
