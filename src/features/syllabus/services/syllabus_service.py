import xml.etree.ElementTree as ET

from fastapi import File
from fastapi import HTTPException

from src.core.contracts.syllabus_repository_contract import SyllabusRepositoryContract
from src.core.entities.syllabus.syllabus import Syllabus
from src.features.syllabus.services.syllabus_service_contract import SyllabusServiceContract
from src.features.syllabus.syllabus_utils.xml_utils import parse_syllabus
from src.models.syllabus.syllabus_models import Course


class SyllabusService(SyllabusServiceContract):
    def __init__(self, syllabus_repository: SyllabusRepositoryContract):
        self.repository = syllabus_repository

    async def save(self, file: File(...)) -> Syllabus:
        try:
            contents = await file.read()
            root = ET.fromstring(contents)
            syllabus = parse_syllabus(root)
            department_id = syllabus["departmentID"]

            return await self.repository.save(department_id=department_id, syllabus=syllabus)

        except ET.ParseError:
            raise HTTPException(status_code=400, detail="Invalid XML format.")

    async def get(self, course_code: str) -> Course:
        return await self.repository.get(course_code)
