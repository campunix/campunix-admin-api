from typing import Any, Optional

from sqlalchemy import text
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.contracts.syllabus_repository_contract import SyllabusRepositoryContract
from src.core.entities.syllabus.syllabus import Syllabus
from src.models.syllabus.syllabus_models import Course, SyllabusOut


class SyllabusRepository(SyllabusRepositoryContract):
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def getByDeptID(self, department_id: int) -> Optional[SyllabusOut]:
        statement = select(Syllabus).where(Syllabus.department_id == department_id)
        result = await self.db_session.exec(statement)
        syllabusOut = result.one_or_none()
        return syllabusOut

    async def getByDeptIDAndCourseCode(self, department_id: int, course_code: str) -> Optional[SyllabusOut]:
        statement = text("""
                        SELECT jsonb_build_object(
                            'departmentID', syllabus->'departmentID',
                            'semester', syllabus->'semester',
                            'departmentCode', syllabus->'departmentCode',
                            'departmentName', syllabus->'departmentName',
                            'course', course
                        ) AS merged_data
                        FROM syllabuses, jsonb_array_elements(syllabus->'courses') AS course
                        WHERE syllabuses.department_id = :department_id AND course->>'course_code' = :course_code
                """)

        result = await self.db_session.exec(statement,
                                            params={'department_id': department_id, 'course_code': course_code})
        syllabusOut = result.scalars().one_or_none()
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

    async def updateSyllabus(self, department_id: int, course_code: str, course_type: str) -> SyllabusOut:
        statement = text("""
                            UPDATE syllabuses
                                SET syllabus = jsonb_set(
                                    syllabus, '{courses}', (SELECT jsonb_agg(
                                        CASE
                                            WHEN course->>'course_code' = (:course_code)::text THEN
                                                course || jsonb_build_object('type', (:type)::text)
                                            ELSE
                                                course
                                        END
                                    ) FROM jsonb_array_elements(syllabus->'courses') AS course)
                                )
                            WHERE department_id = :department_id
                            AND syllabus->'courses' @> jsonb_build_array(jsonb_build_object('course_code', (:course_code)::text))
                        """)

        await self.db_session.exec(statement,
                             params={
                                 'department_id': department_id,
                                 'course_code': course_code,
                                 'type': course_type
                             })

        statement = text("""
                                SELECT jsonb_build_object(
                                    'departmentID', syllabus->'departmentID',
                                    'semester', syllabus->'semester',
                                    'departmentCode', syllabus->'departmentCode',
                                    'departmentName', syllabus->'departmentName',
                                    'course', course
                                ) AS merged_data
                                FROM syllabuses, jsonb_array_elements(syllabus->'courses') AS course
                                WHERE syllabuses.department_id = :department_id AND course->>'course_code' = :course_code
                        """)

        result = await self.db_session.exec(statement,
                                            params={
                                                'department_id': department_id,
                                                'course_code': course_code
                                            })
        syllabusOut = result.scalars().one_or_none()
        return syllabusOut
