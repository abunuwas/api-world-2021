# generated by datamodel-codegen:
#   filename:  oas.yaml
#   timestamp: 2021-09-17T18:00:25+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


class Error(BaseModel):
    detail: Optional[str] = None


class Priority(Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'


class Status(Enum):
    pending = 'pending'
    progress = 'progress'
    completed = 'completed'


class CreateTaskSchema(BaseModel):
    priority: Optional[Priority] = 'low'
    status: Optional[Status] = 'pending'
    task: str


class GetTaskSchema(BaseModel):
    id: UUID
    created: datetime
    priority: Priority
    status: Status
    task: str


class ListTasksSchema(BaseModel):
    tasks: List[GetTaskSchema]
