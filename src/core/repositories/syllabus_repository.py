from typing import Any

import sqlalchemy as sa
from sqlalchemy import text

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.contracts.syllabus_repository_contract import SyllabusRepositoryContract
from src.core.entities.syllabus.syllabus import Syllabus, SyllabusBase
from src.models.syllabus.syllabus_models import SyllabusOut
from sqlalchemy import cast, String


class SyllabusRepository(SyllabusRepositoryContract):
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def getByDeptID(self, department_id: int) -> SyllabusOut:
        statement = select(Syllabus).where(Syllabus.department_id == department_id)
        result = await self.db_session.exec(statement)
        syllabusOut = result.one_or_none()
        return syllabusOut

    async def getByDeptIDAndCourseCode(self, department_id: int, course_code: str) -> SyllabusOut:
        statement = select(Syllabus).where(Syllabus.department_id == department_id)

        if course_code:
            statement = statement.where(Syllabus.syllabus["course_code"] == course_code)

        result = await self.db_session.exec(statement)
        syllabusOut = result.one_or_none()
        return syllabusOut

    async def save(self, department_id: int, syllabus: dict[str, Any]) -> Syllabus:
        new_syllabus = Syllabus(
            department_id=department_id,
            syllabus=syllabus
        )
        self.db_session.add(new_syllabus)
        await self.db_session.commit()
        await self.db_session.refresh(new_syllabus)
        return new_syllabus
    
    async def getSyllabusByJsonFilter(self):
        stmt = select(Syllabus).where(cast(Syllabus.syllabus['semester'], String) == '2')
        result = await self.db_session.exec(stmt)
        print(result.fetchall())
