from typing import Any, Optional, List

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.core.contracts.syllabus_repository_contract import SyllabusRepositoryContract
from src.core.entities.syllabus.syllabus import Syllabus
from src.models.syllabus.syllabus_models import SyllabusParsed


class SyllabusRepository(SyllabusRepositoryContract):
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_by_department(self, department_id: int) -> Optional[SyllabusParsed]:
        statement = select(Syllabus).where(Syllabus.department_id == department_id)
        result = await self.db_session.execute(statement)
        syllabus = result.scalars().one_or_none().syllabus
        return SyllabusParsed(**syllabus)

    async def getByDeptIDAndSemesterCode(self, department_id: int, semester_code: int) -> Optional[SyllabusParsed]:
        statement = text("""
                        SELECT jsonb_build_object(
                            'DepartmentID', syllabus->'DepartmentID',
	                        'DepartmentCode', syllabus->'DepartmentCode',
	                        'DepartmentName', syllabus->'DepartmentName',
	                        'Semesters', semesters
                        ) AS merged_data
                        FROM syllabuses, jsonb_array_elements(syllabus->'Semesters') AS semesters
                        WHERE syllabuses.department_id = :department_id AND semesters->>'SemesterCode' = :SemesterCode
                """)

        result = await self.db_session.exec(statement,
                                            params={'department_id': department_id, 'SemesterCode': str(semester_code)})
        syllabusOut = result.scalars().one_or_none()
        return syllabusOut

    async def save(self, department_id: int, syllabus: SyllabusParsed) -> SyllabusParsed:
        syllabus_dict = Syllabus(
            department_id=department_id,
            syllabus=syllabus.model_dump()
        )

        self.db_session.add(syllabus_dict)
        await self.db_session.commit()
        await self.db_session.refresh(syllabus_dict)
        return syllabus

    async def updateSyllabus(self, department_id: int, semester_code: int, course_code: str,
                             course_type: str) -> SyllabusParsed:
        statement = text("""
                            UPDATE syllabuses SET syllabus = jsonb_set(syllabus, '{Semesters}', 
                                (SELECT jsonb_agg(jsonb_set(semester, '{Courses}', (SELECT jsonb_agg(
                                    CASE 
                                        WHEN course->>'CourseCode' = :CourseCode THEN 
                                             course || jsonb_build_object('Type', (:Type)::text)
                                        ELSE 
                                             course
                                        END
                                    ) 
                                    FROM jsonb_array_elements(semester->'Courses') AS course)
                                    )
                                )
                                FROM jsonb_array_elements(syllabus->'Semesters') AS semester
                                WHERE semester->>'SemesterCode' = (:SemesterCode)::text
                                )
                            )
                            WHERE department_id = :department_id
                            AND syllabus->'Semesters' @> jsonb_build_array(
                            jsonb_build_object('SemesterCode', (:SemesterCode)::text))
                        """)

        await self.db_session.exec(statement, params={
            'Type': course_type,
            'CourseCode': course_code,
            'SemesterCode': str(semester_code),
            'department_id': department_id,
        })

        return await self.getByDeptIDAndSemesterCode(department_id, semester_code)

    async def getSemesters(self, department_id: int) -> Optional[List[Any]]:
        statement = select(Syllabus).where(Syllabus.department_id == department_id)
        result = await self.db_session.exec(statement)
        semesters = result.one_or_none()
        return semesters

    async def getCourses(self, department_id: int) -> Optional[List[Any]]:
        statement = select(Syllabus).where(Syllabus.department_id == department_id)
        result = await self.db_session.exec(statement)
        courses = result.one_or_none()
        return courses
