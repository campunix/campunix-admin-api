from typing import Optional

from src.core.contracts.departments_repository_contract import DepartmentsRepositoryContract
from src.core.entities.department import Department
from src.features.admin.services.department_service_contract import DepartmentServiceContract
from src.models.department import DepartmentOut, DepartmentIn


class DepartmentService(DepartmentServiceContract):
    def __init__(
            self,
            departments_repository: DepartmentsRepositoryContract,
    ):
        self.departments_repository = departments_repository

    async def create_department(self, department: DepartmentIn) -> Optional[DepartmentOut]:
        new_department = await self.departments_repository.create(Department(name=department.name))
        return DepartmentOut(id=new_department.id, name=new_department.name)

    async def get_departments(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        return await self.departments_repository.get_all()

    async def update_department(self, id: int, department: DepartmentIn) -> Optional[DepartmentOut]:
        return await self.departments_repository.update(id, Department(id=id, name=department.name))

    async def delete_department(self, id: int) -> bool:
        return await self.departments_repository.delete(id=id)

    async def get_department_by_id(self, id: int) -> Optional[DepartmentOut]:
        return await self.departments_repository.get_by_id(id)
