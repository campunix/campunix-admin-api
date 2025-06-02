import pytest
from fastapi import status

# Fixture to hold and share the created organization's ID across tests
@pytest.fixture(scope="module")
def org_id_holder():
    return {"id": 25}

# Test creating an organization and saving its ID for future tests
@pytest.mark.asyncio
async def test_create_organization(org_id_holder, authorized_client):
    test_org = {"name": "Dhaka University"}

    # Send a POST request to create a new organization
    response = await authorized_client.post("/organizations", json=test_org)

    # Assert successful creation and correct name in response
    assert response.status_code == status.HTTP_200_OK
    org_id_holder["id"] = response.json()["data"]["id"]  # Store ID for later tests
    assert response.json()["data"]["name"] == "Dhaka University"

# Test fetching all organizations
@pytest.mark.asyncio
async def test_get_all_organization(authorized_client):
    response = await authorized_client.get("/organizations")

    # Assert successful response and at least one organization exists
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()["data"]) > 0

# Test fetching a single organization by its ID
@pytest.mark.asyncio
async def test_get_organization_found(org_id_holder, authorized_client):
    org_id = org_id_holder["id"]

    response = await authorized_client.get(f"/organizations/{org_id}")

    # Assert the organization exists and ID matches
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["id"] == org_id

# Test fetching an organization that does not exist
@pytest.mark.asyncio
async def test_get_organization_not_found(authorized_client):
    response = await authorized_client.get("/organizations/999")

    # Assert 404 status code for not found
    assert response.status_code == status.HTTP_404_NOT_FOUND

# Test updating an existing organization
@pytest.mark.asyncio
async def test_update_organization_success(org_id_holder, authorized_client):
    org_id = org_id_holder["id"]

    # Send PUT request to update organization name
    response = await authorized_client.put(f"/organizations/{org_id}", json={"name": "Dhaka University New"})

    # Assert a successful update and name change
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["data"]["name"] == "Dhaka University New"

# Test linking a user to an organization
@pytest.mark.asyncio
async def test_link_user_success(org_id_holder, authorized_client):
    org_id = org_id_holder["id"]

    data = {
        "user_id": 24,
        "role": "ADMIN"
    }

    # Send a POST request to link a user as an admin to the organization
    response = await authorized_client.post(f"/organizations/{org_id}/link-user", json=data)

    # Assert successful user linking and correct message
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "User linked successfully"

# Test deleting a non-existent organization
@pytest.mark.asyncio
async def test_delete_organization_not_found(authorized_client):
    response = await authorized_client.delete("/organizations/999")

    # Assert 404 status code for not found
    assert response.status_code == status.HTTP_404_NOT_FOUND

# Test deleting an existing organization
@pytest.mark.asyncio
async def test_delete_organization_success(org_id_holder, authorized_client):
    org_id = org_id_holder["id"]

    # Send DELETE request to remove the organization
    response = await authorized_client.delete(f"/organizations/{org_id}")

    # Assert successful deletion
    assert response.status_code == status.HTTP_200_OK