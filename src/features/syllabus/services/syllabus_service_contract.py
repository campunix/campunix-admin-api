from abc import ABC, abstractmethod
from typing import Optional, Any, List, Dict

from fastapi import File

from src.models.syllabus.syllabus_models import SyllabusParsed, SyllabusIn, SyllabusOut


class SyllabusServiceContract(ABC):

    @abstractmethod
    async def save(
            self,
            file: File(...),
            title: Optional[str] = None,
            description: Optional[str] = None,
            calendar_year: Optional[str] = None,
            is_active: bool = False
    ) -> SyllabusOut:
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

    @abstractmethod
    async def create_syllabus(self, syllabus_in: SyllabusIn) -> Optional[SyllabusOut]:
        pass

    @abstractmethod
    async def update_syllabus(self, id: int, syllabus_in: SyllabusIn) -> Optional[SyllabusOut]:
        pass

    @abstractmethod
    async def get_all_syllabuses(self, page: int = 1, page_size: int = 10, paginate: bool = False,
                                 department_id: int = None) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def get_syllabus(self, id: int) -> Optional[SyllabusOut]:
        pass
