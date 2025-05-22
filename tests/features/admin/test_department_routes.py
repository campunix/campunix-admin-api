import pytest
from starlette import status

from tests.conftest import authorized_client


@pytest.fixture(scope="module")
def department_id_holder():
    return {"id": 13}


@pytest.mark.asyncio
async def test_create_department(authorized_client, department_id_holder):
    department_req = {
        "name": "Mechanical Engineering",
        "code": "ME",
        "organization_id": 1,
        "created_by": 24
    }

    response = await authorized_client.post("/departments", json=department_req)

    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()["data"]
    department_id_holder["id"] = response_data["id"]
    assert response_data["code"] == "ME"


@pytest.mark.asyncio
async def test_get_all_departments(authorized_client):
    response = await authorized_client.get("/departments")

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"]["items"], list)


@pytest.mark.asyncio
async def test_get_department_by_id(authorized_client, department_id_holder):
    department_id = department_id_holder["id"]
    response = await authorized_client.get(f"/departments/{department_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["id"] == department_id


@pytest.mark.asyncio
async def test_update_department(authorized_client, department_id_holder):
    department_id = department_id_holder["id"]
    updated_data = {
        "name": "Mechanical Engineering Test",
        "code": "ME",
        "organization_id": 1
    }

    response = await authorized_client.put(f"/departments/{department_id}", json=updated_data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["name"] == "Mechanical Engineering Test"


@pytest.mark.asyncio
async def test_delete_department(authorized_client, department_id_holder):
    department_id = department_id_holder["id"]
    response = await authorized_client.delete(f"/departments/{department_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "Deleted successfully"
