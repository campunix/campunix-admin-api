import pytest
from starlette import status

from tests.conftest import authorized_client

# Fixture to hold and share the created department's ID across test functions
@pytest.fixture(scope="module")
def department_id_holder():
    return {"id": 13}

# Test creating a department via the API
@pytest.mark.asyncio
async def test_create_department(authorized_client, department_id_holder):
    department_req = {
        "name": "Mechanical Engineering",
        "code": "ME",
        "organization_id": 1,
        "created_by": 24
    }

    # Send a POST request to create a new department
    response = await authorized_client.post("/departments", json=department_req)

    # Assert status and response correctness
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()["data"]
    department_id_holder["id"] = response_data["id"]  # Save ID for later tests
    assert response_data["code"] == "ME"

# Test fetching all departments
@pytest.mark.asyncio
async def test_get_all_departments(authorized_client):
    response = await authorized_client.get("/departments")

    # Assert response is successful and data is a list
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"]["items"], list)

# Test fetching a department by its ID
@pytest.mark.asyncio
async def test_get_department_by_id(authorized_client, department_id_holder):
    department_id = department_id_holder["id"]
    response = await authorized_client.get(f"/departments/{department_id}")

    # Assert response is successful and department ID matches
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["id"] == department_id

# Test updating an existing department
@pytest.mark.asyncio
async def test_update_department(authorized_client, department_id_holder):
    department_id = department_id_holder["id"]
    updated_data = {
        "name": "Mechanical Engineering Test",
        "code": "ME",
        "organization_id": 1
    }

    # Send a PUT request to update the department
    response = await authorized_client.put(f"/departments/{department_id}", json=updated_data)

    # Assert response is successful and the name is updated
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["name"] == "Mechanical Engineering Test"

# Test deleting a department by its ID
@pytest.mark.asyncio
async def test_delete_department(authorized_client, department_id_holder):
    department_id = department_id_holder["id"]
    response = await authorized_client.delete(f"/departments/{department_id}")

    # Assert response is successful and message indicates deletion
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "Deleted successfully"