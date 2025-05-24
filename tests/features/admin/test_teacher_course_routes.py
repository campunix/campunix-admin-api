import pytest
from starlette import status

from tests.conftest import authorized_client

'''

@pytest.fixture(scope="module")
def teacher_course_holder():
    return {"id": None}


@pytest.mark.asyncio
async def test_create_teacher_course(authorized_client, teacher_course_holder):
    payload = {
        "teacher_id": 1,
        "course_id": 72
    }

    response = await authorized_client.post("/teacherCourse", json=payload)

    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()["data"]
    teacher_course_holder["id"] = response_data["id"]
    assert response_data["teacher"]["id"] == 1
    assert response_data["course"]["id"] == 72


@pytest.mark.asyncio
async def test_get_all_course_teacher(authorized_client):
    response = await authorized_client.get("/teacherCourse")

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"], list)


@pytest.mark.asyncio
async def test_get_teacher_course_by_id(authorized_client, teacher_course_holder):
    tc_id = teacher_course_holder["id"]
    response = await authorized_client.get(f"/teacherCourse/{tc_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["id"] == tc_id


@pytest.mark.asyncio
async def test_update_teacher_course(authorized_client, teacher_course_holder):
    tc_id = teacher_course_holder["id"]
    update_data = {
        "teacher_id": 2,
        "course_id": 1,
        "semester_id": 1
    }

    response = await authorized_client.put(f"/teacherCourse/{tc_id}", json=update_data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["teacher_id"] == 2


@pytest.mark.asyncio
async def test_assign_teachers(authorized_client):
    payload = [1, 2]
    course_id = 1

    response = await authorized_client.post(f"/teacherCourse/{course_id}/assignTeachers", json=payload)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"], dict) or isinstance(response.json()["data"], list)


@pytest.mark.asyncio
async def test_assign_courses(authorized_client):
    payload = [1, 2]
    teacher_id = 1

    response = await authorized_client.post(f"/teacherCourse/{teacher_id}/assignCourses", json=payload)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"], dict) or isinstance(response.json()["data"], list)


@pytest.mark.asyncio
async def test_delete_teacher_course(authorized_client, teacher_course_holder):
    tc_id = teacher_course_holder["id"]
    response = await authorized_client.delete(f"/teacherCourse/{tc_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "Deleted successfully"


'''