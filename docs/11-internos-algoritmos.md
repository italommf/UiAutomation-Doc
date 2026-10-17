# 11 — Internos: como os algoritmos realmente funcionam

Tudo abaixo foi **deduzido lendo o código** (nada executado). Números de linha são do `uiautomation.py` 2.0.29.

## 11.1 Busca: `Exists` → `FindControl` → `WalkControl`
`Control.Exists` (L7098):
1. **Controle de elemento direto** (`_elementDirectAssign`, criado por `GetChildren`, `ControlFromPoint`…): não busca. Pega a raiz com `IUIAutomation.GetRootElement()`; se `CompareElements(self._element, raiz)` → `True`; senão `True` se `ViewWalker.GetParentElement(elemento)` existir. Não há `try/except`: um elemento já morto pode levantar `COMError` em vez de devolver `False`.
2. Sem critérios → `LookupError`.
3. Zera `_element`; se `searchFromControl` existe e **ainda não foi resolvido**, chama `prev.Exists(...)` com os **mesmos** `maxSearchSeconds/interval` — ou seja, uma cadeia `a.b.c` resolve pai antes do filho, e o orçamento de tempo é aplicado a cada nível (o tempo total pode passar do que você pediu).
4. Laço: `FindControl(searchFromControl, _CompareFunction, searchDepth, findFromSelf=False, foundIndex)`. Achou → guarda `control.Element` em `self._element` e zera `_element` do temporário. Não achou → dorme `min(restante, intervalo)`; se acabou o tempo, devolve `False`. A varredura roda **antes** de checar o prazo, então o tempo real = prazo + até uma varredura.
5. `DEBUG_SEARCH_TIME=True` loga `traverseCount` (nós visitados) e duração.

`FindControl` → `WalkControl(control, includeTop=findFromSelf, maxDepth)` e conta ocorrências até `foundIndex` (guarda `child.traverseCount`). Se `control` é `None`/falsy → começa na raiz. ⚠ `if not control` usa `__bool__`/`__len__`? `Control` não define `__bool__`; define `__getitem__` mas não `__len__`, então é sempre truthy.

`WalkControl` (L10474) é **iterativo, pré-ordem (profundidade primeiro)**: mantém uma pilha `controlList` com o "próximo irmão" por nível. Para cada nó: `yield`; guarda o próximo irmão no nível atual; se `depth+1 < maxDepth`, desce para o primeiro filho. Consequências:
- Cada nó custa ≥ 2 chamadas COM só de navegação (`GetNextSibling` + `GetFirstChild`) mais as propriedades que o critério pedir. Critério `AutomationId` = 1 chamada por nó; `Name` = 1; `Compare` com várias propriedades = várias.
- Árvore muito larga (milhares de itens de lista) é o gargalo; `searchDepth` e começar de um ancestral mais próximo reduzem diretamente o nº de nós.
- A ordem é a da Raw View (inclui painéis intermediários); `foundIndex=2` é "o segundo na ordem de pré-ordem".

`_CompareFunction` (L7061) testa as chaves na ordem do dicionário `searchProperties`. Em `__init__` o dicionário começa com os `**kwargs` extras (é o próprio dict dos kwargs) e depois recebe, nesta ordem: `Name`, `SubName`, `RegexName`, `ClassName`, `AutomationId`, `ControlType`, `Depth`, `Compare` (só os não‑`None`; confirmado pelo `GetSearchPropertiesStr` que mostrou `{Name:…, ControlType:…}`). Retorna `False` na primeira falha — o **custo depende da ordem**: `Name`/`ClassName`/`AutomationId` são testados antes de `ControlType`, e `Compare` por último. Chaves desconhecidas não têm `elif`, logo passam.

`Disappears` desliga temporariamente `DEBUG_EXIST_DISAPPEAR` (variável global modificada com `global`) para não logar cada `Exists(0,0)`, e a restaura — não é thread-safe.

