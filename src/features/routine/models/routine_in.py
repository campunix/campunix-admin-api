from pydantic import BaseModel, Field


class RoutineIn(BaseModel):
    department_id: int = Field(1, gt=0)
    total_slots: int = Field(1, gt=0, le=20)


class SavedRoutineIn(BaseModel):
    syllabus_id: int
    title: str = None
    description: str = None
    calendar_year: str = None
    is_active: bool = False
    routine: str