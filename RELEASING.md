# Guia de releases e packages

As releases seguem [Semantic Versioning](https://semver.org/) e são geradas a partir de tags no formato `vMAJOR.MINOR.PATCH`.

## O que é automatizado

- todo merge na `main` atualiza uma GitHub Release em rascunho;
- PRs são agrupados nas notas conforme seus labels;
- tags `v*` executam novamente lint, testes e cobertura;
- o workflow rejeita uma tag diferente da versão do `pyproject.toml`;
- `wheel`, `sdist` e `SHA256SUMS` são anexados à GitHub Release;
- uma imagem é testada e publicada no GitHub Container Registry;
- artifacts e imagem recebem attestations de procedência assinadas pelo GitHub;
- versões estáveis também atualizam a tag de container `latest`.

## Labels de versionamento

| Label | Impacto | Exemplo |
| --- | --- | --- |
| `major` | Incrementa MAJOR | Mudança incompatível |
| `minor` ou `enhancement` | Incrementa MINOR | Nova funcionalidade compatível |
| `patch` ou `bug` | Incrementa PATCH | Correção compatível |
| `skip-changelog` | Omite das notas | Manutenção sem valor para a release |

## Publicar uma versão

1. Confira o rascunho em **Releases** e revise destaques e migrações.
2. Atualize `project.version` no `pyproject.toml` via PR.
3. Aguarde a CI da `main` ficar verde após o merge.
4. Crie e envie uma tag anotada:

   ```bash
   git switch main
   git pull --ff-only origin main
   git tag -a v0.1.0 -m "BenchFlow v0.1.0"
   git push origin v0.1.0
   ```

5. Acompanhe o workflow **Publish Release**. Ele publica o rascunho somente depois que todas as validações e o push da imagem terminarem.

## Consumir a imagem

```bash
docker pull ghcr.io/matheusyanmonteiro/benchflow:0.1.0
docker run --rm -p 8000:8000 ghcr.io/matheusyanmonteiro/benchflow:0.1.0
curl http://127.0.0.1:8000/health
```

Tags publicadas para cada versão:

- `0.1.0`: versão semântica imutável por convenção;
- `v0.1.0`: equivalente à tag Git;
- `sha-<12 caracteres>`: rastreabilidade até o commit;
- `latest`: versão estável mais recente.

## Verificar os artifacts

Depois de baixar todos os arquivos da release:

```bash
sha256sum --check SHA256SUMS
python -m pip install ./benchflow_crud-0.1.0-py3-none-any.whl
gh attestation verify ./benchflow_crud-0.1.0-py3-none-any.whl --repo matheusyanmonteiro/benchflow
gh attestation verify oci://ghcr.io/matheusyanmonteiro/benchflow:0.1.0 --repo matheusyanmonteiro/benchflow
```

Em caso de falha antes da publicação, corrija a causa e execute novamente o workflow. Não mova uma tag de versão já publicada; crie uma nova versão de patch.