## 11.2 Movimento do mouse: `MoveTo` (L2012)
```
moveTime  = MAX_MOVE_SECOND / moveSpeed          (0 se moveSpeed<=0)
maxPoint  = max(|dx|, |dy|)  limitado a min(screenW, screenH)
se maxPoint < max(screenW, screenH):
      maxPoint = 100 + int((maxSide-100)/maxSide * maxPoint)
      moveTime = moveTime * maxPoint / maxSide
stepCount = maxPoint // 20
se stepCount > 1: para i em range(stepCount): SetCursorPos(cur + int(step*i)); sleep(moveTime/stepCount)
SetCursorPos(x, y); sleep(waitTime)
```
Ou seja, mesmo para distância ~0 há um piso de `maxPoint=100` ⇒ 5 passos e ≈ `1*100/maxSide` ≈ 0,04 s (em tela 2560 de largura). Trajetória linear, o último ponto é fixado pelo `SetCursorPos(x,y)` final. Deslocamento máximo teórico (diagonal grande) ≈ 1 s (`MAX_MOVE_SECOND`).
`Control.MoveCursorToInnerPos(simulateMove=True)` chama `MoveTo(x, y, waitTime=0)` se `MAX_MOVE_SECOND > 0`; com `simulateMove=False` ou `MAX_MOVE_SECOND=0` chama só `SetCursorPos`.
`DragDrop` = `PressMouse(x1,y1,0.05)` + `MoveTo(x2,y2,speed,0.05)` + `ReleaseMouse(wait)`; `ReleaseMouse` solta onde o cursor estiver.

## 11.3 `SendKeys`: o analisador (L2740)
Duas fases: **(a)** o texto vira uma lista `keys` de eventos; **(b)** a lista é executada.

Estado: `hold` (há modificador esperando teclas), `include` (dentro de `( )`), `insertIndex` (onde inserir novas teclas), `lastKeyValue`.

Fase (a), por token:
| Token | `hold=False` | `hold=True` |
|---|---|---|
| `{nome [n]}` com nome em `SpecialKeyNames` (case-insensitive) | acrescenta `[down, up]`; se `nome` ∈ `holdKeys` ⇒ `hold=True` e `insertIndex` = posição do `up` do modificador | **insere** `down,up` em `insertIndex` (ou seja, *entre* o down e o up do modificador); depois: se `include` ⇒ `insertIndex++`; senão se for outro modificador ⇒ `insertIndex++` (empilha `{Ctrl}{Shift}`), senão `hold=False` |
| `{x}` com `x` em `CharacterCodes` (**case‑sensitive**) | (cai no ramo "caractere unicode") — acrescenta `x` como Unicode | insere VK down/up em `insertIndex` |
| `{qualquer-outro}` | acrescenta como Unicode | acrescenta como Unicode **no fim** (depois de soltar o modificador) |
| `(` | literal | `include=True` |
| `)` | literal | `include=False; hold=False` |
| caractere normal | Unicode | se em `CharacterCodes` → VK inserido; senão Unicode no fim; depois `include` ? `insertIndex++` : `hold=False` |

`holdKeys` = WIN, LWIN, RWIN, SHIFT, LSHIFT, RSHIFT, CTRL, CONTROL, LCTRL, RCTRL, LCONTROL, (LCONTROL repetido), ALT, LALT, RALT. (`RCONTROL`, que existe em `SpecialKeyNames`, **não** segura.)

