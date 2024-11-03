from abc import abstractmethod, ABC
from typing import Optional

from src.models.teacher_course import TeacherCourseIn, TeacherCourseOut


class TeacherCourseCourseServiceContract(ABC):
    @abstractmethod
    async def create_teacher_course(self, teacher_course: TeacherCourseIn) -> Optional[TeacherCourseOut]:
        pass

    @abstractmethod
    async def get_teacher_courses(self, page: int = 1, page_size: int = 10, paginate: bool = False):
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
