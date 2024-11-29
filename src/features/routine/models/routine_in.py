from pydantic import BaseModel, Field

class RoutineIn(BaseModel):
    total_slots: int = Field(1, gt=0, le=20)
