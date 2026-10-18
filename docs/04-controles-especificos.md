# 04 — Controles específicos (41 tipos)

Cada classe só fixa `ControlType=ControlType.XxxControl` e adiciona métodos `GetXxxPattern()` (atalhos para `GetPattern(PatternId.Xxx)`) que devolvem o pattern ou `None`. Os comentários do código indicam o que o Microsoft docs diz sobre o suporte: *Must support* (obrigatório) ou *Conditional*.

| Classe | Patterns atalho (`GetXxxPattern`) | Extras |
|---|---|---|
| `AppBarControl` | — | |
| `ButtonControl` | ExpandCollapse, Invoke, Toggle | |
| `CalendarControl` | Grid, Table, Scroll, Selection | |
| `CheckBoxControl` | Toggle | **`SetChecked(checked: bool)`** → bool |
| `ComboBoxControl` | ExpandCollapse, Selection, Value | **`Select(itemName='', condition=None, simulateMove=True, waitTime)`** |
| `CustomControl` | — | |
| `DataGridControl` | Grid, Scroll, Selection, Table | |
| `DataItemControl` | SelectionItem, ExpandCollapse, GridItem, ScrollItem, TableItem, Toggle, Value | |
| `DocumentControl` | Text, Scroll, Value | |
| `EditControl` | RangeValue, Text, Value | |
| `GroupControl` | ExpandCollapse | |
| `HeaderControl` | Transform | |
| `HeaderItemControl` | Invoke, Transform | |
| `HyperlinkControl` | Invoke, Value | |
| `ImageControl` | GridItem, TableItem | |
| `ListControl` | Grid, MultipleView, Scroll, Selection | |
| `ListItemControl` | SelectionItem, ExpandCollapse, GridItem, Invoke, ScrollItem, Toggle, Value | |
| `MenuControl` | — | |
| `MenuBarControl` | Dock, ExpandCollapse, Transform | |
| `MenuItemControl` | ExpandCollapse, Invoke, SelectionItem, Toggle | |
| `PaneControl` (+TopLevel) | Dock, Scroll, Transform | |
| `ProgressBarControl` | RangeValue, Value | |
| `RadioButtonControl` | SelectionItem | |
| `ScrollBarControl` | RangeValue | |
| `SemanticZoomControl` | — | |
| `SeparatorControl` | — | |
| `SliderControl` | RangeValue, Selection, Value | |
| `SpinnerControl` | RangeValue, Selection, Value | |
| `SplitButtonControl` | ExpandCollapse, Invoke | |
| `StatusBarControl` | Grid | |
| `TabControl` | Selection, Scroll | |
| `TabItemControl` | SelectionItem | |
| `TableControl` | Grid, GridItem, Table, TableItem | **`GetTableItemsValue(row=-1, column=-1)`** |
| `TextControl` | GridItem, TableItem, Text | |
| `ThumbControl` | Transform | |
| `TitleBarControl` | — | |
| `ToolBarControl` | Dock, ExpandCollapse, Transform | |
| `ToolTipControl` | Text, Window | |
| `TreeControl` | Scroll, Selection | |
| `TreeItemControl` | ExpandCollapse, Invoke, ScrollItem, SelectionItem, Toggle | |
| `WindowControl` (+TopLevel) | Transform, Window, Dock | `MetroClose()` |

> Os atalhos são só açúcar: nada impede chamar `ctrl.GetPattern(PatternId.InvokePattern)` em qualquer controle. **O que de fato funciona depende do app**, não da classe (ex.: no laboratório, o `SliderControl` do WinForms **não** tinha `RangeValuePattern`, só `ValuePattern`; e `ListItem` do ListView tinha Toggle porque tinha checkbox).

## Métodos especiais, em detalhe

### `CheckBoxControl.SetChecked(checked)`
Usa `TogglePattern.SetToggleState(On/Off)`; retorna o booleano de `SetToggleState` (True quando atingiu o estado). Retorna `False` se o controle não tem TogglePattern. Para checkbox tri-estado o ciclo real do `Toggle()` foi **On → Indeterminate → Off → On** (testado).

### `ComboBoxControl.Select(itemName | condition, simulateMove, waitTime)`
1. Se tem `ExpandCollapsePattern` → `Expand()`; senão (WinForms) clica 10 px dentro da borda direita (`Click(x=-10, ratioY=0.5)`).
2. Procura um `ListItemControl` **descendente do combo** por `Name=itemName` (ou `Compare=lambda c,d: condition(c.Name)`), espera 1 s.
3. Se achar: `ScrollIntoView` se houver o pattern, e **clica no item** (mouse real!).
4. Se não achar, tenta uma `ListControl(searchDepth=1)` direto sob o Desktop (popups que são filhos da raiz).
5. Se falhar, loga amarelo e recolhe o combo. Retorna bool.
> 🧪 Testado: no **WinForms** (`DropDownList` sem `ExpandCollapsePattern`) o `Select` usa o clique na borda direita e o app recebeu o evento (`'Verde'`); no **WPF** (com `ExpandCollapsePattern`) ele expande, acha o `ListItem` e clica (`'Azul'` selecionado). `Select('Roxo')` (inexistente) devolve `False`, loga em amarelo e recolhe o combo; `condition=lambda n: n.startswith('Am')` também funciona. Ele **usa o mouse**: se preferir não usar, expanda e use `SelectionItemPattern.Select()` do item (🧪 funciona no WPF).

