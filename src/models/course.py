from typing import List

from pydantic import BaseModel

from src.models.course_teacher_map import CoursesTeacherOut


class CourseOut(BaseModel):
    id: int
    title: str
    code: str
    course_type: str
    course_teachers: List[CoursesTeacherOut] = []


class CourseIn(BaseModel):
    title: str
    code: str
    department_id: int
    course_type: str
