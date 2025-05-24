import pytest
from fastapi import status

from tests.conftest import authorized_client


@pytest.fixture(scope="module")
def pref_id_holder():
    return {"id": 31}


@pytest.mark.asyncio
async def test_create_preference(authorized_client, pref_id_holder):
    pref_request = {
        "teacher_id": 1,
        "day": "SUNDAY",
        "slot_no": 1
    }

    response = await authorized_client.post("/preferences", json=pref_request)

    assert response.status_code == status.HTTP_200_OK
    pref_id_holder["id"] = response.json()["data"]["id"]
    assert response.json()["data"]["teacher_id"] == 1


@pytest.mark.asyncio
async def test_get_all_preferences(authorized_client):
    response = await authorized_client.get("/preferences")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()["data"]) > 0


@pytest.mark.asyncio
async def test_get_preferences_by_teacher_id(authorized_client):
    response = await authorized_client.get("/preferences/byTeacher", params={"teacher_id": 299})

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["items"] == []


@pytest.mark.asyncio
async def test_get_preference_by_id(authorized_client, pref_id_holder):
    pref_id = pref_id_holder["id"]

    response = await authorized_client.get(f"/preferences/{pref_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["id"] == pref_id


@pytest.mark.asyncio
async def test_get_preference_by_id_not_found(authorized_client):
    response = await authorized_client.get("/preferences/999")

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.asyncio
async def test_update_preference(authorized_client, pref_id_holder):
    update_data = {
        "teacher_id": 1,
        "day": "MONDAY",
        "slot_no": 2
    }

    pref_id = pref_id_holder["id"]

    response = await authorized_client.put(f"/preferences/{pref_id}", json=update_data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["day"] == '2'


@pytest.mark.asyncio
async def test_update_preference_not_found(authorized_client):
    response = await authorized_client.put("/preferences/999", json={
        "teacher_id": 1,
        "day": "MONDAY",
        "slot_no": 2
    })

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.asyncio
async def test_delete_preference(authorized_client, pref_id_holder):
    pref_id = pref_id_holder["id"]
    response = await authorized_client.delete(f"/preferences/{pref_id}")

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_delete_preference_not_found(authorized_client):
    response = await authorized_client.delete("/preferences/999")

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.asyncio
async def test_get_days(authorized_client):
    response = await authorized_client.get("/preferences/days")

    assert response.status_code == status.HTTP_200_OK
    assert "SUNDAY" in response.json()["data"]["items"]