Resultado prático:
- `{Ctrl}a` → `Ctrl↓ A↓ A↑ Ctrl↑` (o "a" entra entre down e up do Ctrl).
- `{Ctrl}A` (maiúsculo) → também `VK_A` **sem Shift** (porque `CharacterCodes['A'] = VK_A`): é Ctrl+A, não Ctrl+Shift+A. Para Shift use `{Ctrl}{Shift}a`.
- `{Ctrl}!` → `!` não está em `CharacterCodes` ⇒ vira Unicode digitado **depois** do Ctrl soltar.
- `{Ctrl}(ab)` → Ctrl segurado durante `a` e `b`.
- `{Ctrl}{a 3}`: 1ª repetição é combinada com Ctrl; `hold` vira `False`; as 2 seguintes são Unicode normais → "Ctrl+A, depois 'aa'" (bate com o docstring).
- Maiúsculas/símbolos fora de hold sempre via Unicode (`KEYEVENTF_UNICODE`), por isso independem de layout — mas muitos apps que escutam teclas VK (jogos, atalhos) não veem Unicode como tecla.

Fase (b), execução:
- evento Unicode → `SendUnicodeChar` (par down/up por `SendInput`) + `sleep(interval)`.
- evento VK → `keybd_event(vk, scancode, flags)`, **sempre com `ExtendedKey`** (inclusive letras). O scancode vem de `_VKtoSC`: tabela `_SCKeys` (shifts, ctrls, alts, wins, numpad…) ou `MapVirtualKeyA`, com bit `0x100` para APPS/CANCEL/SNAPSHOT/DIVIDE/NUMLOCK.
- Pausas: depois de um `up` seguido de Unicode ou de outro `down` → `interval`; depois de `down` ou `up` seguido de `up` → 0,01 s fixo (`hotkeyInterval`, "senão teclas combinadas podem não ser capturadas"); no último evento → `interval`. No fim, `sleep(waitTime)`.
- Não há verificação de teclas presas: se uma exceção ocorrer no meio, um modificador pode ficar pressionado (o bloco que liberaria está comentado). `RunByHotKey` faz essa limpeza (`releaseAllKeys`) no `finally`.

