from abc import ABC, abstractmethod
from typing import Optional, Any

from fastapi import File

from src.models.syllabus.syllabus_models import SyllabusParsed


class SyllabusServiceContract(ABC):

    @abstractmethod
    async def save(self, file: File(...)) -> SyllabusParsed:
        pass

    @abstractmethod
    def get_by_department_id(self, department_id: int) -> Optional[SyllabusParsed]:
        pass

    @abstractmethod
    async def get_course_list(self, department_id: int) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def getByDeptIDAndSemesterCode(self, department_id: int, semester_code: int) -> Optional[SyllabusParsed]:
        pass

    @abstractmethod
    async def updateSyllabus(self, department_id: int, semester_code: int, course_code: str, course_title: str) -> \
    Optional[SyllabusParsed]:
        pass

    @abstractmethod
    async def template(self, department_id: int) -> Optional[Any]:
        pass
