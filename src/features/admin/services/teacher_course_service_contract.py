from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

from src.models.course_teacher_map import CoursesTeachers
from src.models.syllabus.syllabus_models import TeacherCourseOutForSyllabus
from src.models.teacher_course_map import TeachersCourseIn, TeachersCourseOut


class TeacherCourseServiceContract(ABC):
    @abstractmethod
    async def create_teacher_course(self, teacher_course: TeachersCourseIn) -> Optional[TeachersCourseOut]:
        pass

    @abstractmethod
    async def get_teacher_courses(self, page: int = 1, page_size: int = 10, paginate: bool = False) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def update_teacher_course(self, id: int, teacher_course: TeachersCourseIn) -> Optional[TeachersCourseOut]:
        pass

    @abstractmethod
    async def delete_teacher_course(self, id: int) -> bool:
        pass

    @abstractmethod
    async def get_teacher_course_by_id(self, id: int) -> Optional[CoursesTeachers]:
        pass

    @abstractmethod
    async def get_teacher_course_by_course_code(self, department_id: int, course_code: str) -> Optional[TeacherCourseOutForSyllabus]:
        pass