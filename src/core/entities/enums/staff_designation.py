from sqlalchemy import Enum

class StaffDesignation(str, Enum):
    OFFICER = "OFFICER"
    ASSISTANT_OFFICER = "ASSISTANT_OFFICER"
    ACCOUNTANT = "ACCOUNTANT"
    LIBRARIAN = "LIBRARIAN"