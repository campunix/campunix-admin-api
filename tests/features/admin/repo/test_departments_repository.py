from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

import pytest

from src.core.entities.department import Department
from src.core.entities.preference import Preference
from src.core.repositories.departments_repository import DepartmentsRepository
from src.core.repositories.organizations_repository import OrganizationsRepository
from src.core.repositories.preferences_repository import PreferencesRepository
from src.models.department import DepartmentIn
from src.models.organization import OrganizationIn

# Test the creation of a Department using DepartmentsRepository
@pytest.mark.asyncio
async def test_department_create():
    mock_session = AsyncMock()
    repo = DepartmentsRepository(db_session=mock_session)

    # Create a DepartmentIn instance to use as input
    department = DepartmentIn(
        name="Test Department",
        code="TE",
        organization_id=1,
        created_by=1
    )

    # Call the create method
    result = await repo.create(department)

    # Assert that the returned result matches the input department
    assert result == department


# Test updating a department using OrganizationsRepository
@pytest.mark.asyncio
async def test_department_update():
    mock_session = AsyncMock()

    # Updated department input data
    updated_department_in = DepartmentIn(
        name="Test Department Updated",
        code="TE",
        organization_id=1,
        created_by=1
    )

    # Mock of the updated department entity (database entity)
    updated_department_entity = Department(
        id=1,
        name="Test Department Updated",
        code="TE",
        organization_id=1,
        created_by=1,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    repo = OrganizationsRepository(db_session=mock_session)

    # Mock session's get method to return the updated department
    mock_session.get.return_value = updated_department_entity

    # Mock session's execute method to simulate returning the updated entity
    mock_execute_result = MagicMock()
    mock_execute_result.scalar_one_or_none.return_value = updated_department_entity
    mock_session.execute.return_value = mock_execute_result

    # Call the update method
    result = await repo.update(id=1, obj_data=updated_department_in)

    # Assert that the update returns the updated department entity
    assert result == updated_department_entity


# Test successful deletion of a department using PreferencesRepository
@pytest.mark.asyncio
async def test_delete_department_success():
    mock_session = AsyncMock()
    repo = PreferencesRepository(db_session=mock_session)

    # Department to be deleted (as DepartmentIn)
    department = DepartmentIn(
        name="Test Department",
        code="TE",
        organization_id=1,
        created_by=1
    )

    # Mock the execute method to return the department to be deleted
    mock_execute_result = MagicMock()
    mock_execute_result.scalars.return_value.one_or_none.return_value = department
    mock_session.execute.return_value = mock_execute_result

    # Call the delete method
    result = await repo.delete(id=1)

    # Check that session.delete and session.commit were awaited with correct arguments
    mock_session.delete.assert_awaited_once_with(department)
    mock_session.commit.assert_awaited_once()
    assert result is True


# Test deletion of a non-existent organization using PreferencesRepository
@pytest.mark.asyncio
async def test_delete_organization_not_found():
    mock_session = AsyncMock()
    repo = PreferencesRepository(db_session=mock_session)

    # Mock the execute method to return None (not found)
    mock_execute_result = MagicMock()
    mock_execute_result.scalars.return_value.one_or_none.return_value = None
    mock_session.execute.return_value = mock_execute_result

    # Call the delete method with a non-existent id
    result = await repo.delete(id=999)

    # Ensure delete and commit are not called when nothing is found
    mock_session.delete.assert_not_called()
    mock_session.commit.assert_not_called()
    assert result is False