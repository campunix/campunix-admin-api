import xml.etree.ElementTree as ET
from typing import Optional, Any

from fastapi import File
from fastapi import HTTPException

from src.core.contracts.syllabus_repository_contract import SyllabusRepositoryContract
from src.features.syllabus.services.syllabus_service_contract import SyllabusServiceContract
from src.features.syllabus.syllabus_utils.xml_utils import parse_syllabus, create_template
from src.models.syllabus.syllabus_models import SyllabusParsed


class SyllabusService(SyllabusServiceContract):
    def __init__(self, syllabus_repository: SyllabusRepositoryContract):
        self.repository = syllabus_repository

    async def save(self, file: File(...)) -> SyllabusParsed:
        try:
            contents = await file.read()
            root = ET.fromstring(contents)
            syllabus = parse_syllabus(root)

            return await self.repository.save(syllabus=syllabus)

        except ET.ParseError:
            raise HTTPException(status_code=400, detail="Invalid XML format.")

    async def getByDepartmentID(self, department_id) -> Optional[SyllabusParsed]:
        return await self.repository.getByDeptID(department_id)

    async def getByDeptIDAndSemesterCode(self, department_id: int, semester_code: int) -> Optional[SyllabusParsed]:
        return await self.repository.getByDeptIDAndSemesterCode(department_id, semester_code)

    async def updateSyllabus(self, department_id: int, semester_code: int, course_code: str, course_type: str) -> \
    Optional[SyllabusParsed]:
        return await self.repository.updateSyllabus(department_id, semester_code, course_code, course_type)

    async def template(self, department_id: int) -> Optional[Any]:
        semesters = await self.repository.getSemesters(department_id)
        courses = await self.repository.getCourses(department_id)
        template = create_template(department_id, semesters, courses)
        return template
