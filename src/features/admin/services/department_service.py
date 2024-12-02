from typing import Optional

from src.core.contracts.departments_repository_contract import DepartmentsRepositoryContract
from src.core.entities.department import Department
from src.core.exceptions.not_found_exception import NotFoundException
from src.features.admin.services.department_service_contract import DepartmentServiceContract
from src.models.department import DepartmentOut, DepartmentIn


class DepartmentService(DepartmentServiceContract):
    def __init__(
            self,
            departments_repository: DepartmentsRepositoryContract,
    ):
        self.departments_repository = departments_repository

    async def create_department(self, department: DepartmentIn) -> Optional[DepartmentOut]:
        new_department = await self.departments_repository.create(
            Department(
                name=department.name,
                code=department.code,
                organization_id=department.organization_id,
                created_by=department.created_by,
            )
        )

        return DepartmentOut(id=new_department.id, name=new_department.name, code=new_department.code)

    async def get_departments(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        data = await self.departments_repository.get_all()

        departments = {
            "departments": [
                {key: value for key, value in item.items() if key not in ["organization_id", "created_at", "updated_at"]}
                for item in data["items"]
            ]
        }
        return departments

    async def update_department(self, id: int, department: DepartmentIn) -> Optional[DepartmentOut]:
        return await (
            self
            .departments_repository
            .update(
                id,
                Department(
                    id=id,
                    code=department.code,
                    name=department.name,
                    created_by=department.created_by,
                )
            )
        )

    async def delete_department(self, id: int) -> bool:
        return await self.departments_repository.delete(id=id)

    async def get_department_by_id(self, id: int) -> Optional[DepartmentOut]:
        department = await self.departments_repository.get_by_id(id)

        if not department:
            raise NotFoundException

        return DepartmentOut(id=department.id, name=department.name, code=department.code)
