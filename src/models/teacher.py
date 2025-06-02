from typing import List

from pydantic import BaseModel

from src.models.department import DepartmentOut
from src.models.teacher_course_map import TeachersCourseOut


class TeacherOut(BaseModel):
    id: int
    full_name: str
    email: str
    designation: str
    status: str
    department: DepartmentOut = None
    courses: List[TeachersCourseOut] = []


class TeacherIn(BaseModel):
    user_id: int
    designation: str
    status: str
    department_id: int



