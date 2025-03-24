from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, List

from src.models.course import CourseOut
from src.models.teacher import TeacherOut
from src.models.teacher_course import TeacherCourseIn, TeacherCourseOut


class TeacherCourseServiceContract(ABC):
    @abstractmethod
    async def create_teacher_course(self, teacher_course: TeacherCourseIn) -> Optional[TeacherCourseOut]:
        pass

    @abstractmethod
    async def get_teacher_courses(self, page: int = 1, page_size: int = 10, paginate: bool = False) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def update_teacher_course(self, id: int, teacher_course: TeacherCourseIn) -> Optional[TeacherCourseOut]:
        pass

    @abstractmethod
    async def delete_teacher_course(self, id: int) -> bool:
        pass

    @abstractmethod
    async def get_teacher_course_by_id(self, id: int) -> Optional[TeacherCourseOut]:
        pass

    @abstractmethod
    async def get_teacher_course_by_course_code(self, department_id: int, course_code: str) -> Optional[
        TeacherCourseOut]:
        pass

    @abstractmethod
    async def assign_teachers(self, course_id: int, teachers: List[int]) -> Optional[CourseOut]:
        pass

    @abstractmethod
    async def assign_courses(self, teacher_id: int, courses: List[int]) -> Optional[TeacherOut]:
        pass
