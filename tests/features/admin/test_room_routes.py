import pytest
from starlette import status

from tests.conftest import authorized_client


@pytest.fixture(scope="module")
def room_id_holder():
    return {"id": 14}


@pytest.mark.asyncio
async def test_create_room(authorized_client, room_id_holder):
    room_req = {
        "name": "Room T-101",
        "code": "T-101",
        "department_id": 1,
        "room_type": "LECTURE"
    }

    response = await authorized_client.post("/rooms", json=room_req)

    assert response.status_code == status.HTTP_200_OK
    room_id_holder["id"] = response.json()["data"]["id"]
    assert response.json()["data"]["code"] == "T-101"


@pytest.mark.asyncio
async def test_get_all_rooms(authorized_client):
    response = await authorized_client.get("/rooms")

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"]["items"], list)


@pytest.mark.asyncio
async def test_get_room_by_id(authorized_client, room_id_holder):
    room_id = room_id_holder["id"]
    response = await authorized_client.get(f"/rooms/{room_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["id"] == room_id


@pytest.mark.asyncio
async def test_update_room(authorized_client, room_id_holder):
    room_id = room_id_holder["id"]
    response = await authorized_client.put(f"/rooms/{room_id}", json={
        "name": "Room T-101",
        "code": "T-101",
        "department_id": 1,
        "room_type": "LAB"
    })

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["room_type"] == "LAB"


@pytest.mark.asyncio
async def test_get_room_types(authorized_client):
    response = await authorized_client.get("/rooms/roomTypes")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()["data"]["items"]) > 0

@pytest.mark.asyncio
async def test_delete_room(authorized_client, room_id_holder):
    room_id = room_id_holder["id"]
    response = await authorized_client.delete(f"/rooms/{room_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "Deleted successfully"
