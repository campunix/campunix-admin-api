from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

import pytest

from src.core.entities.enums.room_type import RoomType
from src.core.entities.room import Room
from src.core.repositories.rooms_repository import RoomsRepository
from src.models.room import RoomIn

# Test creation of a Room using RoomsRepository
@pytest.mark.asyncio
async def test_room_create():
    mock_session = AsyncMock()
    repo = RoomsRepository(db_session=mock_session)

    # Create a RoomIn instance to use as input
    room = RoomIn(name="Room-101", code="R-101", department_id=1, room_type=RoomType.LECTURE)

    # Call the create method
    result = await repo.create(room)

    # Assert that the returned result matches the input room
    assert result == room

# Test updating a Room using RoomsRepository
@pytest.mark.asyncio
async def test_room_update():
    mock_session = AsyncMock()

    # Updated room input data
    updated_room_in = RoomIn(
        name="Room-101 Updated",
        code="R-101",
        department_id=1,
        room_type=RoomType.LECTURE
    )

    # Mock of the updated room entity (database entity)
    updated_room_entity = Room(
        id=1,
        name="Room-101 Updated",
        code="R-101",
        department_id=1,
        room_type=RoomType.LECTURE,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    repo = RoomsRepository(db_session=mock_session)

    # Mock session's get method to return the updated room
    mock_session.get.return_value = updated_room_entity

    # Mock session's execute method to simulate returning the updated entity
    mock_execute_result = MagicMock()
    mock_execute_result.scalar_one_or_none.return_value = updated_room_entity
    mock_session.execute.return_value = mock_execute_result

    # Call the update method
    result = await repo.update(id=1, obj_data=updated_room_in)

    # Assert that the update returns the updated room entity
    assert result == updated_room_entity

# Test successful deletion of a Room using RoomsRepository
@pytest.mark.asyncio
async def test_delete_room_success():
    mock_session = AsyncMock()
    repo = RoomsRepository(db_session=mock_session)

    # Room to be deleted (Room entity)
    room = Room(
        id=1,
        name="Room-101",
        code="R-101",
        department_id=1,
        room_type=RoomType.LECTURE,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    # Mock the execute method to return the room to be deleted
    mock_execute_result = MagicMock()
    mock_execute_result.scalars.return_value.one_or_none.return_value = room
    mock_session.execute.return_value = mock_execute_result

    # Call the delete method
    result = await repo.delete(id=1)

    # Check that session.delete and session.commit were awaited with correct arguments
    mock_session.delete.assert_awaited_once_with(room)
    mock_session.commit.assert_awaited_once()
    assert result is True

# Test deletion of a non-existent Room using RoomsRepository
@pytest.mark.asyncio
async def test_delete_room_not_found():
    mock_session = AsyncMock()
    repo = RoomsRepository(db_session=mock_session)

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

# Test that get_room_types returns the values of the RoomType enum
@pytest.mark.asyncio
async def test_get_room_types_returns_enum_values():
    mock_session = AsyncMock()
    repo = RoomsRepository(db_session=mock_session)

    # Call get_room_types, which should return the values of the RoomType enum
    result = await repo.get_room_types()

    expected = {"items": [room.value for room in RoomType]}
    assert result == expected