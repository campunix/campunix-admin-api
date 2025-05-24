import pytest
from unittest.mock import AsyncMock

from src.core.entities.enums.room_type import RoomType
from src.core.entities.room import Room
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.services.room_service import RoomService
from src.models.room import RoomIn, RoomOut


@pytest.fixture
def mock_rooms_repository():
    repo = AsyncMock()
    return repo


@pytest.fixture
def room_service(mock_rooms_repository):
    return RoomService(rooms_repository=mock_rooms_repository)


@pytest.mark.asyncio
async def test_create_room(room_service, mock_rooms_repository):
    room_in = RoomIn(name="Lab 1", code="LAB1", department_id=1, room_type="LAB")
    fake_room_entity = Room(id=1, name="Lab 1", code="LAB1", department_id=1, room_type=RoomType.LAB)
    mock_rooms_repository.create.return_value = fake_room_entity

    result = await room_service.create_room(room_in)

    assert isinstance(result, RoomOut)
    assert result.name == "Lab 1"


@pytest.mark.asyncio
async def test_get_rooms_with_filters(room_service, mock_rooms_repository):
    mock_rooms_repository.get_all.return_value = {
        "data": [
            Room(id=1, name="CSE 101", code="CSE101", department_id=1, room_type=RoomType.LECTURE)
        ],
        "total": 1,
        "page": 1,
        "page_size": 10
    }

    result = await room_service.get_rooms(search_query="CSE", department_id=1, paginate=True)

    assert isinstance(result["data"][0], RoomOut)
    assert result["data"][0].code == "CSE101"


@pytest.mark.asyncio
async def test_update_room_success(room_service, mock_rooms_repository):
    room_in = RoomIn(name="Updated Room", code="NEW1", department_id=1, room_type="LAB")
    fake_room_entity = Room(id=1, name="Updated Room", code="NEW1", department_id=1, room_type=RoomType.LAB)
    mock_rooms_repository.update.return_value = fake_room_entity

    result = await room_service.update_room(1, room_in)

    assert isinstance(result, RoomOut)
    assert result.name == "Updated Room"


@pytest.mark.asyncio
async def test_update_room_not_found(room_service, mock_rooms_repository):
    room_in = RoomIn(name="X", code="X", department_id=1, room_type="LAB")
    mock_rooms_repository.update.return_value = None

    with pytest.raises(NotFoundException):
        await room_service.update_room(999, room_in)


@pytest.mark.asyncio
async def test_delete_room_success(room_service, mock_rooms_repository):
    mock_rooms_repository.delete.return_value = True

    result = await room_service.delete_room(1)
    assert result is True


@pytest.mark.asyncio
async def test_delete_room_failure(room_service, mock_rooms_repository):
    mock_rooms_repository.delete.return_value = False

    with pytest.raises(NotFoundException):
        await room_service.delete_room(999)


@pytest.mark.asyncio
async def test_get_room_by_id_success(room_service, mock_rooms_repository):
    mock_rooms_repository.get_by_id.return_value = Room(id=1, name="Room", code="R1", department_id=1,
                                                        room_type=RoomType.LAB)

    result = await room_service.get_room_by_id(1)

    assert isinstance(result, RoomOut)
    assert result.code == "R1"


@pytest.mark.asyncio
async def test_get_room_by_id_not_found(room_service, mock_rooms_repository):
    mock_rooms_repository.get_by_id.return_value = None

    with pytest.raises(NotFoundException):
        await room_service.get_room_by_id(999)


@pytest.mark.asyncio
async def test_get_room_types_success(room_service, mock_rooms_repository):
    mock_rooms_repository.get_room_types.return_value = {
        "CLASSROOM": "Classroom",
        "LAB": "Laboratory"
    }

    result = await room_service.get_room_types()

    assert "CLASSROOM" in result


@pytest.mark.asyncio
async def test_get_room_types_failure(room_service, mock_rooms_repository):
    mock_rooms_repository.get_room_types.return_value = None

    with pytest.raises(NotFoundException):
        await room_service.get_room_types()
