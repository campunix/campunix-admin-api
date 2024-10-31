from abc import ABC, abstractmethod
from typing import Any, Optional

from src.models.syllabus.syllabus_models import Course, SyllabusOut


class SyllabusRepositoryContract(ABC):

    @abstractmethod
    async def save(self, department_id: int, syllabus: dict[str, Any]):
        pass

    @abstractmethod
    async def getByDeptID(self, department_id) -> Optional[SyllabusOut]:
        pass

    @abstractmethod
    async def getByDeptIDAndCourseCode(self, department_id, course_code) -> Optional[SyllabusOut]:
        pass