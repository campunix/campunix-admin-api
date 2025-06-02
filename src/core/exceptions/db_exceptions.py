from typing import Any, Dict, Optional

from fastapi import status


class DatabaseIntegrityError(Exception):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_409_CONFLICT, detail, headers)


class DatabaseError(Exception):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_500_INTERNAL_SERVER_ERROR, detail, headers)
