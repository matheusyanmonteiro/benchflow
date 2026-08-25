# Guia de contribuição

Este repositório usa um GitFlow simplificado, com rastreabilidade entre issue, branch, pull request e entrega.

## Fluxo de trabalho

1. Abra uma issue usando o formulário de **Bug**, **Feature** ou **Pedido**.
2. Aguarde a triagem e associe responsável, prioridade e milestone quando aplicável.
3. Crie uma branch a partir da base correta:
   - `feature/<numero>-<descricao>` para funcionalidade;
   - `fix/<numero>-<descricao>` para correção;
   - `chore/<numero>-<descricao>` para pedido técnico ou manutenção;
   - `hotfix/<numero>-<descricao>` a partir da `main` para correção urgente.
4. Faça commits pequenos seguindo [Conventional Commits](https://www.conventionalcommits.org/):
   `feat:`, `fix:`, `test:`, `docs:`, `refactor:`, `chore:` ou `ci:`.
5. Abra um draft PR cedo, relacione a issue com `Closes #<numero>` e preencha o template.
6. Antes do merge, obtenha aprovação, resolva as conversas e aguarde o check obrigatório `quality`.
7. Use **Squash and merge**. O título do PR se torna a mensagem do commit na branch protegida.

## Estratégia de branches

- `main`: versão estável e potencialmente implantável; aceita mudanças apenas por pull request.
- `develop`: integração opcional para ciclos com várias features antes de uma release.
- `feature/*`, `fix/*` e `chore/*`: trabalho curto, associado a uma issue.
- `release/*`: estabilização de uma versão antes do PR para `main`.
- `hotfix/*`: correção urgente criada a partir de `main`, também entregue via PR.

Para uma equipe com entrega contínua, os mesmos controles podem ser usados sem `develop`: as branches curtas abrem PR diretamente para `main`.

## Qualidade local

```bash
uv sync --dev
uv run ruff check .
uv run pytest
```

A suíte falha se a cobertura total ficar abaixo de 95%. Mudanças de comportamento devem incluir testes do caminho feliz e dos erros relevantes.

## Revisão

O autor deve manter o PR pequeno e fornecer instruções reproduzíveis. O revisor verifica:

- aderência aos critérios de aceite da issue;
- legibilidade e escopo da solução;
- testes, cobertura e compatibilidade;
- riscos de segurança, dados e operação;
- estratégia de rollback quando a mudança tiver impacto operacional.
