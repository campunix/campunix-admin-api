from abc import abstractmethod
from typing import Any, Optional, List

from src.core.contracts.base_repository_contract import BaseRepositoryContract
from src.models.syllabus.syllabus_models import SyllabusParsed


class SyllabusRepositoryContract(BaseRepositoryContract):

    @abstractmethod
    async def save(self, department_id: int, syllabus: SyllabusParsed):
        pass

    @abstractmethod
    async def get_by_department(self, department_id) -> Optional[SyllabusParsed]:
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
