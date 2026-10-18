# 13 — Guia prático: como fazer cada coisa (sem complicação)

Este capítulo é o "como fazer" do dia a dia. Os exemplos que mostram um **resultado** abaixo foram **executados e conferidos** (laboratório WinForms `UIA-LAB` e WPF). Os marcados *(ilustrativo)* seguem o mesmo padrão, mas não foram executados exatamente como estão. Nos exemplos, `janela` é a janela que você já achou:

```python
import uiautomation as auto
janela = auto.WindowControl(searchDepth=1, Name="UIA-LAB")
```

---

## 0. As 6 regras de ouro

1. **Ache a janela primeiro** e procure tudo **a partir dela** (`janela.ButtonControl(...)`), nunca do Desktop inteiro.
2. **Identifique por `AutomationId`** quando existir; depois por `Name`. Posição na tela é o último recurso.
3. **Ação = pattern primeiro** (`Invoke`, `Toggle`, `SetValue`, `Select`…). Mouse e teclado só quando não tiver jeito.
4. **Confirme que achou** com `Exists(segundos)` antes de agir (ele devolve `True/False`, não dá erro).
5. **Quando a tela mudar, espere por condição**, não por tempo fixo (`time.sleep(5)` é palpite).
6. **Descubra os nomes olhando a árvore** (seção 6), não adivinhando.

---

## 1. Clique, Invoke, Toggle, SetValue… qual usar?

### 1.1 A tabela de decisão

| Eu quero… | Use | Por quê |
|---|---|---|
| Apertar um **botão**, link, item de menu | `GetInvokePattern().Invoke(0)` | rápido, não usa o mouse, não depende de posição |
| Marcar/desmarcar uma **caixinha** | `GetTogglePattern().Toggle(0)` ou `SetChecked(True)` | `SetChecked` já garante o estado final |
| Escolher uma **opção de rádio** / item de lista / aba | `GetSelectionItemPattern().Select(0)` | seleciona direto |
| **Escrever** num campo | `GetValuePattern().SetValue("texto", 0)` | instantâneo; dispara `TextChanged` |
| Escrever e o app **valida tecla por tecla** (máscara, autocompletar, busca ao digitar) | `SendKeys("texto")` | gera eventos de teclado de verdade |
| **Abrir/fechar** árvore, expansor, combo | `GetExpandCollapsePattern().Expand(0)` / `Collapse(0)` | sem mouse |
| **Rolar** até um ponto | `GetPattern(PatternId.ScrollPattern).SetScrollPercent(-1, 50)` ou `ScrollItemPattern.ScrollIntoView()` | exato |
| **Fechar/minimizar** a janela | `GetWindowPattern().Close()` / `SetWindowVisualState(...)` | como o X |
| Botão **direito**, **duplo clique**, **arrastar**, passar o mouse | `RightClick()`, `DoubleClick()`, `DragDrop(...)`, `MoveCursorToMyCenter()` | só o mouse faz |
| O elemento **não tem nenhum pattern** | `Click()` | último recurso |
| Atalho de teclado (Ctrl+S…) | `SendKeys("{Ctrl}s")` | só o teclado faz |

### 1.2 `Invoke` × `Click` lado a lado (medido)

| | `Invoke(0)` | `Click(simulateMove=False, waitTime=0)` | `Click()` padrão |
|---|---|---|---|
| Tempo médio por ação | **4 ms** | 58 ms | 129 ms (+0,5 s de espera) |
| Move o seu mouse? | **Não** | Sim | Sim (animado) |
| Funciona com a janela **minimizada**? | **Sim** ✅ | não esperado (o elemento sai da tela) | idem |
| Funciona com o botão **coberto** por outra janela? | **Sim** ✅ | **Não**: o clique cai na janela de cima | **Não** |
| Depende de posição/monitor/escala? | Não | Sim | Sim |
| Espera o app terminar o clique? | **Sim** (cuidado!) | Não | Não |

Em português: o **`Invoke` fala com o programa; o `Click` fala com o ponteiro do mouse**. Por isso o `Invoke` aguenta janela escondida, mas também **espera o programa responder**.

