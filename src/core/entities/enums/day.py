from enum import Enum

class Day(int, Enum):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7

    @classmethod
    def from_str(cls, type_str: str):
        try:
            return cls[type_str.upper()]
        except KeyError:
            raise ValueError(f"Invalid day type: {type_str}")

    @classmethod
    def to_str(cls, day: 'Day'):
        day_enum = cls(day)
        return day_enum.name
