from sqlalchemy import Enum

class TeacherDesignation(str, Enum):
    PROFESSOR = "PROFESSOR"
    ASSOCIATE_PROFESSOR = "ASSOCIATE_PROFESSOR"
    ASSISTANT_PROFESSOR = "ASSISTANT_PROFESSOR"
    LECTURER = "LECTURER"