import pytest
from unittest.mock import AsyncMock, patch
from pydantic import BaseModel
from typing import List

from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.services.PreferenceService import PreferenceService
from src.models.department import DepartmentOut
from src.models.preference import PreferenceIn, PreferenceOut
from src.models.teacher import TeacherOut
from src.core.entities.preference import Preference
from src.core.entities.enums.day import Day

# Fixture for a mocked preferences repository
@pytest.fixture
def mock_preferences_repository():
    return AsyncMock()

# Fixture for a mocked teacher service
@pytest.fixture
def mock_teacher_service():
    return AsyncMock()

# Fixture for constructing the PreferenceService with mocked dependencies
@pytest.fixture
def service(mock_preferences_repository, mock_teacher_service):
    return PreferenceService(
        preferences_repository=mock_preferences_repository,
        teacher_service=mock_teacher_service
    )

# Helper to construct a mock TeacherOut object
def get_mock_teacher():
    return TeacherOut(
        id=1,
        full_name="John Doe",
        email="john@example.com",
        designation="Professor",
        status="active",
        department=DepartmentOut(id=1, name="Computer Science", code="CSE"),
        courses=[]
    )

# Test the creation of a preference where teacher exists
@pytest.mark.asyncio
async def test_create_preference_success(service, mock_preferences_repository, mock_teacher_service):
    # Mock the teacher service to return a teacher, and repository to return a preference entity
    mock_teacher_service.get_teacher_by_id.return_value = get_mock_teacher()
    mock_preferences_repository.create.return_value = Preference(id=1, teacher_id=1, day=Day.SUNDAY, slot_no=2)

    preference = PreferenceIn(teacher_id=1, day="SUNDAY", slot_no=2)
    result = await service.create_preference(preference)

    assert result.teacher_id == 1
    assert result.teacher_name == "John Doe"

# Test error when trying to create a preference for a non-existent teacher
@pytest.mark.asyncio
async def test_create_preference_teacher_not_found(service, mock_teacher_service):
    mock_teacher_service.get_teacher_by_id.return_value = None

    with pytest.raises(NotFoundException):
        await service.create_preference(PreferenceIn(teacher_id=999, day="MONDAY", slot_no=1))

# Test fetching all preferences (entity_to_model_list is patched)
@pytest.mark.asyncio
@patch("src.features.admin.services.PreferenceService.entity_to_model_list")
async def test_get_preferences(mock_entity_to_model_list, service, mock_preferences_repository):
    # Mock repository get_all and entity_to_model_list
    mock_preferences_repository.get_all.return_value = {
        "items": [{"id": 1, "teacher_id": 1, "teacher_name": "John Doe", "day": "SUNDAY", "slot_no": 2}],
        "page_size": 10, "total_items": 1, "total_pages": 1, "current_page": 1
    }
    mock_entity_to_model_list.return_value = {"items": [], "page_size": 10}

    result = await service.get_preferences()
    assert isinstance(result, dict)

# Test fetching preferences by teacher id (entity_to_model_list is patched)
@pytest.mark.asyncio
@patch("src.features.admin.services.PreferenceService.entity_to_model_list")
async def test_get_preferences_by_teacher_id(mock_entity_to_model_list, service, mock_preferences_repository):
    # Mock repository get_all and entity_to_model_list
    mock_preferences_repository.get_all.return_value = {
        "items": [{"id": 1, "teacher_id": 1, "teacher_name": "John Doe", "day": "SUNDAY", "slot_no": 2}],
        "page_size": 10, "total_items": 1, "total_pages": 1, "current_page": 1
    }
    mock_entity_to_model_list.return_value = {"items": [], "page_size": 10}

    result = await service.get_preferences_by_teacher_id(teacher_id=1)
    assert isinstance(result, dict)

# Test updating a preference successfully
@pytest.mark.asyncio
async def test_update_preference_success(service, mock_preferences_repository, mock_teacher_service):
    # Mock teacher service and repository update
    mock_teacher_service.get_teacher_by_id.return_value = get_mock_teacher()
    mock_preferences_repository.update.return_value = Preference(id=1, teacher_id=1, day=Day.MONDAY, slot_no=1)

    result = await service.update_preference(
        id=1,
        preference=PreferenceIn(teacher_id=1, day="MONDAY", slot_no=1)
    )

    assert isinstance(result, PreferenceOut)
    assert result.teacher_id == 1

# Test error when updating a non-existent preference
@pytest.mark.asyncio
async def test_update_preference_not_found(service, mock_preferences_repository, mock_teacher_service):
    # Mock teacher exists, but repository update returns None (not found)
    mock_teacher_service.get_teacher_by_id.return_value = get_mock_teacher()
    mock_preferences_repository.update.return_value = None

    with pytest.raises(NotFoundException):
        await service.update_preference(
            id=999,
            preference=PreferenceIn(teacher_id=1, day="MONDAY", slot_no=1)
        )