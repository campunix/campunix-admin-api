from typing import Optional

from pydantic import BaseModel, Field

from src.models.department import DepartmentOut


class TeacherOut(BaseModel):
    id: int
    full_name: str
    email: str
    designation: str
    status: str
    department: DepartmentOut = None


class TeacherIn(BaseModel):
    user_id: int
    designation: str
    status: str
    department_id: int
