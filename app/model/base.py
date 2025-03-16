from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Field
from sqlmodel import MetaData, SQLModel


class BaseModel(SQLModel):
    metadata = MetaData(schema="task_management")
    SQLModel.metadata = metadata


class AuditFieldsMixin(SQLModel):
    created_by: str = Field(nullable=False, default="system", description="User who created the record")
    created_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc).date(), description="record created date")  # UTC date
    updated_by: str | None = Field(nullable=True, description="User who last updated the record")
    updated_date: datetime | None = Field(nullable= True, description="record updated date")


async def commit_and_refresh(session: AsyncSession, instance=None):
        """
        Commit the transaction and optionally refresh the instance.

        :param session: The AsyncSession instance.
        :param instance: Optional instance to refresh after commit.
        """
        await session.commit()
        if instance is not None:
            await session.refresh(instance)
            return instance