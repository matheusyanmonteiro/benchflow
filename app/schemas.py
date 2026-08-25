"""Contratos HTTP do CRUD de tarefas."""

from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    """Dados necessários para criar uma tarefa."""

    title: str = Field(min_length=1, max_length=120)
    description: str = Field(default="", max_length=500)


class TaskUpdate(BaseModel):
    """Dados aceitos na atualização completa de uma tarefa."""

    title: str = Field(min_length=1, max_length=120)
    description: str = Field(default="", max_length=500)
    completed: bool = False


class Task(TaskCreate):
    """Representação pública de uma tarefa."""

    model_config = ConfigDict(frozen=True)

    id: int
    completed: bool = False
