from abc import abstractmethod
from typing import Optional

from src.core.contracts.base_repository_contract import BaseRepositoryContract
from src.core.entities.semester import Semester


class SemestersRepositoryContract(BaseRepositoryContract):
    @abstractmethod
    async def get_semester_by_year_and_number(self, department: int, year: int, number: int) -> Optional[Semester]:
        pass
