from pydantic import BaseModel, Field

class PreferenceOut(BaseModel):
    teacher_id: int
    day: int
    slot_no: int

class PreferenceIn(BaseModel):
    teacher_id: int
    day: int
    slot_no: int
