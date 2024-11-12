from enum import Enum


class RoomType(str, Enum):
    LECTURE = "LECTURE"
    LAB = "LAB"
    LIBRARY = "LIBRARY"
    SEMINAR = "SEMINAR"
    COMMON = "COMMON"
    OFFICE = "OFFICE"
    DINING = "DINING"
    OTHERS = "OTHERS"

    @classmethod
    def from_str(cls, type_str: str):
        try:
            return cls[type_str]
        except KeyError:
            raise ValueError(f"Invalid type: {type_str}")