Nomes aceitos em `{...}` além dos óbvios (lidos de `SpecialKeyNames`): `ENTER/RETURN`, `TAB`, `ESC/ESCAPE`, `SPACE`, `BACK` (**não existe `BACKSPACE`**), `DELETE/DEL`, `INSERT/INS`, `HOME`, `END`, `PAGEUP/PRIOR`, `PAGEDOWN/NEXT`, `LEFT/RIGHT/UP/DOWN`, `F1…F24`, `PRINTSCREEN/SNAPSHOT`, `PAUSE`, `CAPITAL` (**não existe `CAPSLOCK`**), `NUMLOCK`, `SCROLL`, `APPS` (tecla de menu de contexto), `WIN/LWIN/RWIN`, `CTRL/CONTROL/LCTRL/RCTRL`, `ALT/LALT/RALT`, `SHIFT/LSHIFT/RSHIFT`, `NUMPAD0…9`, `MULTIPLY/ADD/SUBTRACT/DECIMAL/DIVIDE`, `VOLUME_UP/DOWN/MUTE`, `MEDIA_PLAY_PAUSE/NEXT_TRACK/PREV_TRACK/STOP`, `BROWSER_BACK/FORWARD/REFRESH/STOP/SEARCH/FAVORITES/HOME`, `LAUNCH_MAIL/MEDIA_SELECT/APP1/APP2`, `OEM_1…8/OEM_PLUS/COMMA/MINUS/PERIOD/OEM_102`, `SLEEP`, `LBUTTON/RBUTTON/MBUTTON/XBUTTON1/2` (botões de mouse como VK), e os de IME (KANA, HANGUL, HANJA, KANJI, CONVERT, NONCONVERT, ACCEPT, MODECHANGE, PROCESSKEY, PACKET). `{Win}d` funciona porque `d` é inserido entre down/up de WIN.
`CharacterCodes` cobre dígitos, letras (as duas caixas), espaço e `` ` - = [ ] \ ; ' , . / `` (símbolos "com shift" estão comentados).

## 11.4 Padrões: `GetPattern` e `CreatePattern`
`GetPattern(id)`: `Element.GetCurrentPattern(id)` devolve `IUnknown`; se truthy → `CreatePattern`, que faz `QueryInterface(GetPatternIdInterface(id))` e instancia `PatternConstructors[id](pattern=iface)`. O objeto é **guardado em `_supportedPatterns[id]`** mas `GetPattern` sempre cria um novo (só `GetCachedPattern(id, cache=True)` reaproveita). `COMError` ⇒ `None`.
`GetPatternIdInterface` monta (uma vez) o dicionário id→interface a partir de `UIAutomationCore`; os padrões "novos" (Annotation, CustomNavigation, Drag, DropTarget, ObjectModel, Spreadsheet*, Styles, TextChild, TextEdit, TextPattern2, TransformPattern2) são carregados em `try/except` separados porque **não existem no Windows 7 ou anterior**; nesse caso `KeyError` ao pedir o id.
`S_OK == 0`: os métodos de ação comparam o retorno do COM com 0. Falhas de HRESULT chegam como `COMError` (não como `False`), exceto `Expand`/`Collapse` que têm `try/except` interno.

## 11.5 Captura de tela: geometria do `Bitmap.FromControl` (L3473)
1. Se o retângulo é zero, sobe para o pai até achar um com área.
2. Se o controle tem HWND: se for top‑level e DWM ativo, usa `DwmGetWindowExtendFrameBounds` (retângulo visível, sem sombra/borda invisível) no lugar de `BoundingRectangle`. `width/height <= 0` ⇒ `rect.width() + width` (assim `0` = tudo, `-10` = 10 px a menos).
3. Chama `BitmapFromWindow(hwnd_da_raiz, left, top, right, bottom, 0, 0, captureCursor)` — **sempre passando o HWND do Desktop e coordenadas de tela**. Logo a captura é uma cópia dos pixels **visíveis na tela** naquela região (janela coberta por outra sai com o que está por cima; janela minimizada/fora da tela sai vazia/preta ou errada). Isto confirma o que antes era suposição.
4. Sem HWND próprio: sobe até um ancestral com HWND, calcula o deslocamento relativo (`rect.left - pRect.left + x`) e delega a `FromHandle`, que soma o `rect` do HWND de volta e captura da raiz do mesmo jeito.

## 11.6 `GetProcesses(detailedInfo=True)` (L2994)
1. `CreateToolhelp32Snapshot(TH32CS_SNAPALL=15)` + `Process32FirstW/NextW` ⇒ pid e nome (`szExeFile`).
2. Para cada pid: `OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION | PROCESS_VM_READ)`. Se falhar (processo protegido/elevado), fica só pid+nome (`ppid=-1`, `is64Bit=None`).
3. `IsWow64Process` ⇒ `is64Bit = not isWow64` (⚠ numa máquina de 32 bits real diria "64 bits"; irrelevante no Win 64).
4. `NtQueryInformationProcess(classe 0)` ⇒ `PROCESS_BASIC_INFORMATION` (6 palavras): `[1]` = endereço do PEB, `[5]` = pid do pai.
5. Lê o PEB (712 bytes em 64‑bit / 472 em 32‑bit), `peb[4]` = `ProcessParameters`; lê `RTL_USER_PROCESS_PARAMETERS` (128/72 bytes) e, no deslocamento `16 + 10*ptrSize`, desempacota os dois `UNICODE_STRING` (`ImagePathName`, `CommandLine`) com `struct '@HHNHHN'`.
6. Lê os textos do espaço do processo alvo. Se `exePath` ficou vazio, cai para `QueryFullProcessImageNameW`.
⚠ Observação: o buffer é `c_wchar * MaximumLength`, mas `MaximumLength` é em **bytes**; o código lê `sizeof(buffer)` = 2× esse valor. Se o intervalo extra não for legível no alvo, o `ReadProcessMemory` falha e `cmdLine` fica vazio (suspeita — não verifiquei). Só funciona entre processos de mesma "bitness" para ler a PEB (32↔64 pode falhar).
`TerminateProcess(pid)`: `OpenProcess(PROCESS_TERMINATE)` + `TerminateProcess(h, -1)` (código de saída `0xFFFFFFFF`).

## 11.7 `RunByHotKey` (L10657)
- Ids: stop=1, exit=2, os do usuário a partir de 3 (na ordem do dicionário).
- Registra cada um com `RegisterHotKey(NULL, id, mod, vk)`. **Se qualquer registro de hotkey de usuário/stop falhar, a função retorna sem entrar no laço** (os já registrados só somem ao fim do processo). Falha no `exitHotKey` só imprime aviso.
- Laço `GetMessageW` no thread principal; em `WM_HOTKEY (0x0312)` compara `lParam` (low word = modificadores, high word = vk). Cada hotkey cria `threading.Thread(threadFunc)`; se a thread anterior desse hotkey ainda vive, só avisa. Há **um único `stopEvent` compartilhado**: `stopHotKey` o seta para todas as threads e as marca para `join(2)` no fim; iniciar uma função nova faz `stopEvent.clear()`.
- `threadFunc`: espera soltar as teclas (se `waitHotKeyReleased`), roda `function(stopEvent)`, captura exceções (imprime traceback) e no `finally` **solta todas as teclas VK que estiverem pressionadas** (varre `Keys.__dict__` com `IsKeyPressed`).
- Saída: `exitHotKey` (padrão Ctrl+D) ⇒ seta `stopEvent`, `join(2)` das vivas e `os._exit(0)`.

## 11.8 Threads/COM
`_AutomationClient.instance()` é um **singleton do processo** criado na primeira thread que o usar. As demais threads precisam chamar `CoInitializeEx` (`UIAutomationInitializerInThread`), mas continuam compartilhando o mesmo objeto `IUIAutomation`/`ViewWalker` criado na outra thread — o docstring manda não passar `Control`/`Pattern` entre threads. O ponto sutil é que o próprio singleton é criado por quem usar primeiro e compartilhado; o código não trata isso. Não consegui concluir só pela leitura se isso é seguro em todos os casos (depende do modelo de apartamento do COM), então a recomendação prática é manter a automação numa única thread de trabalho e criar os controles dentro dela.
`UIAutomationInitializerInThread`: `__init__` inicializa; `Uninitialize` é idempotente (flag `inited`); `__del__` também chama — usar `with` evita chamar tarde demais.

## 11.9 `LogControl` (L10504)
Escreve ControlType/ClassName/AutomationId/Rect/Name/Handle/Depth(+Pid) e consulta **os 34 patterns** (`control.GetPattern(id)` para cada um) para listar `SupportedPattern`. Depois, para cada pattern suportado, imprime valores específicos por `isinstance`: Value→`Value`, RangeValue→`Value`, Toggle→estado nomeado, SelectionItem→`IsSelected`, ExpandCollapse→estado nomeado, Scroll→percentuais H/V, Grid→Row/ColumnCount, GridItem→Row/Column, Text→`DocumentRange.GetText(30)` (com `try/except COMError` porque CEF/Chromium não dá). Nomes de estado vêm de `_GetDictKeyName(Enum.__dict__, valor)`. O texto também é gravado no arquivo de log.

## 11.10 `TextRange.GetBoundingRectangles` e coordenadas
O COM devolve uma lista plana de floats `[x, y, largura, altura, x, y, ...]` (um retângulo por linha visível); a lib converte para `Rect(int(x), int(y), int(x)+int(w), int(y)+int(h))` — trunca em vez de arredondar.

## 11.11 `Control.__getitem__` e navegação
`c[1]` = `GetFirstChild`; `c[-1]` = `GetLastChild`; `c[n>1]` anda `n-1` irmãos; `c[n<-1]` anda `-n-1` irmãos para trás a partir do último; `0` ⇒ `ValueError` sem mensagem. `GetAncestorControl(cond)` testa `cond(ancestral, depth)` com `depth` iniciando em -1.
