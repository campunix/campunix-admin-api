from sqlalchemy.ext.asyncio import AsyncSession

from src.core.contracts.exam_routine_course_teachers_repository_contract import \
    ExamRoutineCourseTeachersRepositoryContract
from src.core.entities.exam_routine.exam_routine_course_teachers import ExamRoutineCourseTeacher
from src.infrastructure.repositories.base_repository import BaseRepository


class ExamRoutineCourseTeachersRepository(
    BaseRepository[ExamRoutineCourseTeacher], ExamRoutineCourseTeachersRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, ExamRoutineCourseTeacher)
