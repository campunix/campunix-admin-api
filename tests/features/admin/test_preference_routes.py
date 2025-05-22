import pytest
from fastapi import status

from tests.conftest import authorized_client


@pytest.fixture(scope="module")
def pref_id_holder():
    return {"id": 31}


@pytest.mark.asyncio
async def test_create_preference(preference_service_mock, authorized_client, pref_id_holder):
    pref_request = {
        "teacher_id": 1,
        "day": "SUNDAY",
        "slot_no": 1
    }

    pref_response = {
        "teacher_id": 1,
        "teacher_name": "Dr. Jugal Krishna Das, B.Sc(Donetsk), MSc.(Donetsk), PhD(Kiev)", "day": "SUNDAY",
        "slot_no": 1
    }

    preference_service_mock.create_preference.return_value = pref_response

    response = await authorized_client.post("/preferences", json=pref_request)

    assert response.status_code == status.HTTP_200_OK
    pref_id_holder["id"] = response.json()["data"]["id"]
    assert response.json()["data"]["teacher_id"] == 1


@pytest.mark.asyncio
async def test_get_all_preferences(preference_service_mock, authorized_client):
    preference_service_mock.get_preferences.return_value = []

    response = await authorized_client.get("/preferences")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()["data"]) > 0


@pytest.mark.asyncio
async def test_get_preferences_by_teacher_id(preference_service_mock, authorized_client):
    preference_service_mock.get_preferences_by_teacher_id.return_value = []

    response = await authorized_client.get("/preferences/byTeacher", params={"teacher_id": 299})

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["items"] == []


@pytest.mark.asyncio
async def test_get_preference_by_id(preference_service_mock, authorized_client, pref_id_holder):
    preference_service_mock.get_preference_by_id.return_value = {
        "teacher_id": 1,
        "teacher_name": "Dr. Jugal Krishna Das",
        "day": "SUNDAY",
        "slot_no": 1
    }

    pref_id = pref_id_holder["id"]

    response = await authorized_client.get(f"/preferences/{pref_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["id"] == pref_id


@pytest.mark.asyncio
async def test_get_preference_by_id_not_found(preference_service_mock, authorized_client):
    preference_service_mock.get_preference_by_id.return_value = None

    response = await authorized_client.get("/preferences/999")

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.asyncio
async def test_update_preference(preference_service_mock, authorized_client, pref_id_holder):
    update_data = {
        "teacher_id": 1,
        "day": "MONDAY",
        "slot_no": 2
    }

    pref_id = pref_id_holder["id"]

    updated_response = {
        "id": pref_id,
        "teacher_id": 1,
        "teacher_name": "Dr. Jugal Krishna Das",
        "day": "MONDAY",
        "slot_no": 2
    }

    preference_service_mock.update_preference.return_value = updated_response

    response = await authorized_client.put(f"/preferences/{pref_id}", json=update_data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["day"] == '2'


@pytest.mark.asyncio
async def test_update_preference_not_found(preference_service_mock, authorized_client):
    preference_service_mock.update_preference.return_value = None

    response = await authorized_client.put("/preferences/999", json={
        "teacher_id": 1,
        "day": "MONDAY",
        "slot_no": 2
    })

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.asyncio
async def test_delete_preference(preference_service_mock, authorized_client, pref_id_holder):
    preference_service_mock.delete_preference.return_value = True
    pref_id = pref_id_holder["id"]
    response = await authorized_client.delete(f"/preferences/{pref_id}")

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_delete_preference_not_found(preference_service_mock, authorized_client):
    preference_service_mock.delete_preference.return_value = False

    response = await authorized_client.delete("/preferences/999")

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.asyncio
async def test_get_days(preference_service_mock, authorized_client):
    preference_service_mock.get_days.return_value = ["SUNDAY", "MONDAY", "TUESDAY"]

    response = await authorized_client.get("/preferences/days")

    assert response.status_code == status.HTTP_200_OK
    assert "SUNDAY" in response.json()["data"]["items"]
