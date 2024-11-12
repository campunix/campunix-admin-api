from pydantic import BaseModel

class RoutineIn(BaseModel):
    total_slots: int
