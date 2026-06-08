from typing import Any
from pydantic import BaseModel

class AuditRecord(BaseModel):
    event_type: str
    payload: dict[str, Any]