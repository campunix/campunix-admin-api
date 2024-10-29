from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from src.core.entities.department import Department, DepartmentBase

class DepartmentsRepositoryContract(ABC):
    @abstractmethod
    async def createDepartment(self, department: DepartmentBase) -> Department:
        pass

    @abstractmethod
    async def get_department_by_id(self, id: int) -> Optional[Department]:
        pass

    @abstractmethod
    async def get_all_departments(
        self,
        page: int = 1,
        page_size: int = 10,
        paginate: bool = False,
        filters: Optional[List[Any]] = None, 
    ) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def update_depatment(self, id: id, department: DepartmentBase) -> Department:
        pass

    @abstractmethod
    async def delete_department(self, id: id) -> bool:
        pass
