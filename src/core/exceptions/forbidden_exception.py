from typing import Any, Dict, Optional

from fastapi import HTTPException, status

class ForbiddenException(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_403_FORBIDDEN, detail, headers)
