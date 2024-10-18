import re
from datetime import datetime

from pydantic import EmailStr, Field, field_validator

from src.models.common import CustomModel

class CommandResponse(CustomModel):
    success: bool
    message: str