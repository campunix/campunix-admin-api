import pytest
from fastapi import status


@pytest.fixture(scope="module")
def org_id_holder():
    return {"id": 25}


@pytest.mark.asyncio
async def test_create_organization(org_id_holder, authorized_client):
    test_org = {"name": "Dhaka University"}

    response = await authorized_client.post("/organizations", json=test_org)

    assert response.status_code == status.HTTP_200_OK
    org_id_holder["id"] = response.json()["data"]["id"]
    assert response.json()["data"]["name"] == "Dhaka University"


@pytest.mark.asyncio
async def test_get_all_organization(authorized_client):

    response = await authorized_client.get("/organizations")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()["data"]) > 0


@pytest.mark.asyncio
async def test_get_organization_found(org_id_holder, authorized_client):
    org_id = org_id_holder["id"]

    response = await authorized_client.get(f"/organizations/{org_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["id"] == org_id


@pytest.mark.asyncio
async def test_get_organization_not_found(authorized_client):
    response = await authorized_client.get("/organizations/999")

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.asyncio
async def test_update_organization_success(org_id_holder, authorized_client):
    org_id = org_id_holder["id"]

    response = await authorized_client.put(f"/organizations/{org_id}", json={"name": "Dhaka University New"})

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["name"] == "Dhaka University New"


@pytest.mark.asyncio
async def test_link_user_success(org_id_holder, authorized_client):
    org_id = org_id_holder["id"]

    data = {
        "user_id": 24,
        "role": "ADMIN"
    }

    response = await authorized_client.post(f"/organizations/{org_id}/link-user", json=data)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "User linked successfully"


@pytest.mark.asyncio
async def test_delete_organization_not_found(authorized_client):
    response = await authorized_client.delete("/organizations/999")

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.asyncio
async def test_delete_organization_success(org_id_holder, authorized_client):
    org_id = org_id_holder["id"]

    response = await authorized_client.delete(f"/organizations/{org_id}")

    assert response.status_code == status.HTTP_200_OK
