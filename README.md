# BenchFlow

Benchmark didático de GitFlow com um CRUD Python, testes automatizados, cobertura mínima, templates de colaboração e proteção da branch principal.

## O que este repositório demonstra

- três formulários de issue: **bug**, **feature** e **pedido**;
- três exemplos preenchidos de issues e três de pull requests;
- API CRUD de tarefas com FastAPI;
- testes automatizados com `pytest` e cobertura mínima de 95%;
- lint com Ruff;
- GitHub Actions executado em todo PR para `main` ou `develop`;
- `main` protegida por PR, aprovação de outro colaborador, conversas resolvidas e check `quality` aprovado;
- dependências monitoradas pelo Dependabot e ownership via CODEOWNERS.

## Executar o projeto

Requisitos: Python 3.11+ e [uv](https://docs.astral.sh/uv/).

```bash
uv sync --dev
uv run uvicorn app.main:app --reload
```

A API fica em `http://127.0.0.1:8000` e a documentação interativa em `http://127.0.0.1:8000/docs`.

Exemplo de uso:

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H 'Content-Type: application/json' \
  -d '{"title":"Apresentar GitFlow","description":"Executar o benchmark"}'

curl http://127.0.0.1:8000/tasks
```

Endpoints disponíveis:

| Método | Rota | Ação |
| --- | --- | --- |
| `GET` | `/health` | Verifica a saúde da API |
| `POST` | `/tasks` | Cria uma tarefa |
| `GET` | `/tasks` | Lista as tarefas |
| `GET` | `/tasks/{id}` | Consulta uma tarefa |
| `PUT` | `/tasks/{id}` | Atualiza uma tarefa |
| `DELETE` | `/tasks/{id}` | Exclui uma tarefa |

## Testes e cobertura

```bash
uv run ruff check .
uv run pytest
```

O `pytest-cov` mostra as linhas não cobertas, gera `coverage.xml` e interrompe a execução abaixo de 95%. Na CI, esse relatório também fica disponível como artifact.

## Fluxo demonstrado

```mermaid
flowchart LR
    I[Issue triada] --> B[Branch curta]
    B --> C[Commits convencionais]
    C --> P[Pull request]
    P --> Q{CI quality}
    Q -->|falha| C
    Q -->|passa| R[Revisão e aprovação]
    R --> M[Squash merge]
    M --> X[main protegida]
```

O fluxo completo, as convenções de branch e a política de revisão estão em [CONTRIBUTING.md](CONTRIBUTING.md). Os exemplos para apresentação estão em [`docs/exemplos`](docs/exemplos).

## Roteiro rápido para a apresentação

1. Mostre os três botões de abertura de issue e abra o exemplo de feature.
2. Crie `feature/2-filtrar-tarefas` a partir da branch adotada pela equipe.
3. Faça uma alteração propositalmente sem teste e mostre a CI barrando o PR.
4. Adicione o teste, envie o novo commit e mostre o check `quality` aprovado.
5. Mostre que a `main` não aceita push direto e ainda exige revisão/conversas resolvidas.
6. Faça squash merge e demonstre a ligação automática `Closes #2` entre PR e issue.

> A proteção é aplicada no GitHub, não apenas por um arquivo versionado. A configuração reproduzível está em [`.github/branch-protection.json`](.github/branch-protection.json).
