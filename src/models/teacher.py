from pydantic import BaseModel, Field


class TeacherOut(BaseModel):
    # id: int
    id: int = Field(..., alias='teacherId')
    full_name: str
    email: str
    designation: str
    status: str


class TeacherIn(BaseModel):
    user_id: int
    designation: str
    status: str
    department_id: int
