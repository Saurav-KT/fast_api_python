from datetime import datetime
from typing import Optional


class AuditFieldsMixin:
    created_by: str
    created_date: datetime
    updated_by: str | None= None
    updated_date: Optional[datetime] = None