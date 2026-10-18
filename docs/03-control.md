# 03 — A classe `Control` (L6369)

Base de tudo. Embrulha um `IUIAutomationElement`. Tem 128 membros: ~41 fábricas de filhos, 27 propriedades de elemento e ~60 métodos.

## 3.1 Construtor e critérios de busca
```python
Control(searchFromControl=None, searchDepth=0xFFFFFFFF, searchInterval=SEARCH_INTERVAL,
        foundIndex=1, element=None, ControlType=None, Name=None, SubName=None,
        RegexName=None, ClassName=None, AutomationId=None, Depth=None, Compare=None, **searchProperties)
```
| Parâmetro | Significado |
|---|---|
| `searchFromControl` | Onde começar. `None` = raiz (Desktop). Nas fábricas (`w.ButtonControl(...)`) é o próprio `w`. |
| `searchDepth` | Profundidade máxima a partir do ponto de partida (1 = só filhos diretos). |
| `searchInterval` | Pausa entre tentativas (s). |
| `foundIndex` | Qual ocorrência (1-based). `foundIndex=2` = o 2º que casar. |
| `element` | Interno: elemento COM já resolvido. |
| `ControlType` | Valor de `ControlType.XxxControl` (as subclasses já passam o seu). |
| `Name` | Igualdade exata. |
| `SubName` | `SubName in control.Name` (contém). |
| `RegexName` | `re.match` (**ancorado no início**; para "contém" use `.*padrão`). O docstring diz "só um entre Name/SubName/RegexName", mas a lib **não impede** combinar: valem todos, em AND 🧪. |
| `ClassName` | Igualdade exata com a classe Win32/framework. |
| `AutomationId` | Igualdade exata. |
| `Depth` | Só aceita controles **exatamente** nessa profundidade relativa (e define `searchDepth` = Depth). |
| `Compare` | `lambda control, depth: bool` — roda por último, após os outros critérios. |
| `**searchProperties` | Aceita qualquer chave, mas **só para o log de depuração** (chave desconhecida é ignorada na comparação — veja Pegadinhas). |

**Como a comparação funciona** (`_CompareFunction`, L7061): percorre `searchProperties` e retorna False no primeiro critério que não bate; `Compare` é aplicado por último. Os critérios são AND. Pelo código a ordem é a do dicionário; custo é percorrer a árvore em largura/profundidade via `WalkControl` (profundidade primeiro, **pré-ordem**).

**Custo:** cada nó visitado dispara chamadas COM (ClassName, Name, AutomationId…). Prefira `AutomationId`/`ClassName` com `searchDepth` baixo ou comece de um ancestral próximo.

### Métodos de gestão de critérios
| Método | Efeito |
|---|---|
| `SetSearchFromControl(c)` | muda o ponto de partida |
| `SetSearchDepth(n)` | muda a profundidade |
| `AddSearchProperties(**kw)` | `dict.update`; trata `Depth` e `RegexName` |
| `RemoveSearchProperties(**kw)` | remove chaves (os valores passados são ignorados; só as chaves importam) |
| `GetSearchPropertiesStr()` | `"{Name: 'Clicar', ControlType: ButtonControl}"` |
| `GetColorfulSearchPropertiesStr(keyColor, valueColor)` | versão com marcas `<Color=...>` p/ `Logger.ColorfullyLog` |
| `Control.ValidKeys` | `{'ControlType','ClassName','AutomationId','Name','SubName','RegexName','Depth','Compare'}` |

## 3.2 Existência, espera e re-busca
| Método | Retorno | Detalhe |
|---|---|---|
| `Exists(maxSearchSeconds=5, searchIntervalSeconds=0.5, printIfNotExist=False)` | bool | Procura repetidamente. Substitui o `_element`. Para controle de elemento direto só verifica se ainda tem pai. Sem critérios → `LookupError("control's searchProperties must not be empty!")`. Se o `searchFromControl` não existir, falha rápido. |
| `Disappears(maxSearchSeconds=5, searchIntervalSeconds=0.5, printIfNotDisappear=False)` | bool | True quando deixa de existir. |
| `Refind(maxSearchSeconds=10, searchIntervalSeconds=0.5, raiseException=True)` | bool | `Exists` que levanta `LookupError('Find Control Timeout(Ns): {...}')` (e loga em vermelho). |
| `WaitForExist(c, timeout)` / `WaitForDisappear(c, timeout)` | bool | Atalhos módulo-nível (intervalo fixo de 1 s). |

Medidas reais: `Exists(1.2, 0.3)` de algo inexistente demorou ~1.5 s (checa depois de dormir, então estoura o prazo em até 1 intervalo); `Exists(0,0)` ~0.3 s (uma varredura completa da janela do lab).

## 3.3 Propriedades do elemento (somente leitura)
Todas chamam `Element.CurrentXxx` ao vivo (sem cache).

