from pydantic import BaseModel


class TeacherOut(BaseModel):
    id: int
    designation: str
    status: str


class TeacherIn(BaseModel):
    user_id: int
    designation: str
    status: str
    department_id: int
