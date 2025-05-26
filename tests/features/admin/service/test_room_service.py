from unittest.mock import AsyncMock

import pytest

from src.core.entities.enums.room_type import RoomType
from src.core.entities.room import Room
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.services.room_service import RoomService
from src.models.room import RoomIn, RoomOut

# Fixture to create a mocked RoomsRepository for each test
@pytest.fixture
def mock_rooms_repository():
    repo = AsyncMock()
    return repo

# Fixture to create a RoomService instance using the mocked repository
@pytest.fixture
def room_service(mock_rooms_repository):
    return RoomService(rooms_repository=mock_rooms_repository)

# Test the creation of a room via the service
@pytest.mark.asyncio
async def test_create_room(room_service, mock_rooms_repository):
    room_in = RoomIn(name="Lab 1", code="LAB1", department_id=1, room_type=RoomType.LAB)
    fake_room_entity = Room(id=1, name="Lab 1", code="LAB1", department_id=1, room_type=RoomType.LAB)
    mock_rooms_repository.create.return_value = fake_room_entity

    result = await room_service.create_room(room_in)

    assert isinstance(result, RoomOut)
    assert result.name == "Lab 1"

# Test retrieving rooms with filters and pagination
@pytest.mark.asyncio
async def test_get_rooms_with_filters(room_service, mock_rooms_repository):
    mock_rooms_repository.get_all.return_value = {
        "items": [
            {
                "id": 1,
                "name": "Lab 101",
                "code": "LAB1",
                "department_id": 1,
                "room_type": RoomType.LAB,
                "created_at": None,
                "updated_at": None
            }
        ],
        "current_page": 1,
        "total_pages": 1,
        "page_size": 20,
        "total_items": 1
    }

    result = await room_service.get_rooms(page=1, page_size=20, paginate=True)

    assert isinstance(result["items"][0], RoomOut)
    assert result["items"][0].code == "LAB1"

# Test a successful room update operation
@pytest.mark.asyncio
async def test_update_room_success(room_service, mock_rooms_repository):
    room_in = RoomIn(name="Lab 101 Updated", code="LAB1", department_id=1, room_type=RoomType.LAB)
    fake_room_entity = Room(id=1, name="Lab 101 Updated", code="LAB1", department_id=1, room_type=RoomType.LAB)
    mock_rooms_repository.update.return_value = fake_room_entity

    result = await room_service.update_room(1, room_in)

    assert isinstance(result, RoomOut)
    assert result.name == "Lab 101 Updated"

# Test updating a room that does not exist (should raise NotFoundException)
@pytest.mark.asyncio
async def test_update_room_not_found(room_service, mock_rooms_repository):
    room_in = RoomIn(name="X", code="X", department_id=1, room_type="LAB")
    mock_rooms_repository.update.return_value = None

    with pytest.raises(NotFoundException):
        await room_service.update_room(999, room_in)

# Test successful deletion of a room
@pytest.mark.asyncio
async def test_delete_room_success(room_service, mock_rooms_repository):
    mock_rooms_repository.delete.return_value = True

    result = await room_service.delete_room(1)
    assert result is True

# Test deletion of a non-existent room (should raise NotFoundException)
@pytest.mark.asyncio
async def test_delete_room_failure(room_service, mock_rooms_repository):
    mock_rooms_repository.delete.return_value = False

    with pytest.raises(NotFoundException):
        await room_service.delete_room(999)

# Test retrieving a room by id successfully
@pytest.mark.asyncio
async def test_get_room_by_id_success(room_service, mock_rooms_repository):
    mock_rooms_repository.get_by_id.return_value = Room(id=1, name="Room", code="R1", department_id=1,
                                                        room_type=RoomType.LAB)

    result = await room_service.get_room_by_id(1)

    assert isinstance(result, RoomOut)
    assert result.code == "R1"

# Test retrieving a room by id when it does not exist (should raise NotFoundException)
@pytest.mark.asyncio
async def test_get_room_by_id_not_found(room_service, mock_rooms_repository):
    mock_rooms_repository.get_by_id.return_value = None

    with pytest.raises(NotFoundException):
        await room_service.get_room_by_id(999)

# Test retrieving all room types successfully
@pytest.mark.asyncio
async def test_get_room_types_success(room_service, mock_rooms_repository):
    mock_rooms_repository.get_room_types.return_value = {
        "CLASSROOM": "Classroom",
        "LAB": "Laboratory"
    }

    result = await room_service.get_room_types()

    assert "CLASSROOM" in result

# Test retrieving room types when repository returns None (should raise NotFoundException)
@pytest.mark.asyncio
async def test_get_room_types_failure(room_service, mock_rooms_repository):
    mock_rooms_repository.get_room_types.return_value = None

    with pytest.raises(NotFoundException):
        await room_service.get_room_types()