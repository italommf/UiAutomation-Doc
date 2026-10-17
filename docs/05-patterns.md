# 05 — Patterns (34)

Um *pattern* é uma capacidade ("posso ser invocado", "tenho valor", "sou expansível"). Obtenha com `ctrl.GetPattern(PatternId.XxxPattern)` (ou o atalho `GetXxxPattern()` do tipo) → objeto ou `None`. O ponteiro COM fica em `pattern.pattern`.

**Regras gerais do código**
- Métodos de ação recebem `waitTime` (padrão 0.5 s) e dormem **depois** da chamada.
- Retornam `bool` = `(chamada COM == S_OK)`. Na prática, retorna `True` e **erros viram exceção `comtypes.COMError`** (não `False`) — exceto `Expand`/`Collapse`, que envolvem `try/except` e devolvem `False`.
- Propriedades são "ao vivo" (`CurrentXxx`).
- Listas de controles (`GetSelection`, `GetColumnHeaders`…) são montadas por `eleArray.Length/GetElement(i)`; devolvem `[]` se vazio.
- `GetPattern` engole `COMError` e devolve `None` → *teste sempre `if pattern:`*.

Legenda: ✔ = comportamento confirmado no laboratório WinForms; 📖 = só lido no código.

| Pattern | Membros | Notas |
|---|---|---|
| **InvokePattern** | `Invoke(waitTime)` | ✔ clica sem mouse (botão). Dispara o evento do app. |
| **TogglePattern** | `ToggleState`, `Toggle(waitTime)`, `SetToggleState(state, waitTime)` | ✔ `SetToggleState` repete `Toggle` até 6 vezes até chegar ao estado; retorna False se não chegar. Valores: `ToggleState.Off=0, On=1, Indeterminate=2`. |
| **ValuePattern** | `Value`, `IsReadOnly`, `SetValue(str, waitTime)` | ✔ `SetValue` dispara os eventos de mudança (o `TextChanged` do app rodou). Texto com acentos OK. Campo de senha: `Value` volta `''` (não vaza). |
| **RangeValuePattern** | `Value`, `Minimum`, `Maximum`, `SmallChange`, `LargeChange`, `IsReadOnly`, `SetValue(float)` | ✔ ProgressBar: leitura OK (45.0, 0.0, 100.0), `SetValue` levantou `COMError` (somente leitura). |
| **SelectionItemPattern** | `Select()`, `AddToSelection()`, `RemoveFromSelection()`, `IsSelected`, `SelectionContainer` | ✔ RadioButton/ListItem/TabItem. `SelectionContainer` pode ser `None` mesmo assim. |
| **SelectionPattern** | `GetSelection()`, `CanSelectMultiple`, `IsSelectionRequired` | ✔ lista os controles selecionados. ⚠ `CanSelectMultiple` voltou `False` num ListBox `MultiExtended` do WinForms, mas `Select`+`AddToSelection` selecionaram 2 itens: **a propriedade pode mentir** (proxy MSAA). |
| **ExpandCollapsePattern** | `ExpandCollapseState`, `Expand()`, `Collapse()` | ✔ TreeItem. Estados: `Collapsed=0, Expanded=1, PartiallyExpanded=2, LeafNode=3`. |
| **ScrollPattern** | `HorizontalScrollPercent`, `VerticalScrollPercent`, `HorizontalViewSize`, `VerticalViewSize`, `HorizontallyScrollable`, `VerticallyScrollable`, `Scroll(h, v)`, `SetScrollPercent(h, v)`, `ScrollPattern.NoScrollValue = -1` | 📖 `Scroll` usa `ScrollAmount` (`LargeDecrement=0, SmallDecrement=1, NoAmount=2, LargeIncrement=3, SmallIncrement=4`). `SetScrollPercent` aceita 0–100 ou -1 (não rolar nesse eixo). |
| **ScrollItemPattern** | `ScrollIntoView()` | 📖 |
| **WindowPattern** | `Close()`, `CanMaximize`, `CanMinimize`, `IsModal`, `IsTopmost`, `WindowInteractionState`, `WindowVisualState`, `SetWindowVisualState(state)`, `WaitForInputIdle(ms)` | ✔ `Close()` fechou a janela de teste (equivale a clicar no X, não mata processo). `WindowVisualState`: `Normal=0, Maximized=1, Minimized=2`. `WindowInteractionState`: `Running=0, Closing=1, ReadyForUserInteraction=2, BlockedByModalWindow=3, NotResponding=4` (lab retornou 2). |
| **TransformPattern** | `CanMove`, `CanResize`, `CanRotate`, `Move(x,y)`, `Resize(w,h)`, `Rotate(deg)` | ✔ propriedades; ações 📖 |
| **TransformPattern2** | `CanZoom`, `ZoomLevel`, `ZoomMaximum`, `ZoomMinimum`, `Zoom(level)`, `ZoomByUnit(ZoomUnit)` | 📖 |
| **DockPattern** | `DockPosition`, `SetDockPosition(pos)` | 📖 `DockPosition`: Top=0, Left=1, Bottom=2, Right=3, Fill=4, None=5 |
| **GridPattern** | `RowCount`, `ColumnCount`, `GetItem(row, col)` | 📖 |
| **GridItemPattern** | `Row`, `Column`, `RowSpan`, `ColumnSpan`, `ContainingGrid` | 📖 |
| **TablePattern** | `RowOrColumnMajor`, `GetColumnHeaders()`, `GetRowHeaders()` | 📖 |
| **TableItemPattern** | `GetColumnHeaderItems()`, `GetRowHeaderItems()` | 📖 |
| **TextPattern** | `DocumentRange`→`TextRange`, `SupportedTextSelection`, `GetSelection()`, `GetVisibleRanges()`, `RangeFromPoint(x,y)`, `RangeFromChild(child)` | ⚠ `RangeFromChild` está bugado (veja 08). O TextPattern do app Win32 multiline do lab **não existiu**; apps com RichEdit (Bloco de Notas novo, Word) expõem. |
| **TextRange** (objeto devolvido) | `GetText(maxLength=-1)`, `Clone()`, `Compare(r)`, `CompareEndpoints(...)`, `ExpandToEnclosingUnit(TextUnit)`, `FindText(text, backward, ignoreCase)`, `FindAttribute(attrId, val, backward)`, `GetAttributeValue(attrId)`, `GetBoundingRectangles()`→`[Rect]`, `GetChildren()`, `GetEnclosingControl()`, `Move(unit,count)`, `MoveEndpointByUnit(endpoint, unit, count)`, `MoveEndpointByRange(...)`, `Select()`, `AddToSelection()`, `RemoveFromSelection()`, `ScrollIntoView(alignTop)` | 📖 `GetText(-1)` pega tudo. `TextUnit`: Character=0, Format=1, Word=2, Line=3, Paragraph=4, Page=5, Document=6. `TextPatternRangeEndpoint`: Start=0, End=1. |
| **TextPattern2** | (vazio) | 📖 só marcador |
| **TextChildPattern** | `TextContainer`, `TextRange` | 📖 |
| **TextEditPattern** | `GetActiveComposition()`, `GetConversionTarget()` | 📖 (IME) |
| **LegacyIAccessiblePattern** | `Name`, `Value`, `Role`, `State`, `Description`, `Help`, `KeyboardShortcut`, `DefaultAction`, `ChildId`, `DoDefaultAction()`, `Select(AccessibleSelection)`, `SetValue(str)`, `GetSelection()`, `GetIAccessible()` | ✔ quase todo controle Win32 tem. Útil como *fallback* quando o pattern moderno não existe. `Role`→`AccessibleRole`, `State`→bitmask `AccessibleState`. |
| **MultipleViewPattern** | `CurrentView`, `GetSupportedViews()`, `GetViewName(view)`, `SetView(view)` | 📖 (ListView: ícones/detalhes) |
| **ItemContainerPattern** | `FindItemByProperty(startAfterControl, propertyId, value)` | 📖 acha item em lista virtualizada sem realizar tudo |
| **VirtualizedItemPattern** | `Realize()` | 📖 materializa item virtualizado |
| **SynchronizedInputPattern** | `StartListening()`, `Cancel()` | 📖 |
| **AnnotationPattern** | `AnnotationTypeId`, `AnnotationTypeName`, `Author`, `DateTime`, `Target` | 📖 |
| **DragPattern** | `DropEffect`, `DropEffects`, `IsGrabbed`, `GetGrabbedItems()` | 📖 (`DropEffects` "todo SAFEARRAY") |
| **DropTargetPattern** | `DropTargetEffect`, `DropTargetEffects` | 📖 |
| **CustomNavigationPattern** | `Navigate(NavigateDirection)` | 📖 |
| **ObjectModelPattern** | `GetUnderlyingObjectModel()` | 📖 |
| **SpreadsheetPattern** | `GetItemByName(name)` | 📖 (Excel) |
| **SpreadsheetItemPattern** | `Formula`, `GetAnnotationObjects()`, `GetAnnotationTypes()` | 📖 |
| **StylesPattern** | `ExtendedProperties`, `FillColor`, `FillPatternColor`, `Shape`, `StyleId`, `StyleName` | 📖 |

## Prioridade prática ao automatizar
1. `InvokePattern` / `TogglePattern` / `ValuePattern` / `SelectionItemPattern` / `ExpandCollapsePattern` — **não usam mouse nem exigem foco**, são rápidos e funcionam com a janela em segundo plano.
2. `LegacyIAccessiblePattern` — quando o app só expõe MSAA (`DoDefaultAction`, `SetValue`, `Value`).
3. Clique de mouse / `SendKeys` — último recurso (dependem de foco, posição, monitor, DPI).

## Ler propriedades sem criar controle
`ctrl.GetPropertyValue(PropertyId.XxxProperty)` — há 173 ids em `PropertyId` (veja 02). Muitos retornam ponteiros COM sem conteúdo útil; os confiáveis são os que têm tipos simples (Name, ClassName, IsEnabled, BoundingRectangle como tupla de floats `(left, top, width, height)`, etc.).
