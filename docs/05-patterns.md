# 05 — Patterns (34)

Um *pattern* é uma capacidade ("posso ser invocado", "tenho valor", "sou expansível"). Obtenha com `ctrl.GetPattern(PatternId.XxxPattern)` (ou o atalho `GetXxxPattern()` do tipo) → objeto ou `None`. O ponteiro COM fica em `pattern.pattern`.

Legenda: 🧪 = **executado e conferido** (ver `12-relatorio-de-validacao.md`) · 📖 = só lido no código (nenhum app disponível expôs o pattern).

## Regras gerais (todas conferidas 🧪)
- Métodos de ação recebem `waitTime` (padrão 0,5 s) e dormem **depois** da chamada. Com `waitTime=0` o `Invoke` levou 2 ms; com o padrão, 0,50 s.
- Retornam `bool` (`True` quando o COM devolve `S_OK`). **Erros viram exceção `comtypes.COMError`**, não `False` — exceto `Expand`/`Collapse`, que têm `try/except` interno e devolvem `False`.
- Códigos de erro vistos: `0x80040200` (elemento desabilitado), `0x80040201` (elemento não disponível/morto), `0x80131505` (timeout do UIA), `0x80131509` (operação inválida, ex.: gravar em campo somente leitura), `0x80004001` (não implementado).
- Propriedades são "ao vivo" (`CurrentXxx`).
- Listas de controles (`GetSelection`, `GetColumnHeaders`…) devolvem `[]` se vazio.
- `GetPattern` engole `COMError` e devolve `None` → *teste sempre `if pattern:`*.
- Os atalhos `GetXxxPattern()` só existem nas **classes tipadas**. Em um `Control` genérico ou `CustomControl` (comum em `DatePicker`, células de `DataGrid` do WPF…) use `GetPattern(PatternId.XxxPattern)`.
- `GetPattern` cria um objeto **novo** a cada chamada; `GetCachedPattern(id, cache=True)` reaproveita.

## ⚠️ `Invoke` é síncrono (descoberta dos testes)
`InvokePattern.Invoke()` só retorna quando o clique **termina no aplicativo**:
- botão cujo *handler* leva 3 s → o `Invoke` levou **3,39 s**;
- botão que abre um **diálogo modal** → o `Invoke` fica **preso até o diálogo ser fechado** (voltou em 3,01 s quando o diálogo foi fechado aos 3 s);
- se ninguém fechar, ele só desiste com `COMError 0x80131505` depois de **~66 s**;
- enquanto isso, **qualquer outra chamada UIA ao mesmo programa também espera**, e uma busca a partir do Desktop trava por ~66 s (passa pela janela ocupada);
- `LegacyIAccessiblePattern.DoDefaultAction()` se comporta igual; `Click()` de mouse volta na hora (0,7 s).

Receita para botões que abrem modais: chame o `Invoke` **numa thread** e siga o fluxo.
```python
def abrir():
    with auto.UIAutomationInitializerInThread():
        win.ButtonControl(AutomationId='btnModal').GetInvokePattern().Invoke(0)
threading.Thread(target=abrir, daemon=True).start()
dlg = auto.WindowControl(searchDepth=2, Name='Título do diálogo'); dlg.Exists(5)
```
(O diálogo é uma janela filha na árvore; procure com `searchDepth=2` a partir do Desktop **só depois** de ter certeza de que não há outra janela travada.)