### 1.3 O cuidado do `Invoke`
- Botão que abre **diálogo modal** → o `Invoke` **fica preso** até o diálogo fechar. Solução: rode numa thread ou use `Click()` (veja `05-patterns.md`).
- Botão **desabilitado** → `COMError` na hora. Teste antes: `if botao.IsEnabled:`.
- Passou `waitTime` padrão? Ele dorme **0,5 s depois**. Em sequência, use `Invoke(0)`.

### 1.4 `SetValue` × `SendKeys` (testado)
- `SetValue` **não gera nenhum evento de teclado** (o app só recebe "texto mudou"). Perfeito para formulários simples.
- `SendKeys` gera `KeyDown/KeyPress/KeyUp` como uma pessoa digitando. Use quando o campo tem **máscara**, **autocompletar** ou **busca ao digitar**.
- Campo **somente leitura** → `SetValue` dá `COMError`.
- Campo de **senha**: dá para escrever com `SetValue`, mas não dá para ler o valor de volta.

### 1.5 Uma função que escolhe o melhor jeito sozinha
```python
def agir(c):
    """Aciona o controle pelo jeito mais confiável e diz qual usou."""
    p = c.GetPattern(auto.PatternId.InvokePattern)
    if p: p.Invoke(0); return 'Invoke'
    p = c.GetPattern(auto.PatternId.TogglePattern)
    if p: p.Toggle(0); return 'Toggle'
    p = c.GetPattern(auto.PatternId.ExpandCollapsePattern)
    if p: p.Expand(0); return 'Expand'
    p = c.GetPattern(auto.PatternId.SelectionItemPattern)
    if p: p.Select(0); return 'SelectionItem.Select'
    p = c.GetLegacyIAccessiblePattern()
    if p and p.DefaultAction: p.DoDefaultAction(0); return 'Legacy.DoDefaultAction'
    c.Click(simulateMove=False, waitTime=0.1); return 'Click (mouse)'
```
Resultados reais: botão → `Invoke`; caixa de seleção → `Invoke`; item de lista → `Invoke`; item de árvore → `Expand`; rádio → `Invoke`.

### 1.6 Quando o clique de mouse é a resposta certa
- **Botão direito** (menu de contexto): `controle.RightClick()`.
- **Duplo clique**: `controle.DoubleClick()` (gera 2 `MouseDown` + 1 `DoubleClick`).
- **Arrastar e soltar**: `controle.DragDrop(10, 10, 100, 50)` (coordenadas **dentro do controle**).
- **Passar o mouse** para abrir um tooltip/submenu: `controle.MoveCursorToMyCenter()`.
- **Clicar num ponto específico**: `controle.Click(10, 10)` (10 px do canto superior esquerdo), `controle.Click(-10, -10)` (10 px do canto inferior direito), `controle.Click(ratioX=0.9, ratioY=0.5)` (90 % da largura, no meio).
- Antes de clicar: a janela precisa estar **visível, descoberta e em primeiro plano**; confirme com `janela.SetActive()`.

---

## 2. Achando o elemento certo

### 2.1 A escada (comece de cima, desça só se precisar)
```python
janela.ButtonControl(AutomationId="btnClick")        # 1) AutomationId (o melhor)
janela.ButtonControl(Name="Clicar")                  # 2) Name (muda com o idioma)
janela.ButtonControl(SubName="lic")                  # 3) pedaço do nome
janela.ListItemControl(RegexName=r"Item 5\d?$")      # 4) expressão regular (compara do começo)
janela.CheckBoxControl(foundIndex=3)                 # 5) "o 3º checkbox" (frágil)
janela.Control(Compare=lambda c, d: c.ControlTypeName == "EditControl" and c.IsPassword)   # 6) sua regra
```
Resultados reais: o `foundIndex=3` achou `chkGrupo`; o `Compare` achou `txtSenha`; o regex achou `Item 5`.

### 2.2 Dicas que evitam 90% dos problemas
- **Mesmo nome em vários lugares?** Procure **a partir do pai** certo (seção 3), não da janela.
- **`Depth=1`** limita a filhos **diretos**: `janela.ButtonControl(Depth=1, Name="Clicar")`.
- **`searchDepth=2`** limita a profundidade. Menos profundidade = busca mais rápida.
- Guarde o controle numa variável e **reuse**; cada nova busca refaz a varredura.
- Procure **primeiro o container** (grupo, painel, aba) e depois o que está dentro: é mais rápido e não confunde.
- `RegexName` compara **desde o começo**; use `.*trecho` para "contém".
- Parâmetro de busca inventado (`Foo="x"`) é **ignorado em silêncio**; use só os da lista.