### `TableControl.GetTableItemsValue(row=-1, column=-1)`
Monta uma matriz: para cada filho do tabela, lista `cell.GetLegacyIAccessiblePattern().Value` dos filhos. **Bug**: usa `row > 0` e `column > 0`, então a **linha/coluna 0 nunca é selecionável** (devolve a tabela inteira). Além disso exige que todos os filhos tenham LegacyIAccessible.

### `TopLevel`
Ver 03-control §3.8.

## Qual é o ControlType que o app expõe?
Não adivinhe: use `auto.EnumAndLogControl(win, maxDepth=N)` ou o Inspect.exe/“Accessibility Insights” (veja 09) e confira `ControlTypeName`, `AutomationId` e a lista de patterns. Exemplos reais observados no laboratório WinForms: `NumericUpDown` virou **ComboBox** com filhos `Spinner` + `Edit`; `LinkLabel` virou `Text` com filho `Hyperlink`; `DataGridView` virou `Table` com filhos `Custom` (linhas) → `DataItem` (células); `DateTimePicker`/`MonthCalendar`/`PictureBox` viraram `Pane` genérico com só LegacyIAccessible.

## Matriz "Obrigatório × Condicional" (extraída dos docstrings de cada `GetXxxPattern`)
`M` = o docstring diz *"Must support according to MSDN"* · `C` = *"Conditional support"*. É a regra da Microsoft para o tipo de controle, **não** garantia de que o app implementa. (Gerada lendo o código; os docstrings de `ListItem`, `Hyperlink` etc. têm algumas marcas que divergem da tabela atual da Microsoft.)

| Controle | Patterns |
|---|---|
| Button | ExpandCollapse C, Invoke C, Toggle C |
| Calendar | Grid **M**, Table **M**, Scroll C, Selection C |
| CheckBox | Toggle **M** |
| ComboBox | ExpandCollapse **M**, Selection C, Value C |
| DataGrid | Grid **M**, Scroll C, Selection C, Table C |
| DataItem | SelectionItem **M**, ExpandCollapse C, GridItem C, ScrollItem C, TableItem C, Toggle C, Value C |
| Document | Text **M**, Scroll C, Value C |
| Edit | RangeValue C, Text C, Value C |
| Group | ExpandCollapse C |
| Header | Transform C |
| HeaderItem | Invoke C, Transform C |
| Hyperlink | Invoke **M**, Value C |
| Image | GridItem C, TableItem C |
| List | Grid C, MultipleView C, Scroll C, Selection C |
| ListItem | SelectionItem **M**, ExpandCollapse C, GridItem C, Invoke C, ScrollItem C, Toggle C, Value C |
| MenuBar | Dock C, ExpandCollapse C, Transform C |
| MenuItem | ExpandCollapse C, Invoke C, SelectionItem C, Toggle C |
| Pane | Dock C, Scroll C, Transform C |
| ProgressBar | RangeValue C, Value C |
| RadioButton | SelectionItem **M** |
| ScrollBar | RangeValue C |
| Slider / Spinner | RangeValue C, Selection C, Value C |
| SplitButton | ExpandCollapse **M**, Invoke **M** |
| StatusBar | Grid C |
| Tab | Selection **M**, Scroll C |
| TabItem | SelectionItem **M** |
| Table | Grid **M**, GridItem **M**, Table **M**, TableItem **M** |
| Text | GridItem C, TableItem C, Text C |
| Thumb | Transform **M** |
| ToolBar | Dock C, ExpandCollapse C, Transform C |
| ToolTip | Text C, Window C |
| Tree | Scroll C, Selection C |
| TreeItem | ExpandCollapse **M**, Invoke C, ScrollItem C, SelectionItem C, Toggle C |
| Window | Transform **M**, Window **M**, Dock C |

Sem atalhos (nenhum `GetXxxPattern`): AppBar, Custom, Menu, SemanticZoom, Separator, TitleBar — mas `GetPattern(PatternId.X)` funciona neles.
Exemplo da divergência entre regra e realidade, vista no laboratório: o `Table` (DataGridView do WinForms) tinha **só** LegacyIAccessible, apesar de "Grid/Table/GridItem/TableItem = M".
