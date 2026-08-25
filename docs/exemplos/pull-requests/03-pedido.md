# ci: publicar relatório de cobertura como artifact

## Contexto

Atende ao pedido da equipe de tornar o resultado de cobertura acessível e auditável em cada execução da CI.

Closes #3

## Tipo de mudança

- [ ] Correção de bug
- [ ] Nova funcionalidade
- [x] Pedido de manutenção/documentação
- [ ] Mudança incompatível (breaking change)

## O que mudou

- o `pytest-cov` gera o arquivo `coverage.xml`;
- o workflow publica o arquivo no artifact `coverage-report` usando `if: always()`;
- `if-no-files-found: ignore` preserva a causa original caso a suíte falhe antes de gerar o XML;
- o README documenta o relatório.

## Como validar

1. Abra este PR e aguarde o job `quality`.
2. Acesse a execução do workflow.
3. Baixe `coverage-report` na seção **Artifacts**.
4. Confirme que o ZIP contém `coverage.xml`.

## Evidências

Link da execução: `https://github.com/organizacao/repositorio/actions/runs/123456789` (exemplo)

## Risco e rollback

Risco operacional baixo; há pequeno consumo adicional de armazenamento. Para rollback, remova o passo `upload-artifact` e a saída XML.

## Checklist

- [x] Workflow com permissões mínimas
- [x] Dependências de Actions fixadas pelo SHA completo da release
- [x] Documentação atualizada
- [x] CI verde