## Tabela
| Pattern | Membros | Verificado |
|---|---|---|
| **InvokePattern** | `Invoke(waitTime)` | 🧪 dispara o evento do app; não move o mouse; em botão desabilitado levanta `COMError 0x80040200`. |
| **TogglePattern** | `ToggleState`, `Toggle()`, `SetToggleState(state)` | 🧪 2 estados: Off→On→Off; 3 estados: Off→On→Indeterminate→Off. `SetToggleState` tenta até 6 `Toggle` e devolve `False` se o estado é inalcançável (Indeterminate num checkbox de 2 estados). |
| **ValuePattern** | `Value`, `IsReadOnly`, `SetValue(str)` | 🧪 `SetValue` dispara `TextChanged` do app; acentos ok; senha: `Value` vazio mas `SetValue` funciona; multilinha usa `\r\n`. |
| **RangeValuePattern** | `Value`, `Minimum`, `Maximum`, `SmallChange`, `LargeChange`, `IsReadOnly`, `SetValue(float)` | 🧪 Slider WPF: `(30,0,100,2,10,False)`; `SetValue(70)` ok; valor acima do máximo → `COMError`; ProgressBar é somente leitura (`SetValue` → `COMError`). **O `TrackBar` do WinForms não tem RangeValue**, só `ValuePattern` (string). |
| **SelectionItemPattern** | `Select()`, `AddToSelection()`, `RemoveFromSelection()`, `IsSelected`, `SelectionContainer` | 🧪 funciona em RadioButton, ListItem, TabItem, ComboBoxItem e item virtualizado. **Use `IsSelected` por item** para conferir a seleção. |
| **SelectionPattern** | `GetSelection()`, `CanSelectMultiple`, `IsSelectionRequired` | 🧪 ⚠ Num ListBox Win32 multisseleção `CanSelectMultiple` voltou `False` apesar de aceitar vários, e `GetSelection()` devolveu um **item antigo** quando sobrou só um selecionado. Em WPF funcionou certo (`['Verde']`). |
| **ExpandCollapsePattern** | `ExpandCollapseState`, `Expand()`, `Collapse()` | 🧪 TreeItem, Expander, ComboBox, MenuItem. Estados: `Collapsed=0, Expanded=1, PartiallyExpanded=2, LeafNode=3`. Num nó folha o estado é `3` e `Expand()` devolve `False`. |
| **ScrollPattern** | `HorizontalScrollPercent`, `VerticalScrollPercent`, `HorizontalViewSize`, `VerticalViewSize`, `HorizontallyScrollable`, `VerticallyScrollable`, `Scroll(h, v)`, `SetScrollPercent(h, v)`, `ScrollPattern.NoScrollValue = -1` | 🧪 `SetScrollPercent(-1, 50)` → 49 %; `Scroll(NoAmount, LargeIncrement)` aumenta; `SetScrollPercent(-1, 0)` volta ao topo. `ScrollAmount`: `LargeDecrement=0, SmallDecrement=1, NoAmount=2, LargeIncrement=3, SmallIncrement=4`. **`EditControl` não tem `GetScrollPattern`** (use `GetPattern`). |
| **ScrollItemPattern** | `ScrollIntoView()` | 🧪 WPF: leva "Linha 400" para dentro do ListBox. O `ListItem` do ListBox **WinForms não tem** esse pattern. |
| **WindowPattern** | `Close()`, `CanMaximize`, `CanMinimize`, `IsModal`, `IsTopmost`, `WindowInteractionState`, `WindowVisualState`, `SetWindowVisualState(state)`, `WaitForInputIdle(ms)` | 🧪 `Close()` fecha como o X; `SetWindowVisualState` Minimized/Normal/Maximized ok. ⚠ **`WaitForInputIdle` levanta `COMError 0x80004001` ("Não implementado")** em janelas WinForms e WPF. |
| **TransformPattern** | `CanMove`, `CanResize`, `CanRotate`, `Move(x,y)`, `Resize(w,h)`, `Rotate(deg)` | 🧪 `Move(120,80)` e `Resize(1000,800)` aplicados em pixels físicos; `Rotate` em janela → `COMError`; `CanRotate=False`. |
| **TransformPattern2** | `CanZoom`, `ZoomLevel`, `ZoomMaximum`, `ZoomMinimum`, `Zoom(level)`, `ZoomByUnit(ZoomUnit)` | 📖 nenhum app disponível expôs. |
| **DockPattern** | `DockPosition`, `SetDockPosition(pos)` | 📖 idem. `DockPosition`: Top=0, Left=1, Bottom=2, Right=3, Fill=4, None=5. |
| **GridPattern** | `RowCount`, `ColumnCount`, `GetItem(row, col)` | 🧪 DataGrid WPF 3×3; `GetItem(1,2)` devolve a célula "18,90" como **`CustomControl`**. Calendar: 6×7. |
| **GridItemPattern** | `Row`, `Column`, `RowSpan`, `ColumnSpan`, `ContainingGrid` | 🧪 `(1,2,1,1)` e `ContainingGrid` é o grid. |
| **TablePattern** | `RowOrColumnMajor`, `GetColumnHeaders()`, `GetRowHeaders()` | 🧪 cabeçalhos `['Produto','Estoque','Preco']`; `RowOrColumnMajor=0` (RowMajor); `GetRowHeaders()` devolve 3 itens de nome vazio. |
| **TableItemPattern** | `GetColumnHeaderItems()`, `GetRowHeaderItems()` | 🧪 célula (1,2) → `['Preco']`. |
| **TextPattern** | `DocumentRange`, `SupportedTextSelection`, `GetSelection()`, `GetVisibleRanges()`, `RangeFromPoint(x,y)`, `RangeFromChild(child)` | 🧪 `DocumentRange.GetText(-1)` traz tudo; `GetText(5)` limita. ⚠ `SupportedTextSelection` vira `bool` (perde a diferença entre *única* e *múltipla*). ⚠ **`RangeFromChild` falha** (`ArgumentError`: passa a *property* da classe). O TextBox WinForms multilinha **não** expôs TextPattern; WPF `TextBox`/`RichTextBox`/`Document` sim. |
| **TextRange** (objeto devolvido) | `GetText(maxLength=-1)`, `Clone()`, `Compare(r)`, `CompareEndpoints(...)`, `ExpandToEnclosingUnit(TextUnit)`, `FindText(text, backward, ignoreCase)`, `FindAttribute(attrId, val, backward)`, `GetAttributeValue(attrId)`, `GetBoundingRectangles()`, `GetChildren()`, `GetEnclosingControl()`, `Move(unit,count)`, `MoveEndpointByUnit(endpoint, unit, count)`, `MoveEndpointByRange(...)`, `Select()`, `AddToSelection()`, `RemoveFromSelection()`, `ScrollIntoView(alignTop)` | 🧪 `FindText` (maiúsc/minúsc, `backward`, `None` se não acha); `Select()` + `GetSelection()`; `Compare`; `ExpandToEnclosingUnit` (Word → `'ALVO'`, Paragraph → o parágrafo); `Move(Word,1)` → `1`; `MoveEndpointByUnit`; `MoveEndpointByRange`; `GetBoundingRectangles()` → `[Rect]`; `GetAttributeValue(FontWeight)` **700** (negrito) e **400** (normal); `IsItalic` `True`; `FontSize` em pontos (`15.0` para fonte de 20 px); `FindAttribute(FontWeight,700)` acha o trecho em negrito; `ScrollIntoView`. ⚠ `CompareEndpoints` com o wrapper **falha** (`ArgumentError`); funciona em `r.textRange.CompareEndpoints(src, outro.textRange, tgt)`. ⚠ `AddToSelection`/`RemoveFromSelection` → `COMError` (WPF não suporta seleção disjunta). `TextUnit`: Character=0, Format=1, Word=2, Line=3, Paragraph=4, Page=5, Document=6. `TextPatternRangeEndpoint`: Start=0, End=1. Cor de texto (`ForegroundColor`) vermelha veio como `0xFF0000`. |
| **TextPattern2** | (vazio) | 🧪 só marcador: o wrapper da lib não tem membros (`['pattern']`). Existe junto com TextEdit em caixas de texto modernas. |
| **TextEditPattern** | `GetActiveComposition()`, `GetConversionTarget()` | 🧪 ambos devolvem `None` sem composição de IME ativa. |
| **TextChildPattern** | `TextContainer`, `TextRange` | 📖 |
| **LegacyIAccessiblePattern** | `Name`, `Value`, `Role`, `State`, `Description`, `Help`, `KeyboardShortcut`, `DefaultAction`, `ChildId`, `DoDefaultAction()`, `Select(AccessibleSelection)`, `SetValue(str)`, `GetSelection()`, `GetIAccessible()` | 🧪 botão: `Name='Clicar'`, `Role=43` (`PushButton`), `DefaultAction='Pressionar'`; `DoDefaultAction` dispara o clique; `SetValue` escreve no campo; `Select(TakeSelection/AddSelection/RemoveSelection)` funcionam; `GetIAccessible()` devolve `POINTER(IAccessible)`. `State` é bitmask `AccessibleState`. |
| **MultipleViewPattern** | `CurrentView`, `GetSupportedViews()`, `GetViewName(view)`, `SetView(view)` | 🧪 Calendar WPF: visões `[0,1,2]` = `['Mês','Ano','Década']`; `SetView(1)` muda. |
| **ItemContainerPattern** | `FindItemByProperty(startAfterControl, propertyId, value)` | 🧪 acha "Linha 400" numa lista virtualizada **sem rolar** quando recebe um `Control` inicial. ⚠ **Passar `None` falha** (`AttributeError`): a lib sempre chama `control.Element`. |
| **VirtualizedItemPattern** | `Realize()` | 🧪 materializa o item; depois `ScrollIntoView` e `Select` funcionam. |
| **SynchronizedInputPattern** | `StartListening()`, `Cancel()` | 🧪 existe em todos os controles WPF. ⚠ **`StartListening()` quebra** (`TypeError: required argument 'inputType' missing`); `Cancel()` funciona. |
| **DragPattern** | `DropEffect`, `DropEffects`, `IsGrabbed`, `GetGrabbedItems()` | 🧪 leitura em botões da barra de tarefas: `IsGrabbed`, `DropEffect=''`, `DropEffects=()`, `GetGrabbedItems()` devolve lista de controles. |
| **DropTargetPattern** | `DropTargetEffect`, `DropTargetEffects` | 🧪 leitura: `('', ())`. |
| **AnnotationPattern** | `AnnotationTypeId`, `AnnotationTypeName`, `Author`, `DateTime`, `Target` | 📖 |
| **CustomNavigationPattern** | `Navigate(NavigateDirection)` | 📖 |
| **ObjectModelPattern** | `GetUnderlyingObjectModel()` | 📖 |
| **SpreadsheetPattern** | `GetItemByName(name)` | 📖 (Excel) |
| **SpreadsheetItemPattern** | `Formula`, `GetAnnotationObjects()`, `GetAnnotationTypes()` | 📖 |
| **StylesPattern** | `ExtendedProperties`, `FillColor`, `FillPatternColor`, `Shape`, `StyleId`, `StyleName` | 📖 |

