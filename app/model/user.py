from sqlmodel import Field, Relationship
from model.base import BaseModel,AuditFieldsMixin
import uuid
from typing import Optional
from datetime import datetime, timezone

from model.task import Task


class User(BaseModel,AuditFieldsMixin, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4,primary_key=True, index=True, description="user id")
    username: str= Field(nullable=False, index=True, description="user name")
    hashed_password: str = Field(nullable=False, description="user password")
    tasks : Task | None= Relationship(back_populates="user")
