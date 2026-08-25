"""API HTTP do CRUD de tarefas."""

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Request, Response, status

from app.repository import TaskRepository
from app.schemas import Task, TaskCreate, TaskSummary, TaskUpdate

app = FastAPI(
    title="BenchFlow CRUD",
    description="API mínima para demonstrar GitFlow, testes e integração contínua.",
    version="0.1.0",
)
app.state.task_repository = TaskRepository()


def get_repository(request: Request) -> TaskRepository:
    return request.app.state.task_repository


Repository = Annotated[TaskRepository, Depends(get_repository)]


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["tasks"])
def create_task(data: TaskCreate, repository: Repository) -> Task:
    return repository.create(data)


@app.get("/tasks", response_model=list[Task], tags=["tasks"])
def list_tasks(repository: Repository) -> list[Task]:
    return repository.list()


@app.get("/tasks/summary", response_model=TaskSummary, tags=["tasks"])
def summarize_tasks(repository: Repository) -> TaskSummary:
    return repository.summary()


@app.get("/tasks/{task_id}", response_model=Task, tags=["tasks"])
def get_task(task_id: int, repository: Repository) -> Task:
    task = repository.get(task_id)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")
    return task


@app.put("/tasks/{task_id}", response_model=Task, tags=["tasks"])
def update_task(task_id: int, data: TaskUpdate, repository: Repository) -> Task:
    task = repository.update(task_id, data)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")
    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["tasks"])
def delete_task(task_id: int, repository: Repository) -> Response:
    if not repository.delete(task_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
