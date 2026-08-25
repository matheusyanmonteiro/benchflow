"""Repositório em memória usado pelo exemplo."""

from app.schemas import Task, TaskCreate, TaskSummary, TaskUpdate


class TaskRepository:
    """Mantém tarefas em memória durante a execução da aplicação."""

    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def create(self, data: TaskCreate) -> Task:
        task = Task(id=self._next_id, **data.model_dump())
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def list(self) -> list[Task]:
        return list(self._tasks.values())

    def summary(self) -> TaskSummary:
        completed = sum(task.completed for task in self._tasks.values())
        total = len(self._tasks)
        return TaskSummary(total=total, pending=total - completed, completed=completed)

    def get(self, task_id: int) -> Task | None:
        return self._tasks.get(task_id)

    def update(self, task_id: int, data: TaskUpdate) -> Task | None:
        if task_id not in self._tasks:
            return None

        task = Task(id=task_id, **data.model_dump())
        self._tasks[task_id] = task
        return task

    def delete(self, task_id: int) -> bool:
        return self._tasks.pop(task_id, None) is not None

    def clear(self) -> None:
        """Remove os dados e reinicia a sequência; útil para isolar testes."""
        self._tasks.clear()
        self._next_id = 1