---

## 3. Navegando pela árvore: pai, filho, irmão

Pense na tela como um organograma:

```
Janela "UIA-LAB"
 ├── Texto  lblStatus            ← irmão do botão
 ├── Botão  btnClick             ← irmão do texto
 ├── ...
 ├── GroupBox  grpCaixa          ← PAI do checkbox
 │     └── CheckBox  chkGrupo    ← FILHO do grupo
 ├── Edit  cmbEditavel ...
 ├── Edit  txtNome               ← anterior: cmbEditavel · seguinte: txtSenha
 └── Edit  txtSenha
```

### 3.1 Do filho para o pai
```python
chk   = janela.CheckBoxControl(AutomationId="chkGrupo")
grupo = chk.GetParentControl()                 # ('GroupControl', 'grpCaixa')
topo  = chk.GetTopLevelControl()               # a janela: 'UIA-LAB'
g2    = chk.GetAncestorControl(lambda c, d: c.ControlTypeName == "GroupControl")   # sobe até achar
```
`GetAncestorControl` sobe pai por pai e chama sua função com `(controle, profundidade)` (a profundidade é -1, -2, …).

### 3.2 Do pai para os filhos
```python
grupo.CheckBoxControl()                         # procura DENTRO do grupo
[c.AutomationId for c in grupo.GetChildren()]   # ['chkGrupo']
grupo.GetFirstChildControl()                    # primeiro filho
grupo.GetLastChildControl()                     # último filho
janela[3]                                       # o 3º filho (começa em 1); janela[-1] é o último
```
`janela[3]` e `janela.GetChildren()[2]` são o **mesmo** elemento. `janela[0]` dá erro; `janela[9999]` devolve `None`.

### 3.3 De irmão para irmão (o truque do rótulo)
```python
campo = janela.EditControl(AutomationId="txtNome")
campo.GetNextSiblingControl()        # txtSenha  (o seguinte)
campo.GetPreviousSiblingControl()    # cmbEditavel (o anterior)

# "o primeiro campo de texto depois deste rótulo":
rotulo = janela.TextControl(AutomationId="lblStatus")
rotulo.GetSiblingControl(lambda c: c.ControlTypeName == "EditControl")    # txtNome
```
Esse é o jeito clássico de achar um campo **pelo texto ao lado dele** quando o campo não tem `AutomationId`. `GetSiblingControl(cond, forward=False)` olha primeiro os irmãos **anteriores** (do mais próximo para o mais distante) e depois os seguintes.

### 3.4 Receita: achar pelo pai quando o filho não tem identificador
```python
# 1) ache o container pelo que ele TEM (id ou nome)
grupo = janela.GroupControl(AutomationId="grpCaixa")
# 2) procure dentro dele
grupo.CheckBoxControl().SetChecked(True)
```

### 3.5 Receita: achar o pai a partir de um filho conhecido *(ilustrativo)*
```python
botao_ok = dialogo.ButtonControl(Name="OK")
caixa    = botao_ok.GetParentControl()      # o painel que agrupa os botões do diálogo
for irmao in caixa.GetChildren():
    print(irmao.ControlTypeName, irmao.Name)
```

---

## 4. Iterando dentro dos elementos

### 4.1 Os três jeitos
```python
# a) filhos DIRETOS (rápido, 1 nível)
for filho in janela.GetChildren():
    print(filho.ControlTypeName, filho.AutomationId)

# b) TODOS os descendentes, em ordem (WalkControl)
for controle, profundidade in auto.WalkControl(janela, includeTop=False, maxDepth=4):
    print("  " * profundidade, controle.ControlTypeName, controle.AutomationId)

# c) só os que casam com um filtro (helper abaixo)
botoes = achar_todos(janela, 3, tipo="ButtonControl")
```
**Sempre limite `maxDepth`**: sem limite o `WalkControl` percorre a janela inteira (a janela do laboratório tem 174 elementos até o fundo).

