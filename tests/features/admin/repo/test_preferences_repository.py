from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

import pytest
from src.core.entities.enums.day import Day
from src.core.entities.preference import Preference
from src.core.repositories.preferences_repository import PreferencesRepository
from src.models.preference import PreferenceIn

# Test creation of a Preference using PreferencesRepository
@pytest.mark.asyncio
async def test_preference_create():
    mock_session = AsyncMock()
    repo = PreferencesRepository(db_session=mock_session)

    # Create a PreferenceIn instance to use as input
    preference = PreferenceIn(teacher_id=1, day="SUNDAY", slot_no=1)

    # Call the create method
    result = await repo.create(preference)

    # Assert that the returned result matches the input preference
    assert result == preference

# Test updating a Preference using PreferencesRepository
@pytest.mark.asyncio
async def test_preference_update():
    mock_session = AsyncMock()

    # Updated preference input data
    updated_preference_in = PreferenceIn(
        teacher_id=1,
        day="SUNDAY",
        slot_no=2
    )

    # Mock of the updated preference entity (database entity)
    updated_preference_entity = Preference(
        id=1,
        teacher_id=1,
        day="SUNDAY",
        slot_no=2,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    repo = PreferencesRepository(db_session=mock_session)

    # Mock session's get method to return the updated preference
    mock_session.get.return_value = updated_preference_entity

    # Mock session's execute method to simulate returning the updated entity
    mock_execute_result = MagicMock()
    mock_execute_result.scalar_one_or_none.return_value = updated_preference_entity
    mock_session.execute.return_value = mock_execute_result

    # Call the update method
    result = await repo.update(id=1, obj_data=updated_preference_in)

    # Assert that the update returns the updated preference entity
    assert result == updated_preference_entity

# Test successful deletion of a Preference using PreferencesRepository
@pytest.mark.asyncio
async def test_delete_preference_success():
    mock_session = AsyncMock()
    repo = PreferencesRepository(db_session=mock_session)

    # Preference to be deleted (Preference entity)
    preference = Preference(
        id=1,
        teacher_id=1,
        day="SUNDAY",
        slot_no=1,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    # Mock the execute method to return the preference to be deleted
    mock_execute_result = MagicMock()
    mock_execute_result.scalars.return_value.one_or_none.return_value = preference
    mock_session.execute.return_value = mock_execute_result

    # Call the delete method
    result = await repo.delete(id=1)

    # Check that session.delete and session.commit were awaited with correct arguments
    mock_session.delete.assert_awaited_once_with(preference)
    mock_session.commit.assert_awaited_once()
    assert result is True

# Test deletion of a non-existent Preference using PreferencesRepository
@pytest.mark.asyncio
async def test_delete_preference_not_found():
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

# Test that get_days returns the enum names of the Day enum
@pytest.mark.asyncio
async def test_get_days_returns_enum_names():
    mock_session = AsyncMock()
    repo = PreferencesRepository(db_session=mock_session)

    # Call get_days, which should return the names of the Day enum
    result = await repo.get_days()

    expected = {"items": [day.name for day in Day]}
    assert result == expected