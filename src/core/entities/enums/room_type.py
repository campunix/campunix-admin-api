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