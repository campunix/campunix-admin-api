from typing import Optional

from src.core.contracts.base_repository_contract import BaseRepositoryContract
from src.core.entities.teacher_course import TeacherCourse


class TeacherCoursesRepositoryContract(BaseRepositoryContract):

    async def get_teacher_courses_by_course_id(self, course_id: int) -> Optional[TeacherCourse]:
        pass
