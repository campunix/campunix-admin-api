import json
from typing import Any

from sqlmodel.ext.asyncio.session import AsyncSession

from src.core.contracts.syllabus_repository_contract import SyllabusRepositoryContract
from src.core.entities.syllabus.syllabus import Syllabus
from src.models.syllabus.syllabus_models import Course, RecommendedBooks, Book, HardwareSoftwareRequirements, \
    CourseDescription, Module, LearningOutcomes, CourseObjectives


class SyllabusRepository(SyllabusRepositoryContract):
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get(self, courseCode: str) -> Course:
        return Course(
            CourseCode="CSE 105",
            Title="Structured Programming",
            Credit=3.0,
            Prerequisite="None",
            Type="Theory",
            ContactHours=39,
            Rationale=(
                "This course is designed to introduce students to the algorithms' "
                "way of thinking and problem solving by computers."
            ),
            CourseObjectives=CourseObjectives(
                Objectives=[
                    "Make students familiar with basic software design principles...",
                ]
            ),
            StudentLearningOutcomes=LearningOutcomes(
                Outcomes=[
                    "After successful completion of this course, students should...",
                ]
            ),
            CourseDescription=CourseDescription(
                Modules=[
                    Module(
                        Module="Structured Programming Language fundamentals",
                        Content="C, Keywords, History and Features..."
                    ),
                    Module(
                        Module="Basic Input/Output",
                        Content="Formatted and Unformatted, Basic Types..."
                    ),
                ]
            ),
            RecommendedBooks=RecommendedBooks(
                Books=[
                    Book(
                        Title="Teach Yourself C",
                        Author="Herbert Schildt",
                        Publisher="McGraw-Hill",
                        Year=1997
                    )
                ]
            ),
            HardwareSoftwareRequirements=HardwareSoftwareRequirements(
                HW="Core i5, 2.4 GHz, 4 GB RAM, 500 MB disk space",
                SW="Code::Blocks, GCC Compiler, Dev C++"
            )
        )

    async def save(self, department_id: int, syllabus: dict[str, Any]) -> Syllabus:
        new_syllabus = Syllabus(
            department_id=department_id,
            syllabus=syllabus
        )
        self.db_session.add(new_syllabus)
        await self.db_session.commit()
        await self.db_session.refresh(new_syllabus)
        return new_syllabus
