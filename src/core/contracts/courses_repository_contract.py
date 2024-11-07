from abc import abstractmethod
from typing import Optional

from src.core.contracts.base_repository_contract import BaseRepositoryContract
from src.core.entities.course import Course


class CoursesRepositoryContract(BaseRepositoryContract):
    @abstractmethod
    async def get_course_by_code(self, course_code: str, department_id: int) -> Optional[Course]:
        pass