### Cobertura por tecnologia (o que cada UI expôs de verdade)
- **WinForms** (Win32 via proxy MSAA): Invoke, Toggle, Value, SelectionItem/Selection, ExpandCollapse (TreeItem), Scroll (TextBox, ScrollBar), RangeValue (só ScrollBar/ProgressBar), Window, Transform, LegacyIAccessible. Quase nada além disso.
- **WPF**: tudo acima **mais** Text, Grid, Table, GridItem/TableItem, ItemContainer, VirtualizedItem, MultipleView, SynchronizedInput (em todo controle), ScrollItem, RangeValue (Slider).
- **Janelas modernas (WinUI/Paint)**: `TextPattern2` e `TextEditPattern` em caixas de texto.
- Nunca vistos: ver a lista de 📖 acima.

## Prioridade prática ao automatizar
1. `InvokePattern` / `TogglePattern` / `ValuePattern` / `SelectionItemPattern` / `ExpandCollapsePattern` — **não movem o mouse, não exigem foco** e são rápidos. Atenção ao `Invoke` com modais (acima).
2. `LegacyIAccessiblePattern` — quando o app só expõe MSAA.
3. Mouse / `SendKeys` — último recurso.

## Ler propriedades sem criar controle
`ctrl.GetPropertyValue(PropertyId.XxxProperty)` — 173 ids em `PropertyId` (veja 02). 🧪 `BoundingRectangleProperty` devolve a tupla de floats `(left, top, largura, altura)`. Muitos ids devolvem ponteiros COM sem conteúdo útil.
