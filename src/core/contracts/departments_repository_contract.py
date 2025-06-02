from abc import abstractmethod
from typing import Optional

from src.core.contracts.base_repository_contract import BaseRepositoryContract
from src.core.entities.department import Department


class DepartmentsRepositoryContract(BaseRepositoryContract):
    @abstractmethod
    async def get_department_by_code(self, department_code: str) -> Optional[Department]:
        pass
