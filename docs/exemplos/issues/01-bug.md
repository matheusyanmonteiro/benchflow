# [Bug]: DELETE de tarefa inexistente retorna 204

**Labels:** `bug`, `triage`
**Severidade:** Média — afeta o uso, mas não bloqueia

## Descrição do problema

Ao excluir uma tarefa que não existe, a API retorna `204 No Content`. Isso faz o cliente assumir que um recurso foi removido, embora nenhum registro tenha sido encontrado.

## Passos para reproduzir

1. Inicie a API com `uv run uvicorn app.main:app`.
2. Execute `curl -i -X DELETE http://localhost:8000/tasks/999`.
3. Observe o status HTTP retornado.

## Comportamento esperado

A API deve retornar `404 Not Found` com `{"detail":"Tarefa não encontrada"}`.

## Evidências

```text
HTTP/1.1 204 No Content
```

**Versão/commit:** `v0.1.0`
**Definição de pronto:** teste de regressão cobrindo tarefa inexistente e contrato HTTP corrigido.
