from abc import abstractmethod
from typing import Optional, List, Dict, Any

from src.core.contracts.base_repository_contract import BaseRepositoryContract
from src.core.entities.teacher_course import TeacherCourse


class TeacherCoursesRepositoryContract(BaseRepositoryContract):

    @abstractmethod
    async def get_teacher_courses_by_course_id(self, course_id: int) -> Optional[TeacherCourse]:
        pass

    @abstractmethod
    async def get_teacher_courses_by_teacher_id(self, teacher_id: int) -> Optional[TeacherCourse]:
        pass

    @abstractmethod
    async def get_teachers_by_course(self, course_id: int) -> Optional[List[Dict[str, Any]]]:
        pass

    @abstractmethod
    async def get_courses_by_teacher(self, teacher_id: int) -> Optional[List[Dict[str, Any]]]:
        pass