### 4.2 Contar por tipo (bom para "entender" uma tela)
```python
from collections import Counter
Counter(c.ControlTypeName[:-7] for c in janela.GetChildren())
# {'Button': 5, 'CheckBox': 2, 'ComboBox': 3, 'Edit': 5, 'Group': 1, 'List': 2, ...}
```

### 4.3 Cuidado: o filho nem sempre é o que você espera
Uma lista de 60 itens devolve **61 filhos** (os 60 itens + a barra de rolagem). **Filtre por tipo**:
```python
itens = [c for c in lista.GetChildren() if c.ControlTypeName == "ListItemControl"]   # 60
```

### 4.4 Listas, abas e árvores
```python
lista = janela.ListControl(AutomationId="lstItens")
lista.ListItemControl(Name="Item 3").GetSelectionItemPattern().Select(0)    # escolher
[t.Name for t in janela.TabControl().GetChildren() if t.ControlTypeName == "TabItemControl"]   # ['Aba Um', 'Aba Dois']
```
**Percorrer uma árvore inteira** (expande, desce e recolhe de volta):
```python
def percorrer_arvore(item, nivel=0, saida=None):
    saida = [] if saida is None else saida
    saida.append("  " * nivel + item.Name)
    ec = item.GetExpandCollapsePattern()
    estava = ec.ExpandCollapseState if ec else None
    if ec and estava == 0: ec.Expand(0)
    for filho in [c for c in item.GetChildren() if c.ControlTypeName == "TreeItemControl"]:
        percorrer_arvore(filho, nivel + 1, saida)
    if ec and estava == 0: ec.Collapse(0)
    return saida

arvore = janela.TreeControl(AutomationId="tvArvore")
for raiz in [c for c in arvore.GetChildren() if c.ControlTypeName == "TreeItemControl"]:
    print("\n".join(percorrer_arvore(raiz)))
# Raiz A / Filho A1 / Filho A2 / Raiz B / Filho B1 / Neto B1a (com a indentação)
```

### 4.5 Tabelas
**ListView (colunas):** cada linha é um `ListItem` e as células são os filhos.
```python
lv = janela.ListControl(AutomationId="lvTabela")
linha = next(i for i in lv.GetChildren() if i.ControlTypeName == "ListItemControl" and i.Name == "Banana")
[c.Name for c in linha.GetChildren()]        # ['Banana', '12', '0,80']
linha.GetChildren()[1].Name                  # '12'  (2ª coluna)
linha.GetTogglePattern().Toggle(0)           # marca a caixinha da linha (ListView com CheckBoxes)
```
**DataGrid (grade):** a estrutura é `Table → Custom (linha) → DataItem (célula)`; a primeira "linha" é o cabeçalho.
```python
def linhas_da_tabela(tab):
    saida = []
    for lin in tab.GetChildren():
        celulas = [c for c in lin.GetChildren() if c.ControlTypeName == "DataItemControl"]
        if celulas:                           # pula o cabeçalho
            saida.append([(c.GetValuePattern().Value if c.GetValuePattern() else c.Name) for c in celulas])
    return saida

grade = janela.TableControl(AutomationId="dgvDados")
linhas_da_tabela(grade)       # [['Caneta','100','2,50'], ['Caderno','40','18,90'], ['Mochila','8','149,00']]
next(l[2] for l in linhas_da_tabela(grade) if l[0] == "Caderno")     # '18,90'  (preço do Caderno)
grade.DataItemControl(Name="Estoque Linha 1").GetValuePattern().Value   # '40'  (célula direta)
```
**WPF DataGrid:** use o `GridPattern`: `grade.GetPattern(auto.PatternId.GridPattern).GetItem(linha, coluna)` (a célula vem como `CustomControl`; leia com `GetPattern(PatternId.ValuePattern).Value`).

