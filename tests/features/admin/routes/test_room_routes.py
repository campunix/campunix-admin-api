import pytest
from starlette import status

from tests.conftest import authorized_client

# Fixture to hold and share the created room's ID across test functions
@pytest.fixture(scope="module")
def room_id_holder():
    return {"id": 9}

# Test creating a room and saving its ID for use in later tests
@pytest.mark.asyncio
async def test_create_room(authorized_client, room_id_holder):
    room_req = {
        "name": "Room T-101",
        "code": "T-101",
        "department_id": 1,
        "room_type": "LECTURE"
    }

    # Send POST request to create a new room
    response = await authorized_client.post("/rooms", json=room_req)

    # Assert successful creation and correct code in response
    assert response.status_code == status.HTTP_200_OK
    room_id_holder["id"] = response.json()["data"]["id"]  # Save ID for later tests
    assert response.json()["data"]["code"] == "T-101"

# Test fetching all rooms
@pytest.mark.asyncio
async def test_get_all_rooms(authorized_client):
    response = await authorized_client.get("/rooms")

    # Assert response is successful and data is a list
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"]["items"], list)

# Test fetching a single room by its ID
@pytest.mark.asyncio
async def test_get_room_by_id(authorized_client, room_id_holder):
    room_id = room_id_holder["id"]
    response = await authorized_client.get(f"/rooms/{room_id}")

    # Assert response is successful and room ID matches
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["id"] == room_id

# Test updating an existing room
@pytest.mark.asyncio
async def test_update_room(authorized_client, room_id_holder):
    room_id = room_id_holder["id"]
    response = await authorized_client.put(f"/rooms/{room_id}", json={
        "name": "Room T-101",
        "code": "T-101",
        "department_id": 1,
        "room_type": "LAB"
    })

    # Assert response is successful and room_type is updated
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["room_type"] == "LAB"

# Test fetching all room types
@pytest.mark.asyncio
async def test_get_room_types(authorized_client):
    response = await authorized_client.get("/rooms/roomTypes")

    # Assert response is successful and there is at least one room type
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()["data"]["items"]) > 0

# Test deleting a room by its ID
@pytest.mark.asyncio
async def test_delete_room(authorized_client, room_id_holder):
    room_id = room_id_holder["id"]
    response = await authorized_client.delete(f"/rooms/{room_id}")

    # Assert successful deletion and correct message in response
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "Deleted successfully"