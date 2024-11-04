from abc import ABC, abstractmethod
from typing import Any, Optional, List

from src.models.syllabus.syllabus_models import SyllabusParsed


class SyllabusRepositoryContract(ABC):

    @abstractmethod
    async def save(self, syllabus: SyllabusParsed):
        pass

    @abstractmethod
    async def getByDeptID(self, department_id) -> Optional[SyllabusParsed]:
        pass

    @abstractmethod
    async def getByDeptIDAndSemesterCode(self, department_id: int, semester_code: int) -> Optional[SyllabusParsed]:
        pass

    @abstractmethod
    async def updateSyllabus(self, department_id: int, semester_code: int, course_code: str, course_type: str) -> \
            Optional[
                SyllabusParsed]:
        pass

    @abstractmethod
    async def getSemesters(self, department_id: int) -> Optional[List[Any]]:
        pass

    @abstractmethod
    async def getCourses(self, department_id: int) -> Optional[List[Any]]:
        pass
