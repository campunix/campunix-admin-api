from pydantic import BaseModel


class PreferenceOut(BaseModel):
    id: int
    teacher_id: int
    teacher_name: str
    day: str
    slot_no: int

class PreferenceIn(BaseModel):
    teacher_id: int
    day: str
    slot_no: int
