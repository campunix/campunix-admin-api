from pydantic import BaseModel


class RoutineSemester:
    id: int
    year: int
    number: int
    serial_number: int
    
    def __init__(self, id: int, year: int, number: int):
        self.id = id
        self.year = year
        self.number = number