from typing import Optional

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from src.features.admin.admin_container import AdminContainer
from src.features.admin.services.room_service_contract import RoomServiceContract
from src.models.course import CourseOut
from src.models.course_teacher_map import CoursesTeacherOut
from src.models.department import DepartmentOut
from src.models.response import APIResponse, CreateResponse
from src.models.room import RoomOut
from src.models.semester import SemesterOut
from src.models.teacher import TeacherOut
from datetime import date

router = APIRouter(prefix="/exam-routine")


@router.post("")
@inject
async def create_exam_routine():
    return CreateResponse(data="Ok")


@router.get("")
@inject
async def get_all(
        room_service: RoomServiceContract = Depends(Provide[AdminContainer.room_service]),
        page: int = 1,
        page_size: int = 20,
        search_query: Optional[str] = None,
        department_id: Optional[int] = None,
        paginate: bool = True
):
    exam_routine = ExamRoutine(
        id=1,
        date="2025-01-10",
        department=DepartmentOut(id=1, name="Computer Science", code="CSE"),
        semester=SemesterOut(id=2, year=2025, number=2, disabled=False),
        room=RoomOut(id=101, name="Lab-1", code="L101", room_type="Lab"),
        courses=[
            CourseOut(
                id=1,
                title="Data Structures",
                code="CSE201",
                course_type="Theory",
                course_teachers=[
                    CoursesTeacherOut(
                        id=1,
                        full_name="Dr. John Doe",
                        email="john.doe@example.com",
                        designation="Professor",
                        status="Active",
                        department=DepartmentOut(id=1, name="Computer Science", code="CSE"),
                    )
                ]
            )
        ],
        teachers=[
            TeacherOut(
                id=2,
                full_name="Dr. Jane Smith",
                email="jane.smith@example.com",
                designation="Associate Professor",
                status="Active",
                department=DepartmentOut(id=1, name="Computer Science", code="CSE"),
                courses=[]
            )
        ],
        description="Final exam schedule"
    )

    return APIResponse(data=exam_routine)

class ExamRoutine(BaseModel):
    id: int
    date: date
    department: DepartmentOut
    semester: SemesterOut
    room: RoomOut
    courses: list[CourseOut]
    teachers: list[TeacherOut]
    description: str