### 4.6 Listas gigantes (virtualizadas, comuns em WPF)
Itens fora da tela podem nem existir na árvore. Use o `ItemContainerPattern` para achar um item sem rolar até ele:
```python
lista = janela_wpf.ListControl(AutomationId="lbBig")                # 500 itens
cont  = lista.GetPattern(auto.PatternId.ItemContainerPattern)
primeiro = lista.ListItemControl(Name="Linha 1")
item = cont.FindItemByProperty(primeiro, auto.PropertyId.NameProperty, "Linha 400")   # precisa de um Control inicial (None dá erro)
item.GetPattern(auto.PatternId.VirtualizedItemPattern).Realize(0)   # materializa
item.GetPattern(auto.PatternId.ScrollItemPattern).ScrollIntoView(0) # traz para a vista
item.GetPattern(auto.PatternId.SelectionItemPattern).Select(0)
```

### 4.7 Menus
```python
janela.MenuItemControl(Name="Arquivo").GetInvokePattern().Invoke(0.4)   # abre o menu
janela.MenuItemControl(Name="Novo").GetInvokePattern().Invoke(0.3)      # escolhe o item
```
(Testado: o app recebeu o evento do menu "Novo".)

---

## 5. Receitas completas

### 5.1 Formulário inteiro, sem mouse
```python
janela.EditControl(AutomationId="txtNome").GetValuePattern().SetValue("Maria da Silva", 0)
janela.CheckBoxControl(AutomationId="chkAceito").SetChecked(True)
janela.RadioButtonControl(AutomationId="rdB").GetSelectionItemPattern().Select(0)
janela.ListControl(AutomationId="lstItens").ListItemControl(Name="Item 3").GetSelectionItemPattern().Select(0)
janela.ButtonControl(AutomationId="btnClick").GetInvokePattern().Invoke(0)
```

### 5.2 Esperar por uma condição (em vez de `sleep`)
```python
import time

def esperar_ate(condicao, tempo=10, intervalo=0.3):
    """Repete 'condicao()' até dar True (ou estourar o tempo)."""
    fim = time.perf_counter() + tempo
    while time.perf_counter() < fim:
        try:
            if condicao(): return True
        except Exception:
            pass                       # o elemento pode ainda não existir
        time.sleep(intervalo)
    return False

# (ilustrativo)
esperar_ate(lambda: janela.ButtonControl(Name="Concluir").IsEnabled, 30)
esperar_ate(lambda: not janela.ProgressBarControl().Exists(0, 0), 60)    # "até a barra sumir"
```
Para esperar **um controle aparecer ou sumir**, o jeito nativo é melhor: `controle.Exists(10)` e `controle.Disappears(10)`.

### 5.3 Tratar janela que fechou no meio do caminho
Reusar um controle de uma janela que já fechou dá **`COMError`**, não `False` (confirmado). Exemplo *(ilustrativo)*:
```python
import comtypes
try:
    botao.GetInvokePattern().Invoke(0)
except comtypes.COMError:
    print("a janela/elemento não existe mais")
```

---

## 6. Descobrindo o que usar (sem ferramenta externa)

A própria biblioteca mostra tudo. Estas funções (testadas) viram o seu "olho":

```python
def descrever(c):
    """Uma linha legível com as 'identidades' do controle."""
    return f"{c.ControlTypeName[:-7]} | id={c.AutomationId!r} | nome={c.Name!r} | classe={c.ClassName!r}"

def caminho(c):
    """Do Desktop até o controle: quem é o pai do pai do pai…"""
    cadeia = []
    while c is not None:
        cadeia.insert(0, descrever(c))
        c = c.GetParentControl()
    return cadeia

def padroes(c):
    """Quais habilidades (patterns) o controle tem."""
    return [nome.replace("Pattern", "") for pid, nome in auto.PatternIdNames.items() if c.GetPattern(pid)]

def gerar_codigo(c, pai="janela"):
    """Sugere a linha de código que acha este controle (melhor identificador primeiro)."""
    tipo = c.ControlTypeName
    if c.AutomationId: return f"{pai}.{tipo}(AutomationId={c.AutomationId!r})"
    if c.Name:         return f"{pai}.{tipo}(Name={c.Name!r})"
    if c.ClassName:    return f"{pai}.{tipo}(ClassName={c.ClassName!r})"
    return f"{pai}.{tipo}()   # sem identificador: procure pelo pai ou pela posição"

def achar_todos(raiz, profundidade=8, **criterios):
    """Todos os descendentes que casam: tipo=, id=, nome=, contem=."""
    achados = []
    for c, d in auto.WalkControl(raiz, False, profundidade):
        if "tipo" in criterios and c.ControlTypeName != criterios["tipo"]: continue
        if "id" in criterios and c.AutomationId != criterios["id"]: continue
        if "nome" in criterios and c.Name != criterios["nome"]: continue
        if "contem" in criterios and criterios["contem"] not in c.Name: continue
        achados.append(c)
    return achados
```
Resultados reais com o botão do laboratório:
```
descrever(botao)  -> Button | id='btnClick' | nome='Clicar' | classe='WindowsForms10.BUTTON.app.0...'
padroes(botao)    -> ['Invoke', 'LegacyIAccessible']
gerar_codigo(botao) -> janela.ButtonControl(AutomationId='btnClick')
```
E o código gerado **acha mesmo** o controle (conferido com `eval`).

