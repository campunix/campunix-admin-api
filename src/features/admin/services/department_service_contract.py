from abc import ABC, abstractmethod
from typing import Optional

from src.models.department import DepartmentIn, DepartmentOut


class DepartmentServiceContract(ABC):
    @abstractmethod
    async def create_department(self, department: DepartmentIn) -> Optional[DepartmentOut]:
        pass

    @abstractmethod
    async def get_departments(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        pass

    @abstractmethod
    async def update_department(self, id: int, department: DepartmentIn) -> Optional[DepartmentOut]:
        pass

    @abstractmethod
    async def delete_department(self, id: int) -> bool:
        pass

    @abstractmethod
    async def get_department_by_id(self, id: int) -> Optional[DepartmentOut]:
        pass