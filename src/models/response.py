from typing import Any, Optional, List, Dict, Union

from pydantic import BaseModel

from src.models.common import CustomModel


class CommandResponse(CustomModel):
    success: bool
    message: str


class APIResponse(BaseModel):
    status: bool
    code: int
    message: Optional[str] = None
    data: Any = None
    errors: Optional[Any] = None
