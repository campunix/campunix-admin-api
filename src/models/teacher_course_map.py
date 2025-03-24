from pydantic import BaseModel


class TeachersCourseOut(BaseModel):
    id: int
    title: str
    code: str
    course_type: str
