# 08 — Bugs reais e pegadinhas

Legenda: 🧪 **reproduzido** em teste real (detalhes em `12-relatorio-de-validacao.md`) · 📖 deduzido lendo o código (não conseguido reproduzir).

## Bugs no código da lib (2.0.29)
| # | Local | Problema | Efeito | Como evitar |
|---|---|---|---|---|
| 1 | `Bitmap.Clone()` e `Bitmap.RotateWithSameSize()` 🧪 | a DLL devolve um ponteiro de 64 bits mas essas duas funções ficaram sem `restype` (as outras têm `c_size_t`); o ponteiro é truncado | **`OSError: access violation`** em 100% das chamadas (5/5), pode corromper memória | use `Copy()` no lugar de `Clone()`; para girar mantendo o tamanho use `Rotate`/`RotateFlip` e recorte/cole |
| 2 | `SetClipboardText` com emoji 🧪 | tamanho calculado com `len(text)` (code points), mas o Windows usa UTF‑16 | texto **truncado**: `'ok 😀 fim'` → `'ok 😀 fi'` | evite caracteres acima de U+FFFF ou grave por outro meio (`pyperclip`, `win32clipboard`) |
| 3 | `SetClipboardHtml` + `GetClipboardHtml` 🧪 | bloco alocado com `len+4` **sem zerar** e copiado com `strncpy(n=len)`: **sem `NUL` final** | `GetClipboardHtml` pode ler lixo → `UnicodeDecodeError` ou texto com lixo depois de `</html>` (47 de 60 repetições com memória "suja") | leia o bloco cru com `ctypes` e corte em `</html>` |
| 4 | `GetClipboardText/Html/Bitmap` 🧪 | não chamam `CloseClipboard()` quando o formato pedido não existe | o clipboard **fica preso**: programas normais (abrem com *handle* de janela) falham com erro 5 até o Python sair; **chamadas normais não vazam** | cheque `'CF_UNICODETEXT' in GetClipboardFormats().values()` antes, ou chame `ctypes.windll.user32.CloseClipboard()` depois |
| 5 | `SendKeys` com caractere > U+FFFF 🧪 | o scancode Unicode é truncado em 16 bits | `😀` sai como `` | não envie emoji por `SendKeys` (o clipboard também tem problema com eles, item 2) |
| 6 | `SendKeys('{Backspace}')`, `{Foo}`, `{CapsLock}` 🧪 | nome inexistente vira "caractere" e vai a `ord()` | **`TypeError: ord() expected a character…`** (não é texto literal) | use os nomes de `SpecialKeyNames`: `{Back}`, `{Capital}`… |
| 7 | `SendKeys('')` 🧪 | laço faz `text[0]` sem checar | `IndexError` | proteja com `if texto:` |
| 8 | `SendKeys('{RControl}a')` 🧪 | `holdKeys` repete `'LCONTROL'` e não tem `'RCONTROL'` | o Ctrl solta **antes** do `a` | use `{Ctrl}`/`{LControl}` |
| 9 | `SendKeys('{Alt}…')` 🧪 | todas as teclas VK vão com `ExtendedKey`; `VK_MENU` estendido = **Alt Gr** | em layouts com Alt Gr (pt‑BR testado) vira **Ctrl+Alt**: `{Alt}x` chega como Ctrl+Alt+X | use **`{LAlt}`** para Alt puro |
| 10 | `SendInput(*inputs)`, `SendUnicodeChar` 🧪 | envia um evento por vez e retorna só o último retorno | devolvem `1` mesmo com 2 eventos (o docstring promete a contagem) | ignore o valor de retorno |
| 11 | `WalkControl(c, includeTop=True, maxDepth=0)` 🧪 | devolve o topo mesmo com `maxDepth=0` | lista não vazia | |
| 12 | `TableControl.GetTableItemsValue(row, column)` 🧪 | `row > 0`/`column > 0` em vez de `>= 0` | linha/coluna 0 nunca é selecionável (devolve a tabela toda); no WinForms a matriz inclui a **linha de cabeçalho** e uma **coluna de cabeçalho de linha** vazia | filtre o resultado completo você mesmo |
| 13 | `Control.DoubleClick` 🧪 | `x, y = self.MoveCursorToInnerPos(...)` quando retorna `None` (área zero) | `TypeError: cannot unpack NoneType` | verifique `BoundingRectangle` antes |
| 14 | `TextPattern.RangeFromChild` 🧪 | passa `Control.Element` (a *property* da classe) | `ArgumentError` sempre | `child.GetPattern(PatternId.TextChildPattern).TextRange` |
| 15 | `TextRange.CompareEndpoints` 🧪 | passa o wrapper `textRange` em vez de `textRange.textRange` | `ArgumentError` | `r.textRange.CompareEndpoints(src, outro.textRange, tgt)` |
| 16 | `ItemContainerPattern.FindItemByProperty(None, …)` 🧪 | sempre chama `control.Element` | `AttributeError` com `None` | passe um `Control` (ex.: o primeiro item) |
| 17 | `SynchronizedInputPattern.StartListening()` 🧪 | o método nativo exige `inputType`; o wrapper não passa | `TypeError` | chamar `p.pattern.StartListening(inputType)` direto (não testado) |
| 18 | `Control.GetPatternAs` 🧪 | devolve um `int` (o código marca "todo") | inutilizável | use `GetPattern` |
| 19 | `GIF.ToGifFile(path, bitmaps, delays=None)` 🧪 | `len(None)` | `TypeError` | passe `delays` (ms) sempre |
| 20 | `Rect` 🧪 | `__eq__` sem `__hash__`; `rect == None` falha | não vira chave de dict; `AttributeError` | converta para tupla |
| 21 | `Control.__init__(Depth=0)` 🧪 | `Depth or searchDepth` ⇒ 0 é ignorado | `Depth=0` não filtra | use `Compare` |
| 22 | `Control(**searchProperties)` 🧪 | chaves desconhecidas são aceitas e **ignoradas** na comparação; `Name`+`SubName` juntos também são aceitos (valem os dois) | falsa sensação de filtro | só use as chaves de `Control.ValidKeys` |
| 23 | `ShowWindow` e quem o usa (`Show/Hide/ShowWindow`, `Maximize/Minimize/Restore`) 🧪 | o retorno é "a janela estava visível antes", não "sucesso" (o docstring diz sucesso) | `ShowWindow(SW.Show)` depois de `Hide` devolve `False` mesmo funcionando; `Maximize()` numa janela escondida devolve `False` | confira com `IsWindowVisible`/`IsZoomed`/`IsIconic` |
| 24 | `Exists()`/`Refind()`/propriedades com elemento morto 🧪 | não tratam `COMError` | levantam `COMError 0x80040201` em vez de `False` | `try/except COMError` ao reutilizar controles de janelas que podem fechar |
| 25 | `Bitmap.FromControl` (2º laço) 📖 | `control.GetParentControl()` sem checar `None` | `AttributeError` se nenhum ancestral tem HWND (não reproduzido) | |
| 26 | `ProcessInfo.__str__` 🧪 | falta o `)` final | cosmético | |

