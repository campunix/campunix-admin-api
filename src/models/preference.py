from pydantic import BaseModel, Field

class PreferenceOut(BaseModel):
    teacher_id: int
    day: str
    slot_no: int

class PreferenceIn(BaseModel):
    teacher_id: int
    day: str
    slot_no: int
