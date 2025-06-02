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


class CreateResponse(APIResponse):
    message: Optional[str] = "Created successfully"
    code: int = s.HTTP_201_CREATED


class DeleteResponse(APIResponse):
    message: Optional[str] = "Deleted successfully"


class UpdateResponse(APIResponse):
    message: Optional[str] = "Updated successfully"


class ErrorResponse(APIResponse):
    code: int = s.HTTP_500_INTERNAL_SERVER_ERROR
    message: Optional[str] = "Something went wrong!"
