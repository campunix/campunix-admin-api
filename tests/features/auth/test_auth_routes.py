import pytest
from fastapi import status


@pytest.mark.asyncio
async def test_register(client, test_user_data):
    response = await client.post("/register", json=test_user_data)

    assert response.status_code == status.HTTP_201_CREATED
    assert "id" in response.json()
    assert response.json()["username"] == test_user_data["username"]


@pytest.mark.asyncio
async def test_login(client, test_user_data):
    login_data = {
        "username": test_user_data["username"],
        "password": test_user_data["password"]
    }
    response = await client.post("/token", data=login_data)

    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "Bearer"


@pytest.mark.asyncio
async def test_get_current_user(authorized_client, test_user_data):
    response = await authorized_client.get("/me")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == test_user_data["username"]


@pytest.mark.asyncio
async def test_get_all_users(authorized_client):
    response = await authorized_client.get("/users")

    assert response.status_code == status.HTTP_200_OK
    assert "items" in response.json()["data"]
    assert isinstance(response.json()["data"]["items"], list)
