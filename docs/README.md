# uiautomation — documentação completa (v2.0.29)

Estudo feito lendo **o código-fonte instalado** em
`.venv/Lib/site-packages/uiautomation/` (um único módulo de ~10.850 linhas) e confirmando
comportamentos num laboratório próprio (o código dele está na seção 4 do [README principal](../README.md)).

| Arquivo | Conteúdo |
|---|---|
| [01-arquitetura.md](01-arquitetura.md) | Como a lib é montada: COM, singleton, DLLs, efeitos colaterais do `import`, threads |
| [02-constantes-e-enums.md](02-constantes-e-enums.md) | TODAS as constantes: ControlType, PatternId, PropertyId, Keys, SW, MB… (gerado) |
| [03-control.md](03-control.md) | A classe `Control`: busca, propriedades, navegação, ações, janelas |
| [04-controles-especificos.md](04-controles-especificos.md) | Os 40 tipos (`ButtonControl`…`WindowControl`) e seus padrões |
| [05-patterns.md](05-patterns.md) | Os 34 patterns (Invoke, Value, Toggle, Text…) com retornos e armadilhas |
| [06-funcoes-win32.md](06-funcoes-win32.md) | Mouse, teclado, `SendKeys`, janelas, tela, processos, hotkeys |
| [07-bitmap-clipboard-logger.md](07-bitmap-clipboard-logger.md) | `Bitmap`, clipboard, `Logger`, `Rect` |
| [08-bugs-e-pegadinhas.md](08-bugs-e-pegadinhas.md) | Bugs reais no código e comportamentos surpreendentes |
| [09-dicas-e-receitas.md](09-dicas-e-receitas.md) | Boas práticas, receitas prontas, depuração |
| [11-internos-algoritmos.md](11-internos-algoritmos.md) | Como busca, mouse, `SendKeys`, processos, captura e hotkeys funcionam por dentro (lido do código) |
| [10-referencia-api-completa.md](10-referencia-api-completa.md) | Lista exaustiva de classes/métodos/funções com linha e docstring (gerado) |

## Números da lib
- 140 classes, 549 métodos/propriedades, 117 funções de módulo, ~295 nomes exportados por `from uiautomation import *`.
- Dependência única: `comtypes`. Windows apenas.
- `from uiautomation import *` e `import uiautomation as auto` expõem tudo (não há `__all__`); constantes como `SEARCH_INTERVAL` precisam ser alteradas em `uiautomation.uiautomation` (veja 01).

Os arquivos `02` e `10` foram gerados automaticamente a partir do código-fonte da biblioteca (análise da AST do `uiautomation.py`).
