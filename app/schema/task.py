from datetime import datetime
from typing import Optional
from pydantic import BaseModel, UUID4,Field
from datetime import datetime, timezone
from app.utils.base_enum import TaskStatus

class BaseConfig:
    from_attributes = True

class AuditFieldBase(BaseModel):
    created_by: str
    created_date: datetime =Field(default_factory=lambda: datetime.now(timezone.utc).date()) # UTC date
    updated_by: Optional[str] = Field(default=None)
    updated_date: Optional[datetime] = Field(default=None)




class TaskBase(BaseModel):
    title: str
    description: Optional[str] = Field(None, max_length=500)
    due_date: Optional[datetime] = None
    status: TaskStatus

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskBase,AuditFieldBase):
    id: UUID4
    class Config(BaseConfig):
        pass


class TaskUpdate(TaskBase):
    updated_by: str

class TaskUpdateResponse(TaskUpdate,AuditFieldBase):
    id: UUID4

    class Config(BaseConfig):
        pass

class TaskResponse(TaskBase,AuditFieldBase):
    id: UUID4
    class Config(BaseConfig):
        pass


