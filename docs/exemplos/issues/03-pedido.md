# [Pedido]: Publicar o relatório de cobertura da CI

**Labels:** `request`, `triage`
**Categoria:** Automação/CI
**Prazo:** antes da apresentação do benchmark

## O que precisa ser feito?

Disponibilizar o arquivo `coverage.xml` como artifact de cada execução do workflow de pull request, inclusive quando um teste falhar depois de o relatório ser criado.

## Contexto e resultado esperado

Durante a revisão, a equipe precisa comprovar de forma auditável que a cobertura mínima foi verificada. O artifact permitirá baixar o resultado diretamente pela execução do GitHub Actions.

## Critérios de aceite

- [ ] O job de testes gera `coverage.xml`.
- [ ] O workflow publica um artifact chamado `coverage-report`.
- [ ] A ausência do arquivo em uma falha antecipada não mascara o erro original.
- [ ] O README explica onde o relatório é gerado.
