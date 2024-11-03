from enum import Enum


class TeacherDesignation(str, Enum):
    PROFESSOR = "PROFESSOR"
    ASSOCIATE_PROFESSOR = "ASSOCIATE_PROFESSOR"
    ASSISTANT_PROFESSOR = "ASSISTANT_PROFESSOR"
    LECTURER = "LECTURER"

    @classmethod
    def from_str(cls, str_val: str):
        try:
            return cls[str_val]
        except KeyError:
            raise ValueError(f"Invalid: {str_val}")