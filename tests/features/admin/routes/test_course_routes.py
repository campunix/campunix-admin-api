import pytest
from starlette import status

from tests.conftest import authorized_client

# Fixture to hold and share the created course's ID across test functions
@pytest.fixture(scope="module")
def course_id_holder():
    return {"id": 108}

# Test creating a course
@pytest.mark.asyncio
async def test_create_course(authorized_client, course_id_holder):
    course_req = {
        "title": "Test Course",
        "code": "T201",
        "department_id": 1,
        "course_type": "THEORY"
    }

    # Send POST request to create a new course
    response = await authorized_client.post("/courses", json=course_req)

    # Assert the response is successful and contains the expected data
    assert response.status_code == status.HTTP_200_OK
    course_data = response.json()["data"]
    course_id_holder["id"] = course_data["id"]  # Store the created course ID for later tests
    assert course_data["code"] == "T201"

# Test fetching all courses
@pytest.mark.asyncio
async def test_get_all_courses(authorized_client):
    response = await authorized_client.get("/courses")

    # Assert the response is successful and contains a list of courses
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"]["items"], list)

# Test fetching a single course by its ID
@pytest.mark.asyncio
async def test_get_course_by_id(authorized_client, course_id_holder):
    course_id = course_id_holder["id"]
    response = await authorized_client.get(f"/courses/{course_id}")

    # Assert the response is successful and the course ID matches
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["id"] == course_id

# Test fetching all courses taught by a specific teacher
@pytest.mark.asyncio
async def test_get_courses_by_teacher(authorized_client):
    response = await authorized_client.get("/courses/byTeacher?teacher_id=1")

    # Assert the response is successful and contains a list of courses
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"]["items"], list)

# Test updating an existing course
@pytest.mark.asyncio
async def test_update_course(authorized_client, course_id_holder):
    course_id = course_id_holder["id"]
    update_data = {
        "title": "Test Course Updated",
        "code": "T201",
        "department_id": 1,
        "course_type": "THEORY"
    }

    # Send PUT request to update the course
    response = await authorized_client.put(f"/courses/{course_id}", json=update_data)

    # Assert the response is successful and the title is updated
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["title"] == "Test Course Updated"

'''
# (Optional) Test bulk creating courses - commented out
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

# Test deleting a course by its ID
@pytest.mark.asyncio
async def test_delete_course(authorized_client, course_id_holder):
    course_id = course_id_holder["id"]
    response = await authorized_client.delete(f"/courses/{course_id}")

    # Assert the response is successful and the deletion message is correct
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "Deleted successfully"

# Test fetching all course types
@pytest.mark.asyncio
async def test_get_course_types(authorized_client):
    response = await authorized_client.get("/courses/courseTypes")

    # Assert the response is successful and contains a list of course types
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json()["data"]["items"], list)