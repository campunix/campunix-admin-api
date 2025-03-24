from pydantic import BaseModel

from src.models.department import DepartmentOut


class CoursesTeacherOut(BaseModel):
    id: int
    full_name: str
    email: str
    designation: str
    status: str
    department: DepartmentOut = None
