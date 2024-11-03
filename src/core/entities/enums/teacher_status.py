from enum import Enum


class TeacherStatus(str, Enum):
    ACTIVE = "ACTIVE"
    LEAVE = "LEAVE"
    LPR = "LPR"
    PRL = "PRL"
    RETIRED = "RETIRED"

    @classmethod
    def from_str(cls, str_val: str):
        try:
            return cls[str_val]
        except KeyError:
            raise ValueError(f"Invalid: {str_val}")