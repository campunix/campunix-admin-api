from typing import Optional


class RoutinePreference:
    id: int
    day: Optional[str] = None
    slot_no: Optional[int] = None

    def __init__(self, id: int, day: str, slot_no: int):
        self.id = id
        self.day = day
        self.slot_no = slot_no