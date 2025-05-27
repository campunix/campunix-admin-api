import pytest
from fastapi import status

from tests.conftest import authorized_client

# Fixture to hold and share the created preference's ID across test functions
@pytest.fixture(scope="module")
def pref_id_holder():
    return {"id": 31}

# Test creating a preference and saving its ID for use in later tests
@pytest.mark.asyncio
async def test_create_preference(authorized_client, pref_id_holder):
    pref_request = {
        "teacher_id": 1,
        "day": "SUNDAY",
        "slot_no": 1
    }

    # Send POST request to create a new preference
    response = await authorized_client.post("/preferences", json=pref_request)

    # Assert successful creation and correct teacher_id in response
    assert response.status_code == status.HTTP_200_OK
    pref_id_holder["id"] = response.json()["data"]["id"]  # Store ID for future tests
    assert response.json()["data"]["teacher_id"] == 1

# Test fetching all preferences
@pytest.mark.asyncio
async def test_get_all_preferences(authorized_client):
    response = await authorized_client.get("/preferences")

    # Assert response is successful and at least one preference exists
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()["data"]) > 0

# Test fetching preferences for a teacher with no preferences
@pytest.mark.asyncio
async def test_get_preferences_by_teacher_id(authorized_client):
    response = await authorized_client.get("/preferences/byTeacher", params={"teacher_id": 299})

    # Assert response is successful and items list is empty
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["items"] == []

# Test fetching a preference by its ID
@pytest.mark.asyncio
async def test_get_preference_by_id(authorized_client, pref_id_holder):
    pref_id = pref_id_holder["id"]

    response = await authorized_client.get(f"/preferences/{pref_id}")

    # Assert the correct preference is returned
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["id"] == pref_id

# Test fetching a preference by a non-existent ID
@pytest.mark.asyncio
async def test_get_preference_by_id_not_found(authorized_client):
    response = await authorized_client.get("/preferences/999")

    # Assert 404 not found is returned
    assert response.status_code == status.HTTP_404_NOT_FOUND

# Test updating a preference by ID
@pytest.mark.asyncio
async def test_update_preference(authorized_client, pref_id_holder):
    update_data = {
        "teacher_id": 1,
        "day": "MONDAY",
        "slot_no": 2
    }

    pref_id = pref_id_holder["id"]

    # Send PUT request to update the preference
    response = await authorized_client.put(f"/preferences/{pref_id}", json=update_data)

    # Assert successful update and correct day value in response
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["day"] == '2'

# Test updating a non-existent preference
@pytest.mark.asyncio
async def test_update_preference_not_found(authorized_client):
    response = await authorized_client.put("/preferences/999", json={
        "teacher_id": 1,
        "day": "MONDAY",
        "slot_no": 2
    })

    # Assert 404 not found is returned
    assert response.status_code == status.HTTP_404_NOT_FOUND

# Test deleting a preference by ID
@pytest.mark.asyncio
async def test_delete_preference(authorized_client, pref_id_holder):
    pref_id = pref_id_holder["id"]
    response = await authorized_client.delete(f"/preferences/{pref_id}")

    # Assert successful deletion
    assert response.status_code == status.HTTP_200_OK

# Test deleting a non-existent preference
@pytest.mark.asyncio
async def test_delete_preference_not_found(authorized_client):
    response = await authorized_client.delete("/preferences/999")

    # Assert 404 not found is returned
    assert response.status_code == status.HTTP_404_NOT_FOUND

# Test fetching the list of days available for preferences
@pytest.mark.asyncio
async def test_get_days(authorized_client):
    response = await authorized_client.get("/preferences/days")

    # Assert the response contains the expected day "SUNDAY"
    assert response.status_code == status.HTTP_200_OK
    assert "SUNDAY" in response.json()["data"]["items"]