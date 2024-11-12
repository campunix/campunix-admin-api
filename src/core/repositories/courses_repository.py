from sqlalchemy.ext.asyncio import AsyncSession

from src.core.contracts.courses_repository_contract import CoursesRepositoryContract
from src.core.entities.course import Course
from src.infrastructure.repositories.base_repository import BaseRepository


class CoursesRepository(
    BaseRepository[Course], CoursesRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Course)