### 6.1 "O que é aquilo na tela?" — inspetor do cursor
Rode, e **durante a contagem** leve o mouse até o elemento que quer entender:
```python
def inspecionar_cursor(espera=3):
    for i in range(espera, 0, -1):
        print(f"posicione o mouse sobre o elemento... {i}"); time.sleep(1)
    c = auto.ControlFromCursor()
    print("elemento :", descrever(c))
    print("patterns :", padroes(c))
    print("código   :", gerar_codigo(c))
    print("caminho  :")
    for linha in caminho(c): print("   ", linha)

inspecionar_cursor()
```
Saída real sobre o botão do laboratório: o tipo, `id='btnClick'`, `['Invoke', 'LegacyIAccessible']` e a cadeia `Pane → Window → Button`. A linha "código" já é a que você cola no script.

> ⚠️ Esses utilitários **leem texto da tela** (nomes de janelas, abas…). Não publique a saída sem conferir.

### 6.2 Despejar a árvore de uma janela
```python
for c, d in auto.WalkControl(janela, includeTop=True, maxDepth=3):
    print("  " * d, descrever(c))
```
Use para escolher entre `AutomationId` e `Name` e para ver **em que nível** está o que você quer (ajuda a regular `searchDepth`/`Depth`).

---

## 7. Armadilhas rápidas (leia antes de culpar a biblioteca)

| Sintoma | Causa provável | Conserto |
|---|---|---|
| `LookupError ... Timeout` | nome/id errado, nível fundo demais, ou o elemento ainda não apareceu | despeje a árvore (6.2); use `Exists(10)` |
| Achou o elemento **errado** | o mesmo `Name` aparece em mais de um lugar | procure a partir do pai certo (seção 3) |
| `Invoke` demora ou trava | botão que abre diálogo modal | thread ou `Click()` |
| `COMError` ao reusar controle | a janela/elemento já fechou | `try/except comtypes.COMError` ou `Refind()` |
| `Click()` caiu em outro lugar | outra janela por cima, janela minimizada ou escala/monitor diferente | traga a janela para frente (`SetActive()`) ou use pattern |
| `SendKeys` digitou onde não devia | o foco estava em outra janela | confirme `auto.GetForegroundWindow() == janela.NativeWindowHandle` |
| `{Alt}` não faz Alt | em teclado com Alt Gr (pt-BR) ele vira Ctrl+Alt | use `{LAlt}` |
| Lista "tem 61 itens" | a barra de rolagem também é filha | filtre por `ControlTypeName` |
| `GetXxxPattern()` não existe | o controle é genérico (`Control`/`CustomControl`) | `GetPattern(auto.PatternId.XxxPattern)` |
| Valor de campo de senha vem vazio | é proposital | só dá para escrever |

---

## 8. Checklist de 30 segundos antes de rodar

- [ ] Achei a janela com `Exists(10)`?
- [ ] Cada controle tem `AutomationId` ou nome confiável (e não posição)?
- [ ] Usei pattern onde dava (e `Click` só onde não dava)?
- [ ] Botões que abrem diálogo estão em thread / uso `Click`?
- [ ] Se vou usar teclado, o foco está confirmado?
- [ ] Tenho um jeito de **parar** o robô (hotkey, veja `09-dicas-e-receitas.md`)?
- [ ] Desliguei o log em arquivo (`auto.Logger.SetLogFile("")`)?
- [ ] Testei primeiro num ambiente de treino, não no sistema de verdade?
