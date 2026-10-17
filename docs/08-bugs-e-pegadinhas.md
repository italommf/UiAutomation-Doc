# 08 — Bugs reais e pegadinhas

Legenda de confiança: 🧪 reproduzido no laboratório · 📖 deduzido lendo o código (não executado).

## Bugs no código da lib
| # | Local | Problema | Efeito | Como evitar |
|---|---|---|---|---|
| 1 | `TextPattern.RangeFromChild` (L5956) 📖 | passa `Control.Element` (a *property* da classe) em vez de `child.Element` | erro/valor inválido sempre | use `child.GetPattern(PatternId.TextChildPattern).TextRange` ou `pattern.pattern.RangeFromChild(child.Element)` |
| 2 | `TextRange.CompareEndpoints` (L5642) 📖 | passa o wrapper `textRange` em vez de `textRange.textRange` | `COMError`/`TypeError` | `r.textRange.CompareEndpoints(src, other.textRange, tgt)` |
| 3 | `TableControl.GetTableItemsValue` (L9837) 📖 | `row > 0`/`column > 0` em vez de `>= 0` | linha/coluna 0 nunca é selecionada (devolve a tabela toda) | filtre você mesmo o resultado completo |
| 4 | `GetClipboardText/Html/Bitmap` 📖 | não chamam `CloseClipboard()` quando o formato não existe | clipboard fica preso ao processo | cheque `GetClipboardFormats()` antes |
| 5 | `Control.DoubleClick` (L7307) 📖 | `x, y = self.MoveCursorToInnerPos(...)` quando retorna `None` (controle com área 0) | `TypeError: cannot unpack NoneType` | verifique `BoundingRectangle` antes |
| 6 | `SendKeys('')` 📖 | laço faz `text[i]` antes de checar tamanho | `IndexError` | proteja com `if text:` |
| 7 | `SendKeys` hold keys 📖 | tupla `holdKeys` repete `'LCONTROL'` e não tem `'RCONTROL'` | `{RControl}` não segura a tecla | use `{Ctrl}` |
| 8 | `SendInput(*inputs)` 📖 | envia um por vez e retorna só o último retorno; sem inputs → `UnboundLocalError` | contagem enganosa | |
| 9 | `WalkControl(c, includeTop=True, maxDepth=0)` 🧪 | devolve o topo mesmo com `maxDepth=0` | lista não vazia | |
| 10 | `Bitmap.FromControl` (L3515) 📖 | no 2º laço `control.GetParentControl()` sem checar `None` | `AttributeError` se nenhum ancestral tem HWND | |
| 11 | `GIF.ToGifFile(path, bitmaps, delays=None)` 📖 | `assert len(bitmaps)==len(delays)` com `None` | `TypeError` | passe `delays` sempre |
| 12 | `Rect` 📖 | `__eq__` sem `__hash__`; `rect == None` falha | não vira chave de dict | converta para tupla |
| 13 | `Control.__init__(Depth=0)` 📖 | `Depth or searchDepth` ⇒ 0 é ignorado | `Depth=0` não filtra nada | use `Compare` |
| 14 | `Control(**searchProperties)` 🧪 | chaves desconhecidas são aceitas e **ignoradas** na comparação (`Foo='bar'` não filtra, apenas aparece no log) | falsa sensação de filtro; `ButtonControl(Name='Clicar', Foo='bar')` achou o botão | só use as chaves de `Control.ValidKeys` |
| 15 | `Control.GetPropertyValue` 🧪 | muitas propriedades devolvem `POINTER(IUnknown)` sem conteúdo (ControllerFor, DescribedBy, FlowsTo…) | | |
| 16 | `ProcessInfo.__str__` 📖 | falta o `)` final | cosmético | |

