import pytest
from unittest.mock import AsyncMock

from src.features.admin.services.department_service import DepartmentService
from src.models.department import DepartmentIn, DepartmentOut
from src.core.entities.department import Department
from src.core.exceptions.not_found_exception import NotFoundException

# Fixture for a mocked DepartmentsRepository
@pytest.fixture
def mock_departments_repository():
    return AsyncMock()

# Fixture for DepartmentService using the mocked repository
@pytest.fixture
def service(mock_departments_repository):
    return DepartmentService(departments_repository=mock_departments_repository)

# Test the successful creation of a department via the service
@pytest.mark.asyncio
async def test_create_department_success(service, mock_departments_repository):
    # Mock the repository's create method to return a Department entity
    mock_departments_repository.create.return_value = Department(
        id=1, name="Computer Science", code="CSE", organization_id=1, created_by=1
    )

    # Input for department creation
    department_in = DepartmentIn(name="Computer Science", code="CSE", organization_id=1, created_by=1)
    # Call the service method
    result = await service.create_department(department_in)

    # Assert the result is a DepartmentOut and has correct data
    assert isinstance(result, DepartmentOut)
    assert result.name == "Computer Science"
    assert result.code == "CSE"
    # Ensure the create method was awaited exactly once
    mock_departments_repository.create.assert_awaited_once()

# Test fetching all departments with pagination
@pytest.mark.asyncio
async def test_get_departments_success(service, mock_departments_repository):
    # Mock repository's get_all to return a paginated result
    mock_departments_repository.get_all.return_value = {
        "items": [
            {
                "id": 1,
                "name": "CS",
                "code": "CSE"
            }
        ],
        "total_items": 1,
        "page_size": 10,
        "total_pages": 1,
        "current_page": 1
    }

    # Call the service method
    result = await service.get_departments(page=1, page_size=10, paginate=True)
    # Assert that result structure and types are as expected
    assert "items" in result
    assert isinstance(result["items"], list)
    assert isinstance(result["items"][0], DepartmentOut)

# Test updating a department via the service
@pytest.mark.asyncio
async def test_update_department_success(service, mock_departments_repository):
    # Mock repository's update to return a DepartmentOut
    mock_departments_repository.update.return_value = DepartmentOut(
        id=1, name="Updated CS", code="UCS"
    )

    # Input for update
    department_in = DepartmentIn(name="Updated CS", code="UCS", organization_id=1, created_by=1)
    # Call the service method
    result = await service.update_department(id=1, department=department_in)

    # Assert result is DepartmentOut and has updated data
    assert isinstance(result, DepartmentOut)
    assert result.name == "Updated CS"
    # Assert that update was called with the right arguments
    mock_departments_repository.update.assert_awaited_once_with(
        1, Department(id=1, name="Updated CS", code="UCS", created_by=1)
    )

# Test successful deletion of a department by id
@pytest.mark.asyncio
async def test_delete_department_success(service, mock_departments_repository):
    # Mock delete to return True (success)
    mock_departments_repository.delete.return_value = True

    # Call the service method
    result = await service.delete_department(id=1)

    # Assert deletion was successful
    assert result is True
    mock_departments_repository.delete.assert_awaited_once_with(id=1)

# Test fetching a department by id, department exists
@pytest.mark.asyncio
async def test_get_department_by_id_success(service, mock_departments_repository):
    # Mock get_by_id to return a Department entity
    mock_departments_repository.get_by_id.return_value = Department(
        id=1, name="CS", code="CSE", organization_id=1, created_by=1
    )

    # Call the service method
    result = await service.get_department_by_id(id=1)

    # Assert result is DepartmentOut and has correct id
    assert isinstance(result, DepartmentOut)
    assert result.id == 1
    mock_departments_repository.get_by_id.assert_awaited_once_with(1)

# Test fetching a department by id, department does not exist
@pytest.mark.asyncio
async def test_get_department_by_id_not_found(service, mock_departments_repository):
    # Mock get_by_id to return None (not found)
    mock_departments_repository.get_by_id.return_value = None

    # Assert that NotFoundException is raised when department is not found
    with pytest.raises(NotFoundException):
        await service.get_department_by_id(id=999)