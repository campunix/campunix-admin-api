from typing import Optional

from pydantic import BaseModel


class PreferenceOut(BaseModel):
    id: int
    teacher_id: int
    teacher_name: str
    department_id: Optional[int] = None
    day: Optional[str] = None
    slot_no: Optional[int] = None

class PreferenceIn(BaseModel):
    teacher_id: int
    day: Optional[str] = None
    slot_no: Optional[int] = None
