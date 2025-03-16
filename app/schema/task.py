
from app.schema.auditfieldmixin import AuditFieldsMixin
from datetime import datetime
import uuid
from typing import Optional
from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    due_date: Optional[datetime] = None
    status: str

class TaskCreateResponse(TaskCreate):
    id: uuid.UUID
    class Config:
        from_attributes = True


class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    due_date: Optional[datetime] = None
    status: str
    updated_by: str

class TaskUpdateResponse(TaskUpdate):
    id: uuid.UUID
    class Config:
        from_attributes = True

