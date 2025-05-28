from typing import List

from pydantic import BaseModel

from src.models.department import DepartmentOut


class CoursesTeacherOut(BaseModel):
    id: int
    full_name: str
    email: str
    designation: str
    status: str
    department: DepartmentOut = None
    relation_id: int = None


class CoursesTeachers(BaseModel):
    course_id: int
    title: str
    code: str
    teachers: List[int]
    department_id: int
