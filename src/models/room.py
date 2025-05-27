from pydantic import BaseModel


class RoomOut(BaseModel):
    id: int
    name: str
    code: str
    room_type: str
    department_id: int = None


class RoomIn(BaseModel):
    name: str
    code: str
    department_id: int
    room_type: str