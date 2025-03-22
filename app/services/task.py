from app.schema.task import TaskCreate, TaskCreateResponse, TaskUpdate, TaskUpdateResponse,TaskResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.model.task import Task
from pydantic import UUID4
from sqlmodel import select
from app.utils.exception import BusinessValidationError
from fastapi import status
from datetime import datetime, timezone
class TaskService:

    @staticmethod
    async def create_task(task_data: TaskCreate, session: AsyncSession) -> TaskCreateResponse:
        """ Business logic before saving to DB """

        # Business Pre-Processing
        # if task_data.due_date and task_data.due_date < date.today():
        #     raise ValueError("Due date cannot be in the past.")

        # Create an ORM object
        new_task = Task(**task_data.model_dump())

        # Save to DB
        session.add(new_task)
        await session.commit()
        await session.refresh(new_task)

        # Convert ORM to Response Schema
        return TaskCreateResponse.model_validate(new_task)

    @staticmethod
    async def delete_task(task_id: UUID4, session: AsyncSession)-> bool:
        result= await session.execute(select(Task).where(Task.id==task_id))
        task= result.scalar_one_or_none()
        if not task:
            raise BusinessValidationError(status_code=status.HTTP_404_NOT_FOUND,detail= f"Task with ID { task_id} does not exist")
        await session.delete(task)
        await session.commit()
        return True

    @staticmethod
    async def update_task(task_id: UUID4, task_data: TaskUpdate,session:AsyncSession):
        result= await session.execute(select(Task).where(Task.id==task_id))
        task= result.scalar_one_or_none()
        if not task:
            raise BusinessValidationError(status_code=status.HTTP_404_NOT_FOUND,detail= f"Task with ID { task_id} does not exist")
        data=task_data.model_dump(exclude_unset=True)
        task.sqlmodel_update(data)
        task.updated_date= datetime.now(timezone.utc).replace(tzinfo=None)
        # update to DB
        session.add(task)
        await session.commit()
        await session.refresh(task)
        # Convert ORM to Response Schema
        return TaskUpdateResponse.model_validate(task)

    @staticmethod
    async def get_task_by_id(task_id: UUID4, session: AsyncSession)->TaskResponse:
        result= await session.execute(select(Task).where(Task.id==task_id))
        task = result.scalars().first()
        if not task:
            raise BusinessValidationError(status_code=status.HTTP_404_NOT_FOUND,detail= f"Task with ID { task_id} does not exist")
        return TaskResponse.model_validate(task)










