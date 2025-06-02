from enum import Enum


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    STAFF = "STAFF"
    TEACHER = "TEACHER"
    STUDENT = "STUDENT"

    @classmethod
    def from_str(cls, role_str: str):
        try:
            return cls[role_str]
        except KeyError:
            raise ValueError(f"Invalid role: {role_str}")
