from typing import List

from pydantic import BaseModel

from src.models.course import CourseOut
from src.models.department import DepartmentOut


class TeachersCourseIn(BaseModel):
    teacher_ids: List[int]
    course_id: int


class TeachersCourseMappingOut(BaseModel):
    id: int
    course: CourseOut


class TeachersCourseOut(BaseModel):
    id: int
    title: str
    code: str
    course_type: str
    department: DepartmentOut = None
    relation_id: int = None
