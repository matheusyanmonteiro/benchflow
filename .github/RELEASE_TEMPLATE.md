## Destaques

<!-- Resuma em 2–4 itens o valor entregue nesta versão. -->

-

## Compatibilidade e migração

<!-- Informe breaking changes, migrações ou escreva "Sem mudanças incompatíveis". -->

Sem mudanças incompatíveis conhecidas.

## Instalação

### Imagem de container

```bash
docker pull ghcr.io/{{REPOSITORY}}:{{VERSION}}
docker run --rm -p 8000:8000 ghcr.io/{{REPOSITORY}}:{{VERSION}}
```

### Pacote Python

Baixe o `wheel` ou o `sdist` anexado nesta release e valide-o com o arquivo `SHA256SUMS`.

## Validação

- [ ] CI da tag aprovada
- [ ] Imagem publicada no GHCR
- [ ] `wheel`, `sdist` e checksums anexados
- [ ] Notas de atualização revisadas
