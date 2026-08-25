# fix(api): retornar 404 ao excluir tarefa inexistente

## Contexto

Corrige o contrato enganoso do endpoint de exclusão, que confirmava uma remoção sem encontrar o recurso.

Closes #1

## Tipo de mudança

- [x] Correção de bug
- [ ] Nova funcionalidade
- [ ] Pedido de manutenção/documentação
- [ ] Mudança incompatível (breaking change)

## O que mudou

- o repositório passa a informar se encontrou a tarefa antes da exclusão;
- o endpoint converte o resultado negativo em `404 Not Found`;
- foi adicionado teste de regressão para um ID inexistente.

## Como validar

1. Execute `uv run pytest`.
2. Inicie a API e envie `DELETE /tasks/999`.
3. Confirme status `404` e mensagem `Tarefa não encontrada`.

## Evidências

```text
9 passed
TOTAL coverage: 100%
```

## Risco e rollback

Risco baixo. Clientes que dependiam incorretamente de `204` para IDs inexistentes perceberão a correção. O rollback consiste em reverter o único commit do PR.

## Checklist

- [x] O título segue Conventional Commits
- [x] O escopo está pequeno e focado
- [x] Adicionei ou atualizei testes
- [x] A cobertura continua em pelo menos 95%
- [x] Não incluí credenciais ou dados sensíveis
- [x] A CI está verde
