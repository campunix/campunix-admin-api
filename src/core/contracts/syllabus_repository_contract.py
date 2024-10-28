from abc import ABC, abstractmethod
from typing import Any

from src.models.syllabus.syllabus_models import SyllabusOut


class SyllabusRepositoryContract(ABC):

    @abstractmethod
    async def save(self, department_id: int, syllabus: dict[str, Any]):
        pass

    @abstractmethod
    async def getByDeptID(self, department_id) -> SyllabusOut:
        pass

    @abstractmethod
    async def getByDeptIDAndCourseCode(self, department_id, course_code) -> SyllabusOut:
        pass
