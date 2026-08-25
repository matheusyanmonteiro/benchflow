# [Feature]: Filtrar tarefas por status de conclusão

**Labels:** `enhancement`, `triage`
**Prioridade sugerida:** Média

## Problema ou oportunidade

Como pessoa que organiza uma lista extensa, preciso visualizar apenas tarefas pendentes ou concluídas para concentrar a revisão no conjunto relevante.

## Solução proposta

Adicionar o query parameter opcional `completed` em `GET /tasks`. Sem o parâmetro, o endpoint mantém o comportamento atual; com `true` ou `false`, retorna somente tarefas do status solicitado.

## Critérios de aceite

- [ ] Sem `completed`, todas as tarefas continuam sendo retornadas.
- [ ] Com `completed=true`, somente tarefas concluídas são retornadas.
- [ ] Com `completed=false`, somente tarefas pendentes são retornadas.
- [ ] Um valor inválido recebe `422 Unprocessable Entity`.
- [ ] A documentação OpenAPI exibe o novo parâmetro.
- [ ] Há testes automatizados e a cobertura permanece acima de 95%.

## Alternativas consideradas

Criar rotas `/tasks/completed` e `/tasks/pending`, descartado por duplicar o recurso e reduzir a flexibilidade de futuros filtros.