## Comportamentos surpreendentes (não são bugs, mas mordem)
1. **`Invoke` é síncrono e pode ficar preso** num botão que abre diálogo modal (e trava outras chamadas UIA ao mesmo app por ~66 s) 🧪 → veja `05-patterns.md`. Rode em thread ou use `Click()`.
2. **`Name` sobrescrito pelo app.** Se o app define `AccessibleName`, `Name` não é o texto exibido 🧪. Leia o conteúdo por `Value`/`Text`.
3. **`RegexName` usa `re.match`** (início da string): `"licar"` não acha "Clicar" 🧪.
4. **Busca é lazy e bloqueante.** `ctrl.Name` num controle inexistente espera até `TIME_OUT_SECOND` (10 s; 3 s após `SetGlobalSearchTimeout(3)`) e levanta `LookupError` 🧪. Use `Exists(0, 0)` para testar sem esperar.
5. **`Exists()` substitui o elemento em cache.**
6. **A árvore é Raw View** (mais nós que o Inspect "Control View") 🧪.
7. **Itens virtualizados/fora da tela** podem ter retângulo zero; cliques com área zero são ignorados com aviso amarelo 🧪 (e `MoveCursorToInnerPos`/`GetPosition` devolvem `None`). `ToBitmap` de um controle de área zero captura o **pai** 🧪.
8. **`GetPattern` cria objeto novo** a cada chamada e engole erros ⇒ `None` 🧪.
9. **Defaults de `waitTime`/`searchInterval` são congelados na definição** 🧪 (mudar `OPERATION_WAIT_TIME` depois do import não altera nada; `SendKey` seguiu dormindo 0,5 s).
10. **Cliques/teclas são globais** — vão para a janela em foco/sob o cursor.
11. **Multilinha usa `\r\n`**; **campo de senha**: `Value` vazio mas `SetValue` funciona 🧪.
12. **ProgressBar é somente leitura** (`SetValue` → `COMError`) 🧪.
13. **`SelectionPattern`** de ListBox Win32 multisseleção: `CanSelectMultiple` pode mentir e `GetSelection()` pode devolver item antigo 🧪 — use `IsSelected` por item.
14. **`SetActive`/`SetForegroundWindow` podem falhar** (o Windows impede roubar foco); no teste funcionou.
15. **`GetWindowText` corta em 259 caracteres** 🧪 (`Name` devolve 300). Para textos longos: `GetEditText(hwnd)` (sem limite 🧪) ou `ValuePattern`.
16. **`Click` real move o mouse do usuário** e `SendKeys` digita onde está o foco.
17. **Apps elevados (admin):** um Python sem elevação normalmente não opera janelas elevadas (regra do Windows; não testado aqui).
18. **Vários monitores:** `GetScreenSize()` é só o primário; `MoveToCenter` centraliza nele 🧪; `GetMonitorsRect()` **não** devolve o primário primeiro 🧪; `SetCursorPos` aceita coordenadas negativas 🧪.
19. **`EnumProcessByWMI` precisa do pacote `wmi`** 🧪 (com `wmi` instalado funciona; devolve `exePath='None'` como texto para processos sem caminho).
20. **`Keys` vs `SpecialKeyNames`:** em `SendKeys` você escreve `{Enter}`; em `SendKey` passa `Keys.VK_RETURN`.
21. **Efeitos do `import`** 🧪: DPI por monitor, `restype` global de `user32.GetForegroundWindow`, log em arquivo na 1ª mensagem (veja 01). O `import` **não** cria o COM nem carrega a DLL.
22. **Locale.** `Name`, `LocalizedControlType` e textos de botões saem no idioma do Windows ("botão", "Pressionar") 🧪. Prefira `AutomationId`/`ClassName`.
23. **`TerminateProcessByName` compara nome exato** (`==`, sensível a maiúsculas) 🧪 e o processo sai com código `0xFFFFFFFF`.
24. **`LogControl`/`EnumAndLogControl` gravam no arquivo de log** 🧪 (incluindo o `Name`) e custam ~95 ms por controle (34 consultas de pattern) contra ~3 ms do `WalkControl` 🧪.
25. **`ColorfullyWrite`**: cor inexistente ou sem `</Color>` fica literal; aninhado não aninha (`<Color=Green>a <Color=Red>b</Color> c</Color>` imprime `a <Color=Red>b c</Color>`) 🧪.
26. **`Click(x)` com `x` negativo** é relativo à borda direita e `Click(-10,-10)` ao canto inferior direito 🧪; as coordenadas são em pixels **físicos** (com escala de 125%, 10 px viraram 8 px lógicos no app).
27. **Encoding.** Mojibake vindo de um app não é culpa da lib.
