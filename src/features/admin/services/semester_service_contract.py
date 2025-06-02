from abc import ABC, abstractmethod
from typing import Optional

from src.models.semester import SemesterIn, SemesterOut


class SemesterServiceContract(ABC):
    @abstractmethod
    async def create_semester(self, semester: SemesterIn) -> Optional[SemesterOut]:
        pass

    @abstractmethod
    async def get_semesters(self, page: int = 1, page_size: int = 10, paginate: bool = False):
        pass

    @abstractmethod
    async def update_semester(self, id: int, semester: SemesterIn) -> Optional[SemesterOut]:
        pass

    @abstractmethod
    async def delete_semester(self, id: int) -> bool:
        pass

    @abstractmethod
    async def get_semester_by_id(self, id: int) -> Optional[SemesterOut]:
        pass