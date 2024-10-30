from sqlalchemy import Enum


class TeacherStatus(str, Enum):
    ACTIVE = "ACTIVE"
    LEAVE = "LEAVE"
    LPR = "LPR"
    PRL = "PRL"
    RETIRED = "RETIRED"