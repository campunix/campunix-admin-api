from sqlalchemy import Enum

class StaffStatus(str, Enum):
    ACTIVE = "ACTIVE"
    LEAVE = "LEAVE"
    LPR = "LPR"
    PRL = "PRL"
    RETIRED = "RETIRED"