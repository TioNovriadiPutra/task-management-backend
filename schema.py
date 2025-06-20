from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str
    status: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdateStatus(BaseModel):
    status: bool

class Task(TaskBase):
    id: int