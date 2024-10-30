from abc import ABC, abstractmethod

from fastapi import File

from src.core.entities.syllabus.syllabus import Syllabus
from src.models.syllabus.syllabus_models import SyllabusOut


class SyllabusServiceContract(ABC):

    @abstractmethod
    async def save(self, file: File(...)) -> Syllabus:
        pass

    @abstractmethod
    def getByDepartmentID(self, department_id: int) -> SyllabusOut:
        pass

    @abstractmethod
    def getByDeptIDAndCourseCode(self, department_id: int, course_code: str) -> SyllabusOut:
        pass

    @abstractmethod
    def getSyllabus(self):
        pass
