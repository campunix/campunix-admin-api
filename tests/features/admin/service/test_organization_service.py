import pytest
from unittest.mock import AsyncMock, patch
from datetime import datetime, timezone

from src.features.admin.services.organization_service import OrganizationService
from src.models.organization import OrganizationIn, OrganizationOut
from src.core.entities.organization import Organization

# Fixture to provide a mocked organizations repository for each test
@pytest.fixture
def mock_organizations_repository():
    return AsyncMock()

# Fixture to provide an OrganizationService instance using the mocked repository
@pytest.fixture
def organization_service(mock_organizations_repository):
    return OrganizationService(organizations_repository=mock_organizations_repository)

# Test the creation of an organization using the service
@pytest.mark.asyncio
async def test_create_organization(organization_service, mock_organizations_repository):
    # Prepare input and mock return value
    organization_in = OrganizationIn(name="Test Org")
    mock_organizations_repository.create.return_value = Organization(id=1, name="Test Org")

    # Call the service method
    result = await organization_service.create_organization(organization_in)

    # Assert the result is an OrganizationOut instance and has correct values
    assert isinstance(result, OrganizationOut)
    assert result.id == 1
    assert result.name == "Test Org"
    # Ensure the repository's create method was called with the correct argument
    mock_organizations_repository.create.assert_called_once_with(Organization(name="Test Org"))

# Test fetching organizations using the service, with entity_to_model_list patch
@pytest.mark.asyncio
@patch("src.features.admin.services.organization_service.entity_to_model_list")
async def test_get_organizations(mock_entity_to_model_list, organization_service, mock_organizations_repository):
    # Mock the repository's get_all method to return organization dicts
    mock_organizations_repository.get_all.return_value = [
        {
            "id": 1,
            "name": "Test Org",
            "created_at": datetime.now(timezone.utc),
            "updated_at": None
        }
    ]
    # Mock the entity_to_model_list function to return formatted results
    mock_entity_to_model_list.return_value = {
        "items": [OrganizationOut(id=1, name="Test Org")],
        "current_page": 1,
        "total_pages": 1,
        "page_size": 10,
        "total_items": 1
    }

    # Call the service method
    result = await organization_service.get_organizations(page=1, page_size=10, paginate=True)

    # Assert the result is correctly formatted and contains OrganizationOut items
    assert isinstance(result["items"][0], OrganizationOut)
    assert result["items"][0].name == "Test Org"
    # Ensure entity_to_model_list was called once
    mock_entity_to_model_list.assert_called_once()

# Test updating an organization using the service
@pytest.mark.asyncio
async def test_update_organization(organization_service, mock_organizations_repository):
    # Prepare input and mock the update return value
    organization_in = OrganizationIn(name="Updated Org")
    updated_org = Organization(id=1, name="Updated Org")
    mock_organizations_repository.update.return_value = updated_org

    # Call the service method
    result = await organization_service.update_organization(id=1, organization=organization_in)

    # Assert the result matches the updated organization
    assert result == updated_org
    # Ensure the update method was called with the correct arguments
    mock_organizations_repository.update.assert_called_once_with(1, Organization(id=1, name="Updated Org"))

# Test deleting an organization using the service
@pytest.mark.asyncio
async def test_delete_organization(organization_service, mock_organizations_repository):
    # Mock the delete method to return True (success)
    mock_organizations_repository.delete.return_value = True

    # Call the service method
    result = await organization_service.delete_organization(id=1)

    # Assert deletion was successful
    assert result is True
    # Ensure the delete method was called with the correct id
    mock_organizations_repository.delete.assert_called_once_with(1)

# Test fetching an organization by id using the service
@pytest.mark.asyncio
async def test_get_organization_by_id(organization_service, mock_organizations_repository):
    # Mock the get_by_id method to return an Organization entity
    mock_organizations_repository.get_by_id.return_value = Organization(id=1, name="Org1")

    # Call the service method
    result = await organization_service.get_organization_by_id(id=1)

    # Assert the result matches the expected organization
    assert result.id == 1
    assert result.name == "Org1"
    # Ensure the get_by_id method was called with the correct id
    mock_organizations_repository.get_by_id.assert_called_once_with(1)