## Comportamentos surpreendentes (não são bugs, mas mordem)
1. **`Name` sobrescrito pelo app.** Se o app define `AccessibleName`, `Name` não é o texto exibido (aconteceu no laboratório: o rótulo mostrava "evento: clique 1" mas `Name` valia o nome acessível). Leia o conteúdo por `ValuePattern`/`LegacyIAccessiblePattern.Value`/`TextPattern`.
2. **Busca por `RegexName` usa `re.match`** (início da string). `RegexName="licar"` não acha "Clicar" 🧪.
3. **Busca é lazy e bloqueante.** `ctrl.Name` num controle que não existe espera até `TIME_OUT_SECOND` (10 s; 3 s depois de `SetGlobalSearchTimeout(3)` 🧪) e levanta `LookupError`. Use `Exists(0, 0)` para testar sem esperar (~uma varredura).
4. **`Exists()` substitui o elemento em cache.** Chamar `Exists` em outro controle com o mesmo critério muda qual elemento ele aponta.
5. **Árvore é Raw View.** Aparecem nós que o Inspect "Control View" esconde; `GetChildren()` do Window do lab devolveu 29 filhos incluindo `TitleBarControl` (último). Índices `w[n]` mudam se o app adicionar elementos.
6. **Nós virtualizados / invisíveis.** Itens fora da tela podem ter `BoundingRectangle` zero (visto nas abas do Bloco de Notas: Rect `(0,0,0,0)`); cliques com área zero são ignorados com log amarelo. Use `ScrollItemPattern.ScrollIntoView()` / `VirtualizedItemPattern.Realize()`.
7. **`GetPattern` cria objeto novo a cada chamada** e engole erros ⇒ `None`. Não confunda "não suporta" com "erro transitório".
8. **Defaults de `waitTime`/`searchInterval` são congelados na definição** (veja 01).
9. **Cliques/teclas são globais.** Vão para a janela que estiver em foco/sob o cursor — se o foco mudar no meio, a ação cai em outro app. Prefira patterns.
10. **Textos multi-linha.** `ValuePattern.Value` do TextBox multiline do WinForms devolve `\r\n`.
11. **Campo de senha.** `IsPassword=True`; `ValuePattern.Value` e `LegacyIAccessible.Value` devolvem `''` 🧪 (mas `SetValue` funciona).
12. **ProgressBar read-only.** `RangeValuePattern.SetValue` → `COMError` 🧪.
13. **`SelectionPattern.CanSelectMultiple` pode mentir** em listas Win32 (proxy) 🧪.
14. **`SetActive`/`SetForegroundWindow` podem falhar** (Windows impede roubar foco). Tente `SwitchToThisWindow` ou mínimo→restaurar.
15. **`GetWindowText` corta em 260.** Para textos longos use `GetEditText(hwnd)` ou `ValuePattern`.
16. **`Click` real move o mouse do usuário** e `SendKeys` digita onde estiver o foco. Em máquina em uso isso é perigoso.
17. **Apps elevados (admin).** Um Python sem elevação não consegue controlar janelas de processo elevado (UIPI): leituras podem funcionar, entradas simuladas são descartadas. Rode como admin ou use `RunScriptAsAdmin` (deduzido de como o Windows funciona, não testado aqui).
18. **Vários monitores.** `GetScreenSize()` é só o primário; `MoveToCenter` centraliza nele. Use `GetMonitorsRect()` e `GetVirtualScreenSize()` (no ambiente de teste: primário 2560×1440, virtual 3640×1920, outro monitor em x negativo).
19. **`EnumProcessByWMI` precisa do pacote `wmi`** 🧪 (`ModuleNotFoundError`).
20. **Nomes do `Keys` vs `SpecialKeyNames`:** em `SendKeys` você escreve `{Enter}`; em `SendKey` você passa `Keys.VK_RETURN`.
21. **Efeito colateral do import:** DPI awareness + restype globais + log em arquivo (veja 01).
22. **Locale.** `Name`, `LocalizedControlType` e textos de botões saem no idioma do Windows/do app ("Abrir", "Fechar", "janela"). Prefira `AutomationId`/`ClassName`, que não são traduzidos.
23. **Encoding.** Se um app devolver texto com mojibake (ocorreu no meu laboratório porque o `.ps1` estava sem BOM), o problema é do app, não da lib.