| Propriedade | Tipo | Observação |
|---|---|---|
| `Name` | str | `''` se None |
| `AutomationId` | str | no WinForms = `Control.Name` |
| `ClassName` | str | |
| `ControlType` / `ControlTypeName` | int / str | `ControlTypeName` ex.: `'ButtonControl'` |
| `LocalizedControlType` | str | traduzido (`'janela'`) |
| `BoundingRectangle` | `Rect` | coordenadas de tela; (0,0,0,0) se invisível |
| `NativeWindowHandle` | int | `0` se não tem HWND (ou erro COM) |
| `ProcessId` | int | |
| `FrameworkId` | str | `'Win32'` (Bloco de Notas), `'WinForm'` (apps WinForms 🧪), `'WPF'`, `'XAML'`, `'Chrome'`… |
| `IsEnabled`, `IsOffscreen`, `IsKeyboardFocusable`, `HasKeyboardFocus` | bool | |
| `IsContentElement`, `IsControlElement` | bool | |
| `IsPassword` | bool | campo de senha |
| `IsRequiredForForm`, `IsDataValidForForm` | bool | |
| `AcceleratorKey`, `AccessKey`, `HelpText`, `ItemStatus`, `ItemType` | str | |
| `AriaProperties`, `AriaRole` | str | web |
| `Culture` | int | LCID |
| `Orientation` | int | `OrientationType` |
| `ProviderDescription` | str | quem fornece a árvore (proxy MSAA, etc.) |
| `Element` | ponteiro COM | faz a busca lazy se necessário |

Não expostas (comentadas no código): `ControllerFor`, `DescribedBy`, `FlowsTo`, `LabeledBy`, todas as `CachedXxx`, `FindAll/FindFirst`, `BuildUpdatedCache`. Para elas use `GetPropertyValue(PropertyId.XxxProperty)` ou `control.Element.CurrentXxx`.

### Métodos de baixo nível
| Método | Descrição |
|---|---|
| `GetPropertyValue(propertyId)` | `Element.GetCurrentPropertyValue`. Retorna tipo conforme a propriedade (muitas devolvem ponteiros COM vazios/`IUnknown`). |
| `GetPropertyValueEx(propertyId, ignoreDefault)` | idem, com opção de ignorar o default |
| `GetClickablePoint()` | `(x, y, gotClickable)` 🧪 — numa janela visível devolveu um ponto válido `(x, y, True)`; numa janela coberta/sem ponto clicável pode vir `(0, 0, False)` |
| `GetRuntimeId()` | tupla de ints (ex.: `(42, 330406)`); identifica o elemento enquanto vive |
| `GetPattern(patternId)` | cria um **novo** pattern ou `None` (engole `COMError`) |
| `GetPatternAs(patternId, riid)` | `GetCurrentPatternAs` (marcado "todo") |
| `GetCachedPattern(patternId, cache)` | com `cache=True` reaproveita de `_supportedPatterns` |
| `GetLegacyIAccessiblePattern()` | atalho para o pattern MSAA |
| `SetFocus()` | bool; `False` se erro COM |

## 3.4 Navegação na árvore (Raw View)
| Método | Retorno |
|---|---|
| `GetParentControl()` | pai ou `None` (raiz) |
| `GetFirstChildControl()`, `GetLastChildControl()` | filho ou `None` |
| `GetNextSiblingControl()`, `GetPreviousSiblingControl()` | irmão ou `None` |
| `GetChildren()` | lista de todos os filhos diretos |
| `GetSiblingControl(condition, forward=True)` | procura irmão por predicado; `forward=False` olha primeiro os **anteriores** (do mais próximo) e depois os seguintes |
| `GetAncestorControl(condition)` | sobe pai a pai; `condition(control, depth)` com `depth` -1, -2, … |
| `control[n]` | `n>=1` n‑ésimo filho (1-based); `-1` último; `-2` penúltimo…; `0` → `ValueError`; fora do range → `None` |
| `IsTopLevel()`, `GetTopLevelControl()` | usa `GetAncestor(hwnd, GAFlag.Root)`; sem HWND sobe os pais até achar um |
| `CreateControlFromControl(c)`, `Control.CreateControlFromElement(e)` | cópia / conversão para a subclasse correta |

Funções de módulo relacionadas: `GetRootControl()`, `GetFocusedControl()`, `GetForegroundControl()`, `GetConsoleWindow()`, `ControlFromPoint(x,y)`, `ControlFromPoint2(x,y)` (via HWND), `ControlFromCursor()`, `ControlFromCursor2()`, `ControlFromHandle(hwnd)`, `ControlsAreSame(a,b)`, `WalkControl`, `WalkTree`, `FindControl`.

