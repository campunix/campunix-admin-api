from abc import abstractmethod
from typing import Optional, List

from src.core.contracts.base_repository_contract import BaseRepositoryContract
from src.core.entities.semester import Semester


class SemestersRepositoryContract(BaseRepositoryContract):
    @abstractmethod
    async def get_semester_by_year_and_number(self, department: int, year: int, number: int) -> Optional[Semester]:
        pass

    @abstractmethod
    async def get_semesters_by_department_id(self, department: int) -> Optional[List[Semester]]:
        pass