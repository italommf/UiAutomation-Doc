# 09 — Dicas, truques e receitas

🧪 = a mesma chamada foi exercitada no laboratório; as demais são montadas a partir das assinaturas lidas no código (revise antes de usar em produção).

## 9.1 Esqueleto recomendado
```python
import uiautomation as auto

auto.Logger.SetLogFile('')            # não gravar @AutomationLog.txt (evita vazar conteúdo de telas)
auto.SetGlobalSearchTimeout(5)        # timeout de acesso a propriedade/Refind (padrão 10 s)

win = auto.WindowControl(searchDepth=1, Name='Título da janela')   # searchDepth=1: só janelas de topo (rápido)
if not win.Exists(10, 0.5):
    raise RuntimeError('janela não apareceu')
```

## 9.2 Regras de ouro de performance e robustez
1. **Sempre limite a busca:** `searchDepth=1` para janelas de topo; comece de um ancestral já encontrado (`win.EditControl(...)`), nunca do Desktop inteiro.
2. **Critério mais estável primeiro:** `AutomationId` > `ClassName`+`Name` > `Name` > `SubName/RegexName` > `Compare`. `Name` muda com idioma/versão.
3. **Guarde o controle encontrado** em variável e reutilize; recriar a busca refaz a varredura.
4. **Patterns antes de mouse/teclado** (rápido, invisível, funciona em segundo plano). Teste `if p:`.
5. **Espere por estado, não por tempo:** `ctrl.Exists(timeout)`, `Disappears`, ou laço com `IsEnabled`/valor — em vez de `time.sleep`.
6. **Zere os `waitTime`** (`Invoke(waitTime=0)`, `SetValue(v, 0)`) quando for encadear ações e você mesmo esperar a condição (os defaults de 0,5 s somam rápido).
7. **Desligue a animação do mouse** se precisar clicar muito: `auto.uiautomation.MAX_MOVE_SECOND = 0` (lido em runtime) ou `simulateMove=False` em cada `Click`.
8. **Cuidado com mouse/teclado reais** em máquina em uso: confirme que a janela é a do foco antes de `SendKeys`:
   ```python
   if auto.GetForegroundWindow() != win.NativeWindowHandle:
       win.SetActive()
   assert auto.GetForegroundWindow() == win.NativeWindowHandle
   ```
9. **Janela alvo certa:** busque por `ClassName` + `ProcessId` quando houver mais de uma instância (um `Name` igual pode pertencer a outro processo). Ex.: `Compare=lambda c,d: c.ProcessId == pid`.

## 9.3 Receitas
### Clicar sem mouse 🧪
```python
btn = win.ButtonControl(AutomationId='btnClick')
btn.GetInvokePattern().Invoke(waitTime=0)
```
Se não tiver `InvokePattern` tente `btn.GetLegacyIAccessiblePattern().DoDefaultAction()` e, por último, `btn.Click()`.

### Preencher texto 🧪
```python
edit = win.EditControl(AutomationId='txtNome')
edit.GetValuePattern().SetValue('Olá çãõ', 0)      # dispara TextChanged
print(edit.GetValuePattern().Value)
```
Fallback quando não há ValuePattern: `edit.Click(); auto.SendKeys('{Ctrl}a{Delete}texto')`.

### Marcar/desmarcar 🧪
```python
chk = win.CheckBoxControl(AutomationId='chkAceito')
chk.SetChecked(True)                               # ou chk.GetTogglePattern().SetToggleState(auto.ToggleState.On)
radio = win.RadioButtonControl(AutomationId='rdB'); radio.GetSelectionItemPattern().Select()
```

### Escolher item de lista/combos 🧪 (lista) / 📖 (combo)
```python
lst = win.ListControl(AutomationId='lstItens')
lst.ListItemControl(Name='Item 3').GetSelectionItemPattern().Select()
sel = [c.Name for c in lst.GetSelectionPattern().GetSelection()]
# combo: combo.Select(itemName='Verde')   # usa mouse; ou ExpandCollapse + SelectionItem do item
```

### Abas e árvores 🧪 / menus 📖 (o `Invoke` do menu não foi executado)
```python
win.TabControl().TabItemControl(Name='Aba Dois').GetSelectionItemPattern().Select()
tree_item = win.TreeItemControl(Name='Raiz A'); tree_item.GetExpandCollapsePattern().Expand(0)
win.MenuItemControl(Name='Arquivo').GetInvokePattern().Invoke()      # abre o menu (WinForms)
win.MenuItemControl(Name='Novo').GetInvokePattern().Invoke()
```

### Ler uma tabela/grade 🧪 (estrutura) 
O `DataGridView` do lab ficou assim: `Table → Custom("Linha N") → DataItem("Coluna Linha N")`.
```python
grid = win.TableControl(AutomationId='dgvDados')
rows = []
for row in grid.GetChildren():
    cells = [c for c in row.GetChildren() if c.ControlType == auto.ControlType.DataItemControl]
    rows.append([c.GetValuePattern().Value if c.GetValuePattern() else c.Name for c in cells])
```
Para `ListView` (Details): `ListItem` com filhos `Text` por coluna: `[t.Name for t in item.GetChildren()]`. (`TableControl.GetTableItemsValue` existe mas tem o bug da linha 0 e exige LegacyIAccessible.)

### Despejar a árvore para entender o app
```python
auto.EnumAndLogControl(win, maxDepth=6, showAllName=False)    # grava também no arquivo de log!
# versão leve, sem log em arquivo:
for c, d in auto.WalkControl(win, includeTop=True, maxDepth=6):
    print('  '*d, c.ControlTypeName, repr(c.AutomationId), repr(c.Name), c.ClassName)
```
(o `LogControl` consulta 34 patterns por nó; a versão acima é bem mais rápida.)

### Esperar uma janela/diálogo por regex
```python
dlg = auto.WindowControl(searchDepth=1, RegexName=r'.*Confirma.*')
if dlg.Exists(8):
    dlg.ButtonControl(Name='Sim').GetInvokePattern().Invoke()
```

### Achar o controle sob o mouse (para descobrir critérios)
```python
c = auto.ControlFromCursor()
print(c, c.GetTopLevelControl(), sep='\n')
auto.EnumAndLogControlAncestors(c)
```
Dica: use um atalho global com `RunByHotKey` para imprimir o controle sob o cursor sem mover o mouse.

### Captura de tela de um controle
```python
win.CaptureToImage('janela.png')
with win.ToBitmap(0, 0, 200, 100) as bmp:      # recorte
    bmp.ToFile('recorte.jpg', quality=90)
```

### Rodar em várias threads
```python
import threading, uiautomation as auto
def worker():
    with auto.UIAutomationInitializerInThread():
        w = auto.WindowControl(searchDepth=1, Name='X'); ...
threading.Thread(target=worker).start()
```

### Botão de emergência (kill switch)
```python
def tarefa(stop):
    while not stop.is_set():
        ...
auto.RunByHotKey({(auto.ModifierKey.Control, auto.Keys.VK_1): tarefa},
                 stopHotKey=(auto.ModifierKey.Control | auto.ModifierKey.Shift, auto.Keys.VK_2))
```

### Atalhos e combinações com `SendKeys`
```python
auto.SendKeys('{Ctrl}a{Delete}')            # selecionar tudo + apagar
auto.SendKeys('{Alt}{F4}')                  # fechar
auto.SendKeys('{Ctrl}{Shift}s')             # Ctrl+Shift+S
auto.SendKeys('{Tab 3}{Enter}')             # 3 tabs + enter
auto.SendKeys('linha1{Enter}linha2')
```
Prefira `win.GetWindowPattern().Close()` a `{Alt}{F4}`.

### Fechar / minimizar janela sem mouse 🧪
```python
win.GetWindowPattern().Close()                       # 🧪 fechou a janela do lab
win.GetWindowPattern().SetWindowVisualState(auto.WindowVisualState.Minimized)
win.Maximize(); win.Restore(); win.SetTopmost(True)
```

## 9.4 Ferramentas de inspeção (para descobrir `AutomationId`/patterns)
- **Accessibility Insights for Windows** (gratuito, Microsoft) ou **Inspect.exe** (Windows SDK / `C:\Program Files (x86)\Windows Kits\10\bin\<ver>\x64\inspect.exe`). Selecione "UIA" e a *Raw View* (a mesma que a lib percorre).
- A própria lib: `ControlFromCursor()`, `EnumAndLogControl`, `control.GetPropertyValue(...)` em laço sobre `PropertyIdNames`.

## 9.5 Cuidados ao importar/executar
- `python -m uiautomation.uiautomation` **não é uma ferramenta de inspeção**: o bloco `__main__` do módulo (L10794) abre/usa o Bloco de Notas e ao final faz `SendKeys('{Ctrl}{End}{Enter}Hello World!')` — digita na janela em foco. Não execute o arquivo diretamente.
- O texto da docstring cita `automation.py -h`, mas esse script de linha de comando **não vem no pacote instalado** (só existe no repositório do GitHub).

## 9.6 Checklist de depuração quando "não acha o controle"
1. A janela é de outro nível (elevada/admin)? 2. O controle está virtualizado/fora da tela (`ScrollIntoView`, `Realize`)? 3. O app é Electron/Chromium/Java/Qt/ jogo — a árvore pode ser mínima (Chromium só expõe com acessibilidade ativada: abra com `--force-renderer-accessibility`; Java precisa do Access Bridge)? 4. `Name` mudou por idioma/estado? 5. `searchDepth` curto demais? 6. O controle só aparece depois de uma ação (popup é filho do Desktop, não da janela — procure `auto.GetRootControl()` com `searchDepth=1`)? 7. Está em outro monitor/DPI? 8. Dump da árvore e compare com o esperado.
