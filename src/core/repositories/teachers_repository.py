from typing import Dict, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.core.contracts.teachers_repository_contract import TeachersRepositoryContract
from src.core.entities.enums.teacher_designation import TeacherDesignation
from src.core.entities.enums.teacher_status import TeacherStatus
from src.core.entities.teacher import Teacher
from src.infrastructure.repositories.base_repository import BaseRepository


class TeachersRepository(
    BaseRepository[Teacher], TeachersRepositoryContract
):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Teacher)

    async def get_teacher_designation(self) -> Dict[str, Any]:
        return {"items": [designation.value for designation in TeacherDesignation]}

    async def get_teacher_status(self) -> Dict[str, Any]:
        return {"items": [status.value for status in TeacherStatus]}

    async def is_teacher(self, user_id: int) -> bool:
        statement = select(Teacher).where(Teacher.user_id == user_id)
        result = await self.db_session.execute(statement)
        teacher = result.scalars().one_or_none()
        return bool(teacher)
