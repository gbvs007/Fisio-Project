# FisioGestão — Protótipo do App

Protótipo navegável do FisioGestão, um prontuário simples para fisioterapeutas.

**Tudo está em um único arquivo: [`index.html`](index.html).** Abra no navegador e pronto. Não precisa instalar nada.

## Telas

1. Login
2. Criar conta (assinatura)
3. Início (celular)
4. Menu hambúrguer aberto
5. Início (computador)
6. Consultar paciente (com busca e filtros)
7. Cadastrar paciente
8. Ficha do paciente (anamnese, evolução, sessões, mídia e comentários)
9. Componentes e estados

Use a barra no topo para ir a uma tela ou ver todas lado a lado. Os botões e links dentro das telas também levam de uma tela para outra.

## Publicar no GitHub Pages

1. Crie um repositório no GitHub e envie estes arquivos.
2. No repositório, abra **Settings → Pages**.
3. Em **Branch**, escolha `main` e a pasta `/ (root)`, depois clique em **Save**.
4. Em cerca de um minuto o protótipo fica disponível em `https://SEU-USUARIO.github.io/NOME-DO-REPOSITORIO/`.

## Arquivos

| Arquivo | Para que serve |
|---|---|
| `index.html` | O protótipo completo. É o único arquivo necessário. |
| `project/*.dc.html` | O código original de cada tela, feito no editor de design do Claude. |
| `build.py` + `shell.html` | Geram o `index.html` a partir das telas originais. Rode `python build.py` se mudar alguma tela. |

> Os dados exibidos (pacientes, sessões, nomes) são fictícios. Este é um protótipo visual: não existe servidor nem banco de dados.
