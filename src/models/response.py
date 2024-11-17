from typing import Any, Optional, List, Dict, Union

from fastapi import status as s
from pydantic import BaseModel

from src.models.common import CustomModel


class CommandResponse(CustomModel):
    success: bool
    message: str


class APIResponse(BaseModel):
    status: bool = True
    code: int = s.HTTP_200_OK
    message: Optional[str] = None
    data: Any = None
    errors: Optional[Any] = None
