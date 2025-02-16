from sqlalchemy.ext.asyncio import AsyncSession

from src.core.contracts.exam_routine_courses_repository_contract import ExamRoutineCoursesRepositoryContract
from src.core.entities.exam_routine.exam_routine_courses import ExamRoutineCourse
from src.infrastructure.repositories.base_repository import BaseRepository


class ExamRoutineCoursesRepository(
    BaseRepository[ExamRoutineCourse], ExamRoutineCoursesRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, ExamRoutineCourse)