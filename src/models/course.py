from pydantic import BaseModel


class CourseOut(BaseModel):
    id: int
    title: str
    code: str
    course_type: str


class CourseIn(BaseModel):
    title: str
    code: str
    department_id: int
    course_type: str
