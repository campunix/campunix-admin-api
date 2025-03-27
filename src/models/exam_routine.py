from pydantic import BaseModel


class ExamRoutineIn(BaseModel):
    routine_id: int
    title: str = None
    description: str = None
    calendar_year: str = None
    is_active: bool = False
    exam_routine: str


class ExamRoutineOut(BaseModel):
    id: int
    routine_id: int
    title: str = None
    description: str = None
    calendar_year: str = None
    is_active: bool = False
    exam_routine: dict
