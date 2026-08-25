from fastapi.testclient import TestClient


def create_task(client: TestClient, title: str = "Preparar benchmark") -> dict:
    response = client.post(
        "/tasks",
        json={"title": title, "description": "Demonstrar o fluxo de contribuição"},
    )
    assert response.status_code == 201
    return response.json()


def test_health_check(client: TestClient) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_list_tasks(client: TestClient) -> None:
    task = create_task(client)

    assert task == {
        "id": 1,
        "title": "Preparar benchmark",
        "description": "Demonstrar o fluxo de contribuição",
        "completed": False,
    }
    assert client.get("/tasks").json() == [task]


def test_get_task(client: TestClient) -> None:
    task = create_task(client)

    response = client.get(f"/tasks/{task['id']}")

    assert response.status_code == 200
    assert response.json() == task


def test_get_unknown_task_returns_not_found(client: TestClient) -> None:
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Tarefa não encontrada"}


def test_update_task(client: TestClient) -> None:
    task = create_task(client)

    response = client.put(
        f"/tasks/{task['id']}",
        json={
            "title": "Apresentar benchmark",
            "description": "Fluxo revisado",
            "completed": True,
        },
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Apresentar benchmark"
    assert response.json()["completed"] is True


def test_update_unknown_task_returns_not_found(client: TestClient) -> None:
    response = client.put(
        "/tasks/999",
        json={"title": "Tarefa inexistente", "completed": False},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Tarefa não encontrada"}


def test_delete_task(client: TestClient) -> None:
    task = create_task(client)

    response = client.delete(f"/tasks/{task['id']}")

    assert response.status_code == 204
    assert client.get(f"/tasks/{task['id']}").status_code == 404


def test_delete_unknown_task_returns_not_found(client: TestClient) -> None:
    response = client.delete("/tasks/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Tarefa não encontrada"}


def test_rejects_invalid_task(client: TestClient) -> None:
    response = client.post("/tasks", json={"title": ""})

    assert response.status_code == 422
