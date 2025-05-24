import pytest
from starlette import status

from tests.conftest import authorized_client


@pytest.fixture(scope="module")
def course_id_holder():
    return {"id": 108}


@pytest.mark.asyncio
async def test_create_course(authorized_client, course_id_holder):
    course_req = {
        "title": "Test Course",
        "code": "T201",
        "department_id": 1,
        "course_type": "THEORY"
    }

    response = await authorized_client.post("/courses", json=course_req)

    assert response.status_code == status.HTTP_200_OK
    course_data = response.json()["data"]
    course_id_holder["id"] = course_data["id"]
    assert course_data["code"] == "T201"


@pytest.mark.asyncio
async def test_get_all_courses(authorized_client):
    response = await authorized_client.get("/courses")

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"]["items"], list)


@pytest.mark.asyncio
async def test_get_course_by_id(authorized_client, course_id_holder):
    course_id = course_id_holder["id"]
    response = await authorized_client.get(f"/courses/{course_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["id"] == course_id


@pytest.mark.asyncio
async def test_get_courses_by_teacher(authorized_client):
    response = await authorized_client.get("/courses/byTeacher?teacher_id=1")

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"]["items"], list)


@pytest.mark.asyncio
async def test_update_course(authorized_client, course_id_holder):
    course_id = course_id_holder["id"]
    update_data = {
        "title": "Test Course Updated",
        "code": "T201",
        "department_id": 1,
        "course_type": "THEORY"
    }

    response = await authorized_client.put(f"/courses/{course_id}", json=update_data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["title"] == "Test Course Updated"


'''

@pytest.mark.asyncio
async def test_bulk_create_courses(authorized_client):
    bulk_courses = [
        {
            "title": "Test Course Two",
            "code": "T202",
            "department_id": 1,
            "course_type": "THEORY"
        },
        {
            "title": "Test Course Three",
            "code": "T203",
            "department_id": 1,
            "course_type": "THEORY"
        }
    ]

    response = await authorized_client.post("/courses/bulk", json=bulk_courses)

    assert response.status_code == status.HTTP_200_OK

'''


@pytest.mark.asyncio
async def test_delete_course(authorized_client, course_id_holder):
    course_id = course_id_holder["id"]
    response = await authorized_client.delete(f"/courses/{course_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "Deleted successfully"


@pytest.mark.asyncio
async def test_get_course_types(authorized_client):
    response = await authorized_client.get("/courses/courseTypes")

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"]["items"], list)
