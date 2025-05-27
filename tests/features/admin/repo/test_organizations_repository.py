from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

import pytest

from src.core.entities.preference import Preference
from src.core.repositories.organizations_repository import OrganizationsRepository
from src.core.repositories.preferences_repository import PreferencesRepository
from src.models.organization import OrganizationIn

# Test creating an organization using OrganizationsRepository
@pytest.mark.asyncio
async def test_organization_create():
    mock_session = AsyncMock()
    repo = OrganizationsRepository(db_session=mock_session)

    # OrganizationIn instance to create
    preference = OrganizationIn(name="Test Org")

    # Call create method and check the result
    result = await repo.create(preference)

    assert result == preference

# Test updating an organization using OrganizationsRepository
@pytest.mark.asyncio
async def test_organization_update():
    mock_session = AsyncMock()

    # Input data for updating the organization
    updated_organization_in = OrganizationIn(
        name="Test Org"
    )

    # Mocked entity after update (Preference used as entity)
    updated_organization_entity = Preference(
        id=1,
        name="Test Org",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    repo = OrganizationsRepository(db_session=mock_session)

    # Mock session gets to return fake entity
    mock_session.get.return_value = updated_organization_entity

    # Mock session execute to simulate update result
    mock_execute_result = MagicMock()
    mock_execute_result.scalar_one_or_none.return_value = updated_organization_entity
    mock_session.execute.return_value = mock_execute_result

    # Call update method and check result
    result = await repo.update(id=1, obj_data=updated_organization_in)

    assert result == updated_organization_entity

# Test successful deletion of an organization using PreferencesRepository
@pytest.mark.asyncio
async def test_delete_organization_success():
    mock_session = AsyncMock()
    repo = PreferencesRepository(db_session=mock_session)

    # Organization to be deleted (OrganizationIn)
    preference = OrganizationIn(
        name="Test Org"
    )

    # Mock session executes to return the organization to be deleted
    mock_execute_result = MagicMock()
    mock_execute_result.scalars.return_value.one_or_none.return_value = preference
    mock_session.execute.return_value = mock_execute_result

    # Call delete method
    result = await repo.delete(id=1)

    # Assert delete and commit are awaited properly
    mock_session.delete.assert_awaited_once_with(preference)
    mock_session.commit.assert_awaited_once()
    assert result is True

# Test deletion of a non-existent organization using PreferencesRepository
@pytest.mark.asyncio
async def test_delete_organization_not_found():
    mock_session = AsyncMock()
    repo = PreferencesRepository(db_session=mock_session)

    # Mock session executes to return None (not found)
    mock_execute_result = MagicMock()
    mock_execute_result.scalars.return_value.one_or_none.return_value = None
    mock_session.execute.return_value = mock_execute_result

    # Call delete with an id that does not exist
    result = await repo.delete(id=999)

    # Assert delete and commit are not called
    mock_session.delete.assert_not_called()
    mock_session.commit.assert_not_called()
    assert result is False