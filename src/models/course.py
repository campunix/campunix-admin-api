from pydantic import BaseModel


class CourseOut(BaseModel):
    id: int
    name: str
    course_type: str


class CourseIn(BaseModel):
    name: str
    department_id: int
    course_type: str
