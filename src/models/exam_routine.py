from pydantic import BaseModel


class ExamRoutineIn(BaseModel):
    syllabus_id: int
    title: str = None
    description: str = None
    calendar_year: str = None
    is_active: bool = False
    exam_routine: str


class ExamRoutineOut(BaseModel):
    id: int
    syllabus_id: int
    title: str = None
    description: str = None
    calendar_year: str = None
    is_active: bool = False
    exam_routine: dict
