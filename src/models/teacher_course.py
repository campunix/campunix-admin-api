from pydantic import BaseModel

from src.models.course import CourseOut
from src.models.teacher import TeacherOut


class TeacherCourseOut(BaseModel):
    id: int
    teacher: TeacherOut
    course: CourseOut


class TeacherCourseIn(BaseModel):
    teacher_id: int
    course_id: int
