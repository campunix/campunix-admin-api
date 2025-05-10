from pydantic import BaseModel

from src.models.department import DepartmentOut


class TeachersCourseOut(BaseModel):
    id: int
    title: str
    code: str
    course_type: str
    department: DepartmentOut = None
    relation_id: int = None
