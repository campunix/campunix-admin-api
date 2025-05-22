import pytest
from starlette import status

from tests.conftest import authorized_client


@pytest.fixture(scope="module")
def teacher_id_holder():
    return {"id": 31}


@pytest.mark.asyncio
async def test_create_teacher(authorized_client, teacher_id_holder):
    teacher_req = {
        "user_id": 25,
        "designation": "LECTURER",
        "status": "ACTIVE",
        "department_id": 1
    }

    response = await authorized_client.post("/teachers", json=teacher_req)

    teacher_data = response.json()["data"]
    teacher_id_holder["id"] = teacher_data["id"]
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_get_all_teachers(authorized_client):
    response = await authorized_client.get("/teachers")

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"]["items"], list)


@pytest.mark.asyncio
async def test_get_teacher_by_id(authorized_client, teacher_id_holder):
    teacher_id = teacher_id_holder["id"]
    response = await authorized_client.get(f"/teachers/{teacher_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["id"] == teacher_id


@pytest.mark.asyncio
async def test_update_teacher(authorized_client, teacher_id_holder):
    teacher_id = teacher_id_holder["id"]
    updated_data = {
        "user_id": 25,
        "designation": "LECTURER",
        "status": "LEAVE",
        "department_id": 1
    }

    response = await authorized_client.put(f"/teachers/{teacher_id}", json=updated_data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["status"] == "LEAVE"


@pytest.mark.asyncio
async def test_delete_teacher(authorized_client, teacher_id_holder):
    teacher_id = teacher_id_holder["id"]
    response = await authorized_client.delete(f"/teachers/{teacher_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "Deleted successfully"


@pytest.mark.asyncio
async def test_get_teacher_status(authorized_client):
    response = await authorized_client.get("/teachers/teacherStatus")

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"]["items"], list)


@pytest.mark.asyncio
async def test_get_teacher_designations(authorized_client):
    response = await authorized_client.get("/teachers/teacherDesignations")

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"]["items"], list)
