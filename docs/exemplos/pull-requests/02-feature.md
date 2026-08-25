# feat(api): permitir filtro de tarefas concluídas

## Contexto

Permite que consumidores da API consultem somente tarefas pendentes ou concluídas sem criar rotas específicas para cada estado.

Closes #2

## Tipo de mudança

- [ ] Correção de bug
- [x] Nova funcionalidade
- [ ] Pedido de manutenção/documentação
- [ ] Mudança incompatível (breaking change)

## O que mudou

- `GET /tasks` aceita o query parameter opcional `completed`;
- o repositório filtra tarefas quando o parâmetro é informado;
- foram cobertos os cenários sem filtro, `true`, `false` e valor inválido;
- a documentação da API é atualizada automaticamente pelo FastAPI.

## Como validar

1. Crie uma tarefa pendente e outra concluída.
2. Execute `GET /tasks?completed=true` e confirme somente a concluída.
3. Execute `GET /tasks?completed=false` e confirme somente a pendente.
4. Execute `uv run pytest`.

## Evidências

```text
GET /tasks?completed=true  HTTP/1.1 200 OK
[{"id":2,"title":"Revisar PR","description":"","completed":true}]
```

## Risco e rollback

Mudança retrocompatível: sem o parâmetro, a resposta permanece igual. Para rollback, reverta o squash commit; não há migração de dados.

## Checklist

- [x] Critérios de aceite verificados
- [x] Testes adicionados
- [x] Cobertura mínima preservada
- [x] OpenAPI conferida
- [x] CI verde
