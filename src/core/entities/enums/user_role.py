from sqlalchemy import Enum


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    STAFF = "STAFF"
    TEACHER = "TEACHER"
    STUDENT = "STUDENT"