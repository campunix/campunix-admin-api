from sqlalchemy.ext.asyncio import AsyncSession

from src.core.contracts.teacher_courses_repository_contract import TeacherCoursesRepositoryContract
from src.core.entities.teacher_course import TeacherCourse
from src.infrastructure.repositories.base_repository import BaseRepository


class TeacherCoursesRepository(
    BaseRepository[TeacherCourse], TeacherCoursesRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, TeacherCourse)
