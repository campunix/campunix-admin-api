import pytest
from starlette import status

from tests.conftest import authorized_client

# Fixture to hold and share the created teacher's ID across test functions
@pytest.fixture(scope="module")
def teacher_id_holder():
    return {"id": 31}

# Test creating a teacher and saving its ID for later use
@pytest.mark.asyncio
async def test_create_teacher(authorized_client, teacher_id_holder):
    teacher_req = {
        "user_id": 25,
        "designation": "LECTURER",
        "status": "ACTIVE",
        "department_id": 1
    }

    # Send POST request to create a new teacher
    response = await authorized_client.post("/teachers", json=teacher_req)

    teacher_data = response.json()["data"]
    teacher_id_holder["id"] = teacher_data["id"]  # Store the created teacher's ID for later tests
    assert response.status_code == status.HTTP_200_OK

# Test fetching all teachers
@pytest.mark.asyncio
async def test_get_all_teachers(authorized_client):
    response = await authorized_client.get("/teachers")

    # Assert response is successful and contains a list of teachers
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"]["items"], list)

# Test fetching a teacher by its ID
@pytest.mark.asyncio
async def test_get_teacher_by_id(authorized_client, teacher_id_holder):
    teacher_id = teacher_id_holder["id"]
    response = await authorized_client.get(f"/teachers/{teacher_id}")

    # Assert response is successful and teacher ID matches
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["id"] == teacher_id

# Test updating a teacher's information (e.g., status)
@pytest.mark.asyncio
async def test_update_teacher(authorized_client, teacher_id_holder):
    teacher_id = teacher_id_holder["id"]
    updated_data = {
        "user_id": 25,
        "designation": "LECTURER",
        "status": "LEAVE",
        "department_id": 1
    }

    # Send PUT request to update the teacher
    response = await authorized_client.put(f"/teachers/{teacher_id}", json=updated_data)

    # Assert response is successful and status is updated
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["status"] == "LEAVE"

# Test deleting a teacher by its ID
@pytest.mark.asyncio
async def test_delete_teacher(authorized_client, teacher_id_holder):
    teacher_id = teacher_id_holder["id"]
    response = await authorized_client.delete(f"/teachers/{teacher_id}")

    # Assert successful deletion and correct message
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "Deleted successfully"

# Test fetching all possible teacher statuses
@pytest.mark.asyncio
async def test_get_teacher_status(authorized_client):
    response = await authorized_client.get("/teachers/teacherStatus")

    # Assert response is successful and contains a list of statuses
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"]["items"], list)

# Test fetching all possible teacher designations
@pytest.mark.asyncio
async def test_get_teacher_designations(authorized_client):
    response = await authorized_client.get("/teachers/teacherDesignations")

    # Assert response is successful and contains a list of designations
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"]["items"], list)