from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Field
from app.model.base import BaseModel, AuditFieldsMixin, commit_and_refresh
import uuid
from datetime import datetime, timezone

class Task(BaseModel,AuditFieldsMixin, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4,primary_key=True, description="Task's ID")
    title: str= Field(nullable=False, index=True, description="task name")
    description: str | None = Field(default=None, description="task description")
    status: str = Field (nullable=False, default="pending", description="task description")
    due_date: datetime | None = Field(nullable=True, default=None, description="task due date")
    is_cancelled: bool | None= Field(nullable=True, default=False, description="If task is cancelled")

    @classmethod
    async def create(cls, session: AsyncSession, **kwargs):
        task = cls(**kwargs)
        session.add(task)
        await session.commit()
        await session.refresh(task)
        return task
        # task=await commit_and_refresh(session,task)
        # return task