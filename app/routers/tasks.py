from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import defer

from app.model.task import Task
from app.schema.task import TaskCreate, TaskCreateResponse, TaskUpdate, TaskUpdateResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from uuid import UUID
from app.services.task import TaskService
from app.utils.response import success_response, SuccessResponse

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)


@router.post("", response_model=SuccessResponse[TaskCreateResponse])
async def create_task(task: TaskCreate, session: AsyncSession = Depends(get_db)):
    try:
        task = await TaskService.create_task(task, session)
        if task:
            return success_response("Task created successfully", data=task, status_code=status.HTTP_201_CREATED)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{task_id}", response_model=SuccessResponse)
async def delete_task(task_id: UUID, session: AsyncSession = Depends(get_db)):
    try:
        task = await TaskService.delete_task(task_id, session)
        if task:
            return success_response("Task deleted successfully", status_code=status.HTTP_200_OK)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{task_id}", response_model= SuccessResponse[TaskUpdateResponse])
async def update_task(task_id: UUID, task: TaskUpdate,session: AsyncSession= Depends(get_db)):
    try:
        task= await TaskService.update_task(task_id=task_id,task_data=task,session= session)
        if task:
            return success_response("Task updated successfully", data=task, status_code=status.HTTP_200_OK)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