`WalkControl(control, includeTop=False, maxDepth=0xFFFFFFFF)` gera `(control, depth)` em **pré-ordem sem recursão**. ⚠️ Com `maxDepth<=0` ele ainda devolve o topo se `includeTop=True` (o `return` vem depois do `yield`).
`FindControl(control, compare, maxDepth, findFromSelf=False, foundIndex=1)` marca `traverseCount` no resultado (nº de nós visitados).
`WalkTree(top, getChildren | getFirstChild+getNextSibling, yieldCondition, includeTop, maxDepth)` é o percorredor genérico (funciona com qualquer árvore: pastas, dicts…); com `getChildren` gera `(nó, profundidade, restantes_no_nível)`, com first/next gera `(nó, profundidade)`.

## 3.5 Ações de mouse (coordenadas relativas ao controle)
Todas retornam `None`, usam `MoveCursorToInnerPos` e não fazem nada (apenas logam em amarelo) se a largura ou altura do `BoundingRectangle` for 0.

Convenção de `x`, `y`: `>=0` offset a partir de left/top; **negativo** = offset a partir de right/bottom (`Click(-10,-10)` = 10px dentro do canto inferior direito); se informados ignoram `ratioX/ratioY` (padrão 0.5 = centro).

| Método | Nota |
|---|---|
| `Click(x,y,ratioX,ratioY,simulateMove=True,waitTime)` | move (animado) e clica |
| `RightClick`, `MiddleClick`, `DoubleClick` | `DoubleClick` espera `GetDoubleClickTime()/2000` s entre cliques |
| `DragDrop(x1,y1,x2,y2,moveSpeed,waitTime)` / `RightDragDrop` | coordenadas relativas ao controle |
| `WheelDown/WheelUp(x,y,ratioX,ratioY,wheelTimes=1,interval=0.05,waitTime)` | dá `SetFocus`, move o cursor e **restaura a posição original** do mouse depois |
| `MoveCursorToInnerPos(...)`, `MoveCursorToMyCenter(simulateMove)` | retornam `(x,y)` ou `None` |
| `GetPosition(ratioX, ratioY)` | só calcula `(x,y)` sem mover |

`simulateMove=False` (ou `MAX_MOVE_SECOND=0`) usa `SetCursorPos` direto, muito mais rápido.

## 3.6 Teclado no controle
`control.SendKey(key, waitTime)` e `control.SendKeys(text, interval=0.01, waitTime, charMode=True)` fazem `SetFocus()` e depois chamam a função global. Para muitos controles o foco só vem com um clique antes. Veja a sintaxe completa de `SendKeys` em `06-funcoes-win32.md`.

## 3.7 Janela nativa a partir do controle
| Método | Descrição |
|---|---|
| `ShowWindow(cmdShow, waitTime)` | procura o HWND no controle **ou nos ancestrais**; `None` se não achar HWND. ⚠ O `bool` é o retorno do Win32: **`True` = a janela estava visível antes**, não "sucesso" 🧪 (`Show` depois de `Hide` devolve `False` mesmo tendo reaparecido) |
| `Show()`, `Hide()` | `SW.Show` / `SW.Hide` |
| `MoveWindow(x,y,w,h,repaint=True)` | só se o controle tem HWND próprio |
| `GetWindowText()`, `SetWindowText(text)` | idem |
| `GetPixelColor(x,y)` | BGR via GDI `GetPixel` (None sem HWND) |
| `ToBitmap(x,y,w,h,captureCursor)`, `CaptureToImage(path,...)` | captura (veja 07). `w/h<=0` → tamanho do controle + w/h |

## 3.8 Mixin `TopLevel` (em `WindowControl` e `PaneControl`)
`SetTopmost(isTopmost=True)`, `IsTopmost()`, `SwitchToThisWindow()`, `Maximize()`, `IsMaximize()`, `Minimize()`, `IsMinimize()`, `Restore()`, `MoveToCenter()`, `SetActive()`.
Todos checam `IsTopLevel()` primeiro e retornam `False` se o controle não for top-level. `SetActive` restaura se minimizada, mostra se oculta e chama `SetForegroundWindow` (**pode falhar** se o processo em primeiro plano não for o do Python — restrição do Windows). `MoveToCenter` usa `GetScreenSize()` (monitor primário). Os retornos de `Maximize/Minimize/Restore` seguem a regra do `ShowWindow` acima 🧪.
`WindowControl.MetroClose()` só para janelas Metro do Windows 8.

## 3.9 Fábricas de filhos
`control.ButtonControl(searchDepth, searchInterval, foundIndex, element, Name, SubName, RegexName, ClassName, AutomationId, Depth, Compare, **kw)` — 41 métodos idênticos (um por tipo + `Control`), todos criam o tipo correspondente com `searchFromControl=self`. São a forma idiomática: `win.EditControl(AutomationId="txtNome")`.
