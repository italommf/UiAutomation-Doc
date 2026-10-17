# 🤖 Automatizando o Windows com Python: o guia humano da biblioteca `uiautomation`

> **Em uma frase:** como fazer o Python "enxergar" e operar janelas, botões, campos e menus de qualquer programa do Windows, do jeito que uma pessoa faria, só que sem cansar, sem errar a digitação e sem reclamar.

Este guia nasceu de um estudo completo da biblioteca **[uiautomation](https://github.com/yinkaisheng/Python-UIAutomation-for-Windows)** (versão **2.0.29**): li o código-fonte inteiro (cerca de 10 mil linhas), testei as funções principais num programa de laboratório criado só para isso e transformei tudo em explicações para quem **não é especialista**.

Não precisa saber nada de automação. Se você já escreveu um `print("olá")` em Python, consegue acompanhar.

---

## 📑 Sumário

1. [O que é isso, afinal?](#1--o-que-é-isso-afinal)
2. [Para que serve (e para que NÃO serve)](#2--para-que-serve-e-para-que-não-serve)
3. [Instalação passo a passo](#3--instalação-passo-a-passo)
4. [Seu primeiro robô em 5 minutos](#4--seu-primeiro-robô-em-5-minutos)
5. [Como o robô "enxerga": a árvore de controles](#5--como-o-robô-enxerga-a-árvore-de-controles)
6. [Encontrando elementos (a arte da busca)](#6--encontrando-elementos-a-arte-da-busca)
7. [Agindo: os três jeitos de fazer algo acontecer](#7--agindo-os-três-jeitos-de-fazer-algo-acontecer)
8. [Os patterns: as "habilidades" de cada elemento](#8--os-patterns-as-habilidades-de-cada-elemento)
9. [Catálogo dos tipos de controle](#9--catálogo-dos-tipos-de-controle)
10. [Receitas prontas (copiar e usar)](#10--receitas-prontas-copiar-e-usar)
11. [Mouse e teclado "de verdade"](#11--mouse-e-teclado-de-verdade)
12. [Janelas, tela, clipboard e processos](#12--janelas-tela-clipboard-e-processos)
13. [Prints e imagens](#13--prints-e-imagens)
14. [Esperas, tempo limite e erros](#14--esperas-tempo-limite-e-erros)
15. [Truques e boas práticas](#15--truques-e-boas-práticas)
16. [Armadilhas e bugs que ninguém te conta](#16--armadilhas-e-bugs-que-ninguém-te-conta)
17. [Como descobrir os "nomes" dos elementos (depuração)](#17--como-descobrir-os-nomes-dos-elementos-depuração)
18. [Segurança, ética e bom senso](#18--segurança-ética-e-bom-senso)
19. [Perguntas frequentes](#19--perguntas-frequentes)
20. [Glossário em português claro](#20--glossário-em-português-claro)
21. [O que tem neste repositório](#21--o-que-tem-neste-repositório)
22. [Como este estudo foi feito (e o que é certeza, o que é suposição)](#22--como-este-estudo-foi-feito-e-o-que-é-certeza-o-que-é-suposição)
23. [Créditos e licença](#23--créditos-e-licença)

---

## 1. 🧠 O que é isso, afinal?

### A ideia em uma analogia

Imagine que você precisa preencher a mesma planilha em um programa antigo, 300 vezes por semana. Você abre a janela, clica no campo "Nome", digita, clica em "Salvar", espera, repete. É chato e dá erro.

Agora imagine contratar um assistente muito literal que:

- **olha a tela** e entende que ali existe "um botão chamado Salvar", "um campo de texto chamado Nome" e "uma caixa de seleção chamada Aceito os termos";
- consegue **apertar o botão** ou **escrever no campo** sem precisar mexer no seu mouse;
- trabalha sem se distrair.

Esse assistente é o que o Python + `uiautomation` entregam.

### Como o Windows permite isso?

O Windows tem, desde o Vista, um recurso chamado **UI Automation** (Automação da Interface do Usuário). Ele existe principalmente para **acessibilidade**: é por ele que leitores de tela (como o Narrador do Windows ou o NVDA) conseguem *ler em voz alta* o que está na tela para pessoas com deficiência visual.

Para isso, cada programa "se descreve" para o Windows: *"aqui tem um botão, o nome dele é OK, ele está habilitado, dá para clicar"*. O Windows junta tudo isso numa **árvore** (como o organograma de uma empresa) e qualquer programa pode consultá-la.

A biblioteca `uiautomation` é uma **tradução amigável** desse recurso para o Python. Ela é gratuita (licença Apache 2.0) e só roda no Windows.

### O que a biblioteca faz, em lista

| Você quer… | A biblioteca oferece… |
|---|---|
| Achar uma janela, botão, campo, menu… | Busca por nome, tipo, identificador, classe |
| Clicar sem mexer no mouse | "Invocar" o elemento direto |
| Escrever em campos | Definir o valor direto, ou digitar tecla por tecla |
| Marcar/desmarcar caixas, escolher itens | Alternar, selecionar, expandir |
| Ler textos e tabelas da tela | Ler valor/nome/células |
| Mexer em janelas | Maximizar, minimizar, fechar, mover, trazer para frente |
| Tirar prints | Capturar uma janela ou só um pedaço |
| Controlar mouse e teclado "de verdade" | Cliques, arrastar, rolar, atalhos |
| Lidar com a área de transferência | Copiar/colar texto, HTML, imagem |
| Listar e encerrar programas | Lista de processos |
| Disparar scripts por atalho global | Hotkeys do tipo Ctrl+Shift+algo |

---

## 2. ✅ Para que serve (e para que NÃO serve)

### Bom uso

- Automatizar **programas de desktop antigos** que não têm API nem integração (sistemas legados, programas internos, emissores, ERPs "de janela").
- **Testar** seu próprio programa (cliques, formulários, fluxos).
- Fazer tarefas repetitivas **no seu próprio computador** com programas que você tem direito de usar.
- Acessibilidade e leitura estruturada da tela.

### Antes de automatizar, pergunte-se

> **Existe um caminho oficial?** Se o sistema tem uma API, um serviço web oficial, exportação de arquivo ou integração, **use isso primeiro**. Automação de tela é o plano B: é mais frágil (uma atualização que muda um botão de lugar pode quebrar o robô) e mais lenta.

Automação de interface é ótima quando **não há outro jeito razoável**. Quando há, o caminho oficial costuma ser mais seguro, rápido e estável.

### Quando NÃO é a ferramenta certa

- **Sites e aplicativos web:** use ferramentas feitas para navegador (Selenium, Playwright). Dá para controlar navegador por UI Automation, mas é o caminho difícil.
- **Jogos e programas que desenham tudo "na unha"** (sem expor botões ao Windows): a árvore fica quase vazia.
- **Linux e macOS:** a biblioteca é **só Windows**.
- **Tarefas que exigem burlar proteções** de terceiros (CAPTCHAs, bloqueios, termos de uso): além de não ser o objetivo da ferramenta, pode ser ilegal ou violar contratos. Veja a seção de [ética](#18--segurança-ética-e-bom-senso).

---

## 3. 🛠️ Instalação passo a passo

### Requisitos

- **Windows** (testado em Windows 11, Python 3.12).
- **Python 3.x** instalado (3.8 ou mais novo é o recomendado).
- Conexão com a internet apenas para instalar.
- Nada de administrador para a maioria dos casos (veja a [FAQ](#19--perguntas-frequentes) para exceções).

### Passo a passo (PowerShell)

Abra o PowerShell na pasta do seu projeto e rode:

```powershell
# 1. Cria um "ambiente virtual" (uma caixinha isolada para suas bibliotecas)
python -m venv .venv

# 2. Instala a biblioteca dentro dessa caixinha
.\.venv\Scripts\python.exe -m pip install --upgrade pip uiautomation

# 3. Confere
.\.venv\Scripts\python.exe -m pip list
```

Você deve ver algo como:

```
Package      Version
------------ -------
comtypes     1.4.17
pip          26.2.1
uiautomation 2.0.29
```

> 💡 **Por que ambiente virtual?** Para não misturar as bibliotecas deste projeto com as de outros. Se algo der errado, você apaga a pasta `.venv` e recomeça sem sujar o resto do computador.

A única dependência da biblioteca é o **`comtypes`** (a ponte entre Python e o sistema de componentes do Windows). Ele é instalado automaticamente.

### Primeiro teste de sanidade

```python
import uiautomation as auto
print(auto.GetScreenSize())   # por exemplo: (1920, 1080)
```

Se imprimiu a resolução da sua tela, está tudo certo.

---

## 4. 🚀 Seu primeiro robô em 5 minutos

Para aprender sem risco, este guia traz o código de um **laboratório**: uma janelinha chamada **UIA-LAB**, feita só para treino, com um exemplar de cada tipo de controle (botões, caixas de texto, listas, tabela, árvore, abas, menu, barra de progresso, etc.).

**Por que um laboratório?** Porque aprender automação mexendo nos *seus* programas de verdade é a receita para o desastre (um robô digitando no lugar errado pode apagar ou enviar algo que você não queria). O laboratório é seguro e previsível.

### 4.1 Crie e abra o laboratório

1. Copie o código abaixo (clique em **"Ver o código do laboratório"**) e salve num arquivo chamado `lab.ps1`.
2. Abra o PowerShell na pasta onde salvou e rode:

```powershell
powershell -STA -ExecutionPolicy Bypass -File lab.ps1
```

<details>
<summary><b>Ver o código do laboratório (lab.ps1)</b></summary>

```powershell
# Laboratorio proprio para testar o uiautomation (janela "UIA-LAB"), com AutomationId em tudo.
Add-Type -AssemblyName System.Windows.Forms, System.Drawing
[System.Windows.Forms.Application]::EnableVisualStyles()
$f = New-Object Windows.Forms.Form
$f.Text = "UIA-LAB"; $f.Name = "frmLab"; $f.Width = 1000; $f.Height = 800; $f.StartPosition = "Manual"; $f.Left = 100; $f.Top = 60
function Add($c,$name,$x,$y,$w,$h,$text){ $c.Name=$name; $c.Left=$x;$c.Top=$y;$c.Width=$w;$c.Height=$h; if($text){$c.Text=$text}; $f.Controls.Add($c); $c }
$lbl = Add (New-Object Windows.Forms.Label) "lblStatus" 10 5 400 20 "evento: nenhum"
$script:n = 0
$btn = Add (New-Object Windows.Forms.Button) "btnClick" 10 30 120 28 "Clicar"
$btn.Add_Click({ $script:n++; $lbl.Text = "evento: clique $script:n" })
$btnD = Add (New-Object Windows.Forms.Button) "btnDesab" 140 30 120 28 "Desabilitado"; $btnD.Enabled = $false
$chk = Add (New-Object Windows.Forms.CheckBox) "chkAceito" 10 65 150 24 "Aceito os termos"
$chk.Add_CheckedChanged({ $lbl.Text = "evento: chk=" + $chk.Checked })
$chk3 = Add (New-Object Windows.Forms.CheckBox) "chkTri" 170 65 150 24 "Tri-estado"; $chk3.ThreeState = $true
$r1 = Add (New-Object Windows.Forms.RadioButton) "rdA" 10 95 80 24 "Opcao A"
$r2 = Add (New-Object Windows.Forms.RadioButton) "rdB" 100 95 80 24 "Opcao B"
$r1.Add_CheckedChanged({ if($r1.Checked){$lbl.Text="evento: radio A"} }); $r2.Add_CheckedChanged({ if($r2.Checked){$lbl.Text="evento: radio B"} })
$cmb = Add (New-Object Windows.Forms.ComboBox) "cmbCor" 10 125 150 24 ""; $cmb.DropDownStyle="DropDownList"; [void]$cmb.Items.AddRange(@("Vermelho","Verde","Azul","Amarelo"))
$cmb.Add_SelectedIndexChanged({ $lbl.Text = "evento: cor=" + $cmb.SelectedItem })
$cmbE = Add (New-Object Windows.Forms.ComboBox) "cmbEditavel" 170 125 150 24 ""; [void]$cmbE.Items.AddRange(@("um","dois","tres"))
$txt = Add (New-Object Windows.Forms.TextBox) "txtNome" 10 155 200 24 ""
$txt.Add_TextChanged({ $lbl.Text = "evento: texto=" + $txt.Text })
$pwd = Add (New-Object Windows.Forms.TextBox) "txtSenha" 220 155 150 24 ""; $pwd.UseSystemPasswordChar = $true
$ml = Add (New-Object Windows.Forms.TextBox) "txtMulti" 10 185 360 80 "linha 1`r`nlinha 2`r`nlinha 3 com acentuacao: caoe"; $ml.Multiline=$true; $ml.ScrollBars="Vertical"
$lb = Add (New-Object Windows.Forms.ListBox) "lstItens" 380 30 150 100 ""; [void]$lb.Items.AddRange(@("Item 1","Item 2","Item 3","Item 4")); $lb.SelectionMode="MultiExtended"
$lv = Add (New-Object Windows.Forms.ListView) "lvTabela" 540 30 430 100 ""; $lv.View="Details"; $lv.FullRowSelect=$true; $lv.CheckBoxes=$true
[void]$lv.Columns.Add("Nome",120); [void]$lv.Columns.Add("Qtd",60); [void]$lv.Columns.Add("Preco",80)
foreach($r in @(@("Maca","3","1,50"),@("Banana","12","0,80"),@("Uva","1","7,00"))){ $i=New-Object Windows.Forms.ListViewItem($r[0]); [void]$i.SubItems.Add($r[1]); [void]$i.SubItems.Add($r[2]); [void]$lv.Items.Add($i) }
$tv = Add (New-Object Windows.Forms.TreeView) "tvArvore" 380 140 200 125 ""
$a=$tv.Nodes.Add("Raiz A"); [void]$a.Nodes.Add("Filho A1"); [void]$a.Nodes.Add("Filho A2"); $b=$tv.Nodes.Add("Raiz B"); $b.Nodes.Add("Filho B1").Nodes.Add("Neto B1a") | Out-Null
$tb = Add (New-Object Windows.Forms.TrackBar) "trkVolume" 590 140 200 40 ""; $tb.Minimum=0; $tb.Maximum=100; $tb.Value=30
$pb = Add (New-Object Windows.Forms.ProgressBar) "pbProgresso" 590 185 200 20 ""; $pb.Value=45
$nud = Add (New-Object Windows.Forms.NumericUpDown) "nudQtd" 800 140 80 24 ""; $nud.Minimum=0;$nud.Maximum=50;$nud.Value=5
$dt = Add (New-Object Windows.Forms.DateTimePicker) "dtpData" 590 215 200 24 ""
$mc = Add (New-Object Windows.Forms.MonthCalendar) "calMes" 800 175 230 160 ""
$tabs = Add (New-Object Windows.Forms.TabControl) "tabGeral" 10 275 360 120 ""
$tp1 = New-Object Windows.Forms.TabPage; $tp1.Text="Aba Um"; $tp1.Name="tpUm"; $tp2 = New-Object Windows.Forms.TabPage; $tp2.Text="Aba Dois"; $tp2.Name="tpDois"
$inner = New-Object Windows.Forms.Button; $inner.Text="Botao na Aba Dois"; $inner.Name="btnAbaDois"; $inner.Width=140; $inner.Left=10; $inner.Top=10; $tp2.Controls.Add($inner)
$tabs.TabPages.Add($tp1); $tabs.TabPages.Add($tp2)
$gb = Add (New-Object Windows.Forms.GroupBox) "grpCaixa" 380 275 200 120 "Grupo"
$inG = New-Object Windows.Forms.CheckBox; $inG.Text="Dentro do grupo"; $inG.Name="chkGrupo"; $inG.Left=10;$inG.Top=25;$inG.Width=150; $gb.Controls.Add($inG)
$lnk = Add (New-Object Windows.Forms.LinkLabel) "lnkSite" 590 250 200 20 "Link clicavel"
$lnk.Add_LinkClicked({ $lbl.Text = "evento: link" })
$dg = Add (New-Object Windows.Forms.DataGridView) "dgvDados" 10 405 560 150 ""; $dg.AllowUserToAddRows=$false
[void]$dg.Columns.Add("c1","Produto"); [void]$dg.Columns.Add("c2","Estoque"); [void]$dg.Columns.Add("c3","Preco")
[void]$dg.Rows.Add("Caneta","100","2,50"); [void]$dg.Rows.Add("Caderno","40","18,90"); [void]$dg.Rows.Add("Mochila","8","149,00")
$pic = Add (New-Object Windows.Forms.PictureBox) "picImg" 590 345 120 80 ""; $pic.BackColor=[Drawing.Color]::Tomato
$ms = New-Object Windows.Forms.MenuStrip; $ms.Name="menuPrincipal"
$mArq = New-Object Windows.Forms.ToolStripMenuItem("Arquivo"); $mArq.Name="mnuArquivo"
$mNovo = New-Object Windows.Forms.ToolStripMenuItem("Novo"); $mNovo.Name="mnuNovo"; $mNovo.Add_Click({ $lbl.Text="evento: menu Novo" })
$mSair = New-Object Windows.Forms.ToolStripMenuItem("Sair do lab"); $mSair.Name="mnuSair"; $mSair.Add_Click({ $f.Close() })
[void]$mArq.DropDownItems.Add($mNovo); [void]$mArq.DropDownItems.Add($mSair); [void]$ms.Items.Add($mArq); $f.MainMenuStrip=$ms; $f.Controls.Add($ms)
$ss = New-Object Windows.Forms.StatusStrip; $ss.Name="statusBar"; [void]$ss.Items.Add("Pronto - barra de status"); $f.Controls.Add($ss)
$ts = New-Object Windows.Forms.ToolStrip; $ts.Name="toolBar"; $tbtn=$ts.Items.Add("BotaoTool"); $tbtn.Name="tsbTool"; $tbtn.Add_Click({ $lbl.Text="evento: toolbar" }); $f.Controls.Add($ts)
$f.Add_Shown({ $f.Activate() })
[void]$f.ShowDialog()
```

</details>

Vai aparecer a janela **UIA-LAB**. Deixe-a aberta. (O código só cria uma janela de treino na memória; não grava nada em disco. Para fechar, use *Arquivo → Sair do lab* ou o X.)

> ℹ️ Os nomes do laboratório não têm acento de propósito, para o arquivo funcionar sem configurar codificação.

### 4.2 Encontre a janela

Em outro terminal:

```python
import uiautomation as auto

janela = auto.WindowControl(searchDepth=1, Name="UIA-LAB")
print(janela.Exists(10))      # True se achou em até 10 segundos
print(janela)
```

Repare no `searchDepth=1`: significa *"procure só entre as janelas de nível mais alto"*. É mais rápido do que vasculhar tudo.

### 4.3 Aperte um botão sem encostar no mouse

```python
botao = janela.ButtonControl(AutomationId="btnClick")
botao.GetInvokePattern().Invoke()
```

O texto do rótulo no topo do laboratório muda para **"evento: clique 1"**. Você acabou de clicar sem mover o mouse.

### 4.4 Escreva num campo

```python
campo = janela.EditControl(AutomationId="txtNome")
campo.GetValuePattern().SetValue("Olá, çãõ!")
print(campo.GetValuePattern().Value)     # -> Olá, çãõ!
```

### 4.5 Marque uma caixa e escolha uma opção

```python
janela.CheckBoxControl(AutomationId="chkAceito").SetChecked(True)
janela.RadioButtonControl(AutomationId="rdB").GetSelectionItemPattern().Select()
```

### 4.6 Feche a janela

```python
janela.GetWindowPattern().Close()
```

> ✅ Todas as linhas acima foram **executadas e conferidas** no laboratório durante o estudo.

Pronto: você achou uma janela, apertou um botão, preencheu um campo, marcou opções e fechou. O resto deste guia é entender **por que** funciona e como fazer em programas reais.

---

## 5. 🌳 Como o robô "enxerga": a árvore de controles

Todo programa na tela é uma **árvore**:

```
Área de Trabalho (raiz)
 ├── Janela "Meu Programa"
 │    ├── Barra de título
 │    │    ├── Botão "Minimizar"
 │    │    ├── Botão "Maximizar"
 │    │    └── Botão "Fechar"
 │    ├── Barra de menu
 │    │    └── Menu "Arquivo"
 │    │         ├── Item "Novo"
 │    │         └── Item "Sair"
 │    ├── Campo de texto "Nome"
 │    ├── Caixa de seleção "Aceito os termos"
 │    └── Botão "Salvar"
 ├── Janela "Outro Programa"
 └── Barra de Tarefas
```

Cada "galho" é um **controle** (na biblioteca, um objeto `Control`). Um controle pode ser um botão, uma janela, um texto, um painel invisível que só agrupa coisas… tudo é controle.

### Propriedades: o "documento de identidade" de cada controle

Cada controle tem características que você pode consultar:

| Propriedade | Para que serve | Exemplo |
|---|---|---|
| `Name` | O nome visível/acessível | `"Salvar"` |
| `AutomationId` | Um código interno, **estável** (quando o programador define) | `"btnSalvar"` |
| `ClassName` | O "tipo técnico" do componente | `"Button"` |
| `ControlTypeName` | A categoria em português claro, digamos | `"ButtonControl"` |
| `BoundingRectangle` | O retângulo que ele ocupa na tela | `(100, 200, 180, 228)` |
| `IsEnabled` | Está habilitado? | `True` / `False` |
| `IsOffscreen` | Está fora da tela? | `False` |
| `ProcessId` | Número do processo (programa) dono | `4812` |
| `NativeWindowHandle` | O "número do documento" da janela no Windows (0 se não tiver) | `330406` |
| `IsPassword` | É campo de senha? | `True` |
| `FrameworkId` | Tecnologia do programa (`Win32`, `WPF`, `XAML`…) | `"Win32"` |

### Dica de ouro sobre identificar elementos

- **`AutomationId`** é o melhor critério: não muda com o idioma e raramente muda entre versões.
- **`Name`** é o mais intuitivo, mas muda de idioma (o botão "Open" vira "Abrir") e às vezes de versão.
- **Posição na tela** é o pior critério: muda com resolução, tamanho de janela e monitor.

### Como ver a árvore de qualquer janela

```python
for controle, profundidade in auto.WalkControl(janela, includeTop=True, maxDepth=4):
    print("  " * profundidade,
          controle.ControlTypeName, repr(controle.AutomationId), repr(controle.Name))
```

Isso imprime um "organograma" parecido com o desenho acima. É assim que você descobre o que existe numa janela antes de automatizar.

> ⚠️ Cuidado: isso imprime **textos reais** do programa. Se a janela tiver dados pessoais, eles aparecem no seu terminal.

---

## 6. 🔎 Encontrando elementos (a arte da busca)

A biblioteca cria um controle com **critérios de busca**:

```python
janela.ButtonControl(Name="Clicar")
```

### O detalhe mais importante: a busca é PREGUIÇOSA

Criar `janela.ButtonControl(Name="Clicar")` **não procura nada ainda**. Ela só anota os critérios. A busca de verdade acontece quando você **usa** o controle (lê uma propriedade, clica, etc.) ou chama `Exists()`.

Isso tem duas consequências boas e uma ruim:

- ✅ Você pode "declarar" todos os controles no início do script.
- ✅ Se a tela mudar, o controle se acha de novo quando preciso.
- ⚠️ Se o elemento não existir e você acessar uma propriedade, o Python **espera até 10 segundos** (o padrão) e então dá o erro `LookupError`.

### Todos os critérios de busca

| Critério | O que faz | Exemplo |
|---|---|---|
| `Name` | Nome exato | `Name="Salvar"` |
| `SubName` | O nome **contém** este trecho | `SubName="Salv"` |
| `RegexName` | Expressão regular (compara desde o **início**) | `RegexName="Salv.*"` |
| `ClassName` | Classe exata | `ClassName="Edit"` |
| `AutomationId` | Identificador exato | `AutomationId="txtNome"` |
| `foundIndex` | Qual ocorrência (1 = primeira) | `foundIndex=2` |
| `searchDepth` | Até quantos níveis descer | `searchDepth=1` |
| `Depth` | Só aceita **exatamente** neste nível | `Depth=2` |
| `Compare` | Sua própria função de decisão | `Compare=lambda c, d: c.IsPassword` |

Todos os critérios que você informar precisam ser verdadeiros ao mesmo tempo (é um "E").

### Exemplos com resultado conferido no laboratório ✅

```python
janela.ButtonControl(Name="Clicar")                    # achou btnClick
janela.ButtonControl(SubName="lic")                    # achou btnClick (contém "lic")
janela.ButtonControl(RegexName="Cl.*")                 # achou btnClick
janela.ButtonControl(RegexName="licar")                # NÃO acha: regex compara do começo
janela.CheckBoxControl(foundIndex=2)                   # a 2ª caixa de seleção (chkTri)
janela.EditControl(AutomationId="txtSenha")            # campo de senha
janela.Control(Compare=lambda c, d: c.IsPassword)      # qualquer coisa que seja senha
```

### O "Compare": sua regra personalizada

Quando os critérios prontos não bastam, escreva uma função que recebe `(controle, profundidade)` e responde `True`/`False`:

```python
botao_desabilitado = janela.Control(
    Compare=lambda c, d: c.ControlTypeName == "ButtonControl" and not c.IsEnabled
)
```

### Quanto mais perto do alvo, mais rápido

Procurar a partir do **Desktop inteiro** é lento (o robô visita elemento por elemento). Procure a partir de um ancestral próximo:

```python
# rápido: só dentro da janela já encontrada
janela.EditControl(AutomationId="txtNome")

# lento: vasculha o computador todo
auto.EditControl(AutomationId="txtNome")
```

### Existe? Sumiu?

```python
botao.Exists(5)         # espera até 5 s; True/False, sem dar erro
botao.Exists(0, 0)      # testa agora, sem esperar
botao.Disappears(5)     # True quando deixar de existir
botao.Refind()          # procura de novo; dá erro se não achar
```

---

## 7. 🎯 Agindo: os três jeitos de fazer algo acontecer

Existe uma **hierarquia de confiabilidade**. Use de cima para baixo:

### 🥇 1º — Patterns (a "habilidade" do elemento)

O robô pede *educadamente* ao programa: *"por favor, invoque este botão"*. Não usa mouse nem teclado e, em geral, não precisa de foco, podendo funcionar até com a janela em segundo plano (regra geral do UI Automation; no laboratório os testes rodaram sem eu tocar no mouse, mas não testei janela escondida atrás de outras).

```python
botao.GetInvokePattern().Invoke()
```

### 🥈 2º — Atalhos "do sistema" (MSAA / Legacy)

Programas antigos às vezes só entendem uma linguagem mais velha, o `LegacyIAccessible`:

```python
botao.GetLegacyIAccessiblePattern().DoDefaultAction()
```

### 🥉 3º — Mouse e teclado simulados

O robô realmente move o mouse e aperta teclas, como se fosse você.

```python
botao.Click()
auto.SendKeys("{Ctrl}a")
```

Funciona em quase tudo, mas é o **mais frágil**: depende de a janela estar em foco, visível, no monitor certo, e **mexe no seu mouse e teclado de verdade**. Se você mexer no computador durante a execução, tudo se embaralha.

> **Regra prática:** se um pattern funciona, use o pattern. Só desça de nível se for necessário.

---

## 8. 🧩 Os patterns: as "habilidades" de cada elemento

Pense em cada elemento como um personagem de jogo com habilidades. Um botão sabe ser **invocado**. Uma caixa de seleção sabe **alternar**. Um campo de texto sabe **guardar um valor**. Cada habilidade é um *pattern*.

Para pedir uma habilidade:

```python
pattern = elemento.GetPattern(auto.PatternId.InvokePattern)
if pattern:
    pattern.Invoke()
```

Ou use os atalhos prontos, como `elemento.GetInvokePattern()`. **Sempre teste `if pattern:`**: se o elemento não tiver a habilidade, o resultado é `None`.

### As habilidades mais úteis (com analogia)

| Pattern | Analogia | O que você faz |
|---|---|---|
| **Invoke** | "Apertar" | `Invoke()` clica botões, links, itens de menu |
| **Value** | "Caixinha com texto" | `Value` (ler) e `SetValue("texto")` (escrever) |
| **Toggle** | "Interruptor" | `ToggleState` (0 desligado, 1 ligado, 2 indefinido), `Toggle()`, `SetToggleState()` |
| **SelectionItem** | "Escolher um item" | `Select()`, `AddToSelection()`, `RemoveFromSelection()`, `IsSelected` |
| **Selection** | "A lista de escolhidos" | `GetSelection()` devolve os itens selecionados |
| **ExpandCollapse** | "Sanfona" | `Expand()`, `Collapse()`, `ExpandCollapseState` |
| **RangeValue** | "Controle deslizante" | `Value`, `Minimum`, `Maximum`, `SetValue()` |
| **Scroll** | "Barra de rolagem" | `Scroll()`, `SetScrollPercent()`, percentuais |
| **ScrollItem** | "Trazer para a vista" | `ScrollIntoView()` |
| **Window** | "A janela em si" | `Close()`, `SetWindowVisualState()` (minimizar/maximizar), `IsModal` |
| **Transform** | "Mover/redimensionar" | `Move()`, `Resize()`, `CanMove`, `CanResize` |
| **Text** | "Documento de texto rico" | ler trechos, achar palavras, atributos de formatação |
| **Grid / Table** | "Planilha" | `RowCount`, `ColumnCount`, `GetItem(linha, coluna)`, cabeçalhos |
| **LegacyIAccessible** | "Dialeto antigo" | `Name`, `Value`, `DoDefaultAction()`, `SetValue()` |

A biblioteca conhece **34 patterns** ao todo. A lista completa, com cada método, está em [`docs/05-patterns.md`](docs/05-patterns.md).

### Os estados numéricos (para não ficar perdido)

```python
auto.ToggleState.Off            # 0
auto.ToggleState.On             # 1
auto.ToggleState.Indeterminate  # 2  (caixa de "meio marcada")

auto.ExpandCollapseState.Collapsed  # 0  (fechado)
auto.ExpandCollapseState.Expanded   # 1  (aberto)
auto.ExpandCollapseState.LeafNode   # 3  (não tem filhos)

auto.WindowVisualState.Normal       # 0
auto.WindowVisualState.Maximized    # 1
auto.WindowVisualState.Minimized    # 2
```

### O que aprendemos testando cada habilidade ✅

- **Invoke**: dispara o evento do programa de verdade (o clique "contou").
- **SetValue (Value)**: dispara o evento de "texto mudou" do programa — não é só pintar texto na tela. Acentos funcionam.
- **Campo de senha**: o robô **não consegue ler** o valor (volta vazio), mas consegue **escrever** nele.
- **Toggle em caixa de 3 estados**: o ciclo é *ligado → indefinido → desligado → ligado*.
- **Barra de progresso**: dá para ler (valor, mínimo, máximo), mas tentar escrever dá erro (é somente leitura).
- **Seleção**: `Select()` troca a seleção; `AddToSelection()` acrescenta outro item; `RemoveFromSelection()` tira.
- **Janela**: `Close()` fecha a janela como se você clicasse no X.

---

## 9. 📚 Catálogo dos tipos de controle

A biblioteca tem uma classe para cada "tipo" de coisa que pode existir na tela. Em português claro:

| Classe | O que é | Exemplo no dia a dia |
|---|---|---|
| `WindowControl` | Janela | Uma janela de programa |
| `PaneControl` | Painel genérico | Áreas internas, o próprio Desktop |
| `ButtonControl` | Botão | OK, Cancelar |
| `CheckBoxControl` | Caixa de seleção | ☑ Aceito os termos |
| `RadioButtonControl` | Botão de opção | ◉ Masculino ○ Feminino |
| `EditControl` | Campo de texto | Caixa de digitação |
| `ComboBoxControl` | Lista suspensa | Escolha uma cor ▾ |
| `ListControl` / `ListItemControl` | Lista e seus itens | Caixa de listagem |
| `TreeControl` / `TreeItemControl` | Árvore e seus galhos | Explorador de pastas |
| `TabControl` / `TabItemControl` | Conjunto de abas e cada aba | Abas de configuração |
| `MenuBarControl` / `MenuControl` / `MenuItemControl` | Barra de menu, menu, item de menu | Arquivo > Novo |
| `TextControl` | Texto estático (rótulo) | "Nome:" |
| `HyperlinkControl` | Link | Texto clicável |
| `ProgressBarControl` | Barra de progresso | Carregando… 45% |
| `SliderControl` | Controle deslizante | Volume |
| `SpinnerControl` | Contador com setinhas | Quantidade ▲▼ |
| `TableControl` / `DataGridControl` / `DataItemControl` | Tabelas, grades e células | Planilhas, grades de dados |
| `StatusBarControl` | Barra de status | Rodapé da janela |
| `ToolBarControl` | Barra de ferramentas | Ícones no topo |
| `TitleBarControl` | Barra de título | Onde fica o nome da janela |
| `GroupControl` | Grupo/moldura | Caixa "Dados pessoais" |
| `ImageControl` | Imagem | Figuras |
| `ScrollBarControl`, `ThumbControl` | Barra de rolagem e sua alça | |
| `ToolTipControl` | Dica flutuante | Balãozinho ao parar o mouse |
| `DocumentControl` | Documento rico | Editor de texto |
| `CalendarControl` | Calendário | Seleção de data |
| `HeaderControl` / `HeaderItemControl` | Cabeçalho de tabela e suas colunas | |
| `SplitButtonControl` | Botão com seta ao lado | |
| `SeparatorControl` | Linha separadora | |
| `CustomControl` | Algo "personalizado" | Componentes próprios do programa |
| `AppBarControl`, `SemanticZoomControl` | Tipos modernos (Windows 8+) | |

**Importante:** o tipo que o programa *declara* nem sempre é o que você imagina. No laboratório, por exemplo, um "seletor numérico" apareceu como `ComboBox` (com um `Spinner` e um `Edit` dentro), e uma "grade de dados" apareceu como `Table` cheia de `Custom` (as linhas) com `DataItem` dentro (as células). **Olhe a árvore antes de assumir.**

### Quem é "obrigado" a ter qual habilidade?

A Microsoft define regras: por exemplo, um `CheckBox` **deve** ter Toggle; um `Window` **deve** ter Window e Transform; já um `Button` **pode** ter Invoke. Mas atenção: **a regra é a teoria; o que vale é o que o programa realmente implementa**. Veja a matriz completa em [`docs/04-controles-especificos.md`](docs/04-controles-especificos.md).

---

## 10. 🍳 Receitas prontas (copiar e usar)

> ✅ = executado e conferido no laboratório · 📖 = montado a partir do código-fonte, revise antes de usar em produção.

### 10.1 Esqueleto de qualquer script ✅

```python
import uiautomation as auto

auto.Logger.SetLogFile("")          # NÃO gravar arquivo de log (veja a seção de armadilhas)
auto.SetGlobalSearchTimeout(5)      # timeout global (padrão: 10 s)

janela = auto.WindowControl(searchDepth=1, Name="Título da janela")
if not janela.Exists(10):
    raise RuntimeError("A janela não apareceu em 10 segundos")
```

### 10.2 Clicar um botão ✅

```python
janela.ButtonControl(AutomationId="btnClick").GetInvokePattern().Invoke(waitTime=0)
```

Se não tiver `Invoke`, tente na ordem:

```python
botao.GetLegacyIAccessiblePattern().DoDefaultAction()   # 📖
botao.Click()                                           # último recurso (usa o mouse)
```

### 10.3 Preencher um formulário ✅

```python
janela.EditControl(AutomationId="txtNome").GetValuePattern().SetValue("Maria da Silva")
janela.CheckBoxControl(AutomationId="chkAceito").SetChecked(True)
janela.RadioButtonControl(AutomationId="rdA").GetSelectionItemPattern().Select()
```

### 10.4 Escolher um item numa lista ✅

```python
lista = janela.ListControl(AutomationId="lstItens")
lista.ListItemControl(Name="Item 3").GetSelectionItemPattern().Select()

escolhidos = [c.Name for c in lista.GetSelectionPattern().GetSelection()]
print(escolhidos)         # ['Item 3']
```

### 10.5 Trocar de aba ✅

```python
janela.TabControl().TabItemControl(Name="Aba Dois").GetSelectionItemPattern().Select()
```

### 10.6 Abrir/fechar um galho de árvore ✅

```python
galho = janela.TreeItemControl(Name="Raiz A")
galho.GetExpandCollapsePattern().Expand()
print([f.Name for f in galho.GetChildren()])    # ['Filho A1', 'Filho A2']
galho.GetExpandCollapsePattern().Collapse()
```

### 10.7 Ler uma tabela 📖

Estrutura observada no laboratório: `Table → Custom (cada linha) → DataItem (cada célula)`.

```python
grade = janela.TableControl(AutomationId="dgvDados")
linhas = []
for linha in grade.GetChildren():
    celulas = [c for c in linha.GetChildren()
               if c.ControlType == auto.ControlType.DataItemControl]
    linhas.append([
        (c.GetValuePattern().Value if c.GetValuePattern() else c.Name)
        for c in celulas
    ])
print(linhas)
```

### 10.8 Esperar um diálogo aparecer e confirmar 📖

```python
dialogo = auto.WindowControl(searchDepth=1, RegexName=r".*Confirma.*")
if dialogo.Exists(8):
    dialogo.ButtonControl(Name="Sim").GetInvokePattern().Invoke()
```

### 10.9 Fechar, minimizar, maximizar ✅/📖

```python
janela.GetWindowPattern().Close()                                    # ✅ fecha
janela.Minimize(); janela.Maximize(); janela.Restore()               # 📖
janela.SetTopmost(True)                                              # 📖 sempre no topo
janela.GetWindowPattern().SetWindowVisualState(auto.WindowVisualState.Minimized)  # 📖
```

### 10.10 Descobrir o que está sob o mouse 📖

```python
c = auto.ControlFromCursor()
print(c)                              # o elemento embaixo do cursor
print(c.GetTopLevelControl())         # a janela dele
auto.EnumAndLogControlAncestors(c)    # a "linhagem" completa, do Desktop até ele
```

### 10.11 Rodar o robô em outra thread 📖

```python
import threading, uiautomation as auto

def trabalho():
    with auto.UIAutomationInitializerInThread():     # obrigatório em threads
        janela = auto.WindowControl(searchDepth=1, Name="X")
        ...

threading.Thread(target=trabalho).start()
```

### 10.12 Botão de emergência (parar com um atalho) 📖

```python
def tarefa(parar):
    while not parar.is_set():
        ...                       # faça um pedaço do trabalho
        parar.wait(0.5)

auto.RunByHotKey(
    {(auto.ModifierKey.Control, auto.Keys.VK_1): tarefa},                   # Ctrl+1 inicia
    stopHotKey=(auto.ModifierKey.Control | auto.ModifierKey.Shift,
                auto.Keys.VK_2),                                            # Ctrl+Shift+2 para
)
# Ctrl+D encerra o programa por inteiro (padrão)
```

> ⚠️ `RunByHotKey` termina o processo Python ao sair (usa `os._exit(0)`).

---

## 11. 🖱️⌨️ Mouse e teclado "de verdade"

### Mouse

| Quero… | Código |
|---|---|
| Clicar no centro de um controle | `controle.Click()` |
| Clicar em outro ponto do controle | `controle.Click(10, 10)` (10 px do canto superior esquerdo) |
| Clicar perto do canto oposto | `controle.Click(-10, -10)` (negativo = a partir do canto inferior direito) |
| Clicar numa proporção | `controle.Click(ratioX=0.9, ratioY=0.5)` |
| Botão direito / meio / duplo clique | `RightClick()`, `MiddleClick()`, `DoubleClick()` |
| Arrastar e soltar | `controle.DragDrop(x1, y1, x2, y2)` |
| Rolar | `controle.WheelDown(wheelTimes=3)`, `WheelUp()` |
| Clicar em coordenada absoluta da tela | `auto.Click(x, y)` |
| Mover o cursor | `auto.MoveTo(x, y)` (animado) ou `auto.SetCursorPos(x, y)` (instantâneo) |
| Saber onde está o cursor | `auto.GetCursorPos()` |

Dicas:

- O mouse "voa" suavemente até o alvo (para parecer natural). Para acelerar: `simulateMove=False` em cada chamada, ou `auto.uiautomation.MAX_MOVE_SECOND = 0`.
- Se o controle tem largura ou altura **zero** (invisível), o clique é **ignorado** e um aviso em amarelo aparece.

### Teclado: `SendKeys`

`SendKeys` digita como uma pessoa. Texto normal é digitado direto; **teclas especiais vão entre chaves** `{ }`.

```python
auto.SendKeys("Olá, mundo!{Enter}")
auto.SendKeys("{Ctrl}a{Delete}")          # Ctrl+A, depois Delete
auto.SendKeys("{Ctrl}{Shift}s")           # Ctrl+Shift+S
auto.SendKeys("{Tab 3}{Enter}")           # 3 Tabs e Enter
auto.SendKeys("{Alt}{F4}")                # Alt+F4
auto.SendKeys("{Win}d")                   # Windows+D (mostrar desktop)
```

#### Folha de cola do `SendKeys`

| Quero… | Escreva |
|---|---|
| Uma tecla especial | `{Enter}`, `{Tab}`, `{Esc}`, `{Space}`, `{Delete}`, `{Back}` (backspace), `{Home}`, `{End}`, `{PageUp}`, `{PageDown}`, `{Left}`, `{Right}`, `{Up}`, `{Down}`, `{F1}`…`{F24}` |
| Repetir | `{Tab 5}` (5 vezes) |
| Atalho com Ctrl / Shift / Alt / Win | `{Ctrl}c`, `{Shift}{Tab}`, `{Alt}{F4}`, `{Win}e` |
| Vários modificadores | `{Ctrl}{Shift}s` |
| Segurar durante um grupo de teclas | `{Ctrl}(ab)` (Ctrl enquanto aperta A e B) |
| Digitar `{` ou `}` | `{{}` e `{}}` |
| Digitar `(` ou `)` soltos | `(` e `)` (fora de grupos já são normais) ou `{(}` `{)}` |

**Pegadinhas do `SendKeys`:**

- O nome da tecla Backspace é **`{Back}`** (não existe `{Backspace}`) e o de Caps Lock é **`{Capital}`** (não existe `{CapsLock}`).
- `SendKeys("")` (texto vazio) **dá erro** — proteja com `if texto:`.
- `{Ctrl}A` (A maiúsculo) é Ctrl+A **sem Shift**. Para Ctrl+Shift+A: `{Ctrl}{Shift}a`.
- Letras e símbolos soltos são digitados como "caracteres Unicode" (funciona em qualquer layout de teclado, mas alguns programas e jogos só reagem a teclas "físicas").
- `SendKeys` digita **onde estiver o foco**. Se o foco mudar no meio, o texto vai parar em outro programa.

### Antes de digitar, confirme o foco 📖

```python
if auto.GetForegroundWindow() != janela.NativeWindowHandle:
    janela.SetActive()
assert auto.GetForegroundWindow() == janela.NativeWindowHandle   # aborta se não conseguiu
```

(O Windows pode recusar trazer uma janela para frente se outro programa está em primeiro plano. Por isso o `assert`.)

---

## 12. 🪟 Janelas, tela, clipboard e processos

### Janelas (por controle) 📖

```python
janela.SetActive()       # traz para frente
janela.Maximize()  /  janela.Minimize()  /  janela.Restore()
janela.MoveToCenter()    # centraliza no monitor principal
janela.SetTopmost(True)  # fica sempre por cima
janela.MoveWindow(x, y, largura, altura)
```

### Tela e monitores ✅

```python
auto.GetScreenSize()         # monitor principal, ex.: (2560, 1440)
auto.GetVirtualScreenSize()  # todos os monitores juntos
auto.GetMonitorsRect()       # um retângulo por monitor (a ordem NÃO é "principal primeiro")
```

Se você usa vários monitores, atenção: `MoveToCenter` e `GetScreenSize` olham só o principal.

### Área de transferência (clipboard)

```python
auto.SetClipboardText("texto")          # 📖 copia texto (SOBRESCREVE o que o usuário tinha!)
print(auto.GetClipboardText())          # 📖
print(auto.GetClipboardFormats())       # ✅ lista os formatos que estão lá agora
auto.SetClipboardHtml("<b>negrito</b>") # 📖
```

> ⚠️ Mexer no clipboard apaga o que o usuário tinha copiado. Se isso importa, **leia e guarde antes, e restaure depois**.
> ⚠️ Há um bug conhecido: ler texto quando o clipboard só tem imagem deixa o clipboard "preso" pelo seu programa. Confira antes com `GetClipboardFormats()`. Detalhes na seção de armadilhas.

### Processos (programas em execução) ✅/📖

```python
for p in auto.GetProcesses():                  # ✅ lista processos
    print(p.pid, p.exeName)                    # p.exePath e p.cmdLine podem vir vazios sem admin

auto.TerminateProcessByName("notepad.exe")     # 📖 ENCERRA à força. Cuidado!
```

### Quem sou eu? 📖

```python
auto.IsUserAnAdmin()        # estou rodando como administrador?
auto.IsDesktopLocked()      # a tela está bloqueada (Win+L)?
```

---

## 13. 📸 Prints e imagens

```python
janela.CaptureToImage("janela.png")                    # print da janela inteira
botao.CaptureToImage("botao.png")                      # print só do botão

with janela.ToBitmap(0, 0, 200, 100) as img:           # um recorte de 200x100 do canto
    img.ToFile("recorte.jpg", quality=90)
```

### O detalhe que surpreende

O print é uma **cópia dos pixels visíveis na tela**. Isso significa que:

- se outra janela estiver **por cima**, o print mostra a outra janela;
- se a janela estiver **minimizada** ou fora da tela, o resultado é inútil.

Para tirar print de uma janela, traga-a para frente antes (`SetActive()`).

### Outras coisas que a classe `Bitmap` faz 📖

- Abrir arquivos (`Bitmap.FromFile`), converter para **PIL** (`ToPILImage`) e **numpy/OpenCV** (`ToNDArray`).
- Ler e escrever pixels (`GetPixelColor`, `SetPixelColor`, `GetPixelColorsOfRect`…).
- Cortar (`Copy`), colar uma imagem em outra (`Paste`), redimensionar (`Resize`), girar (`Rotate`, `RotateFlip`).
- Criar GIFs animados (`GIF.ToGifFile`) e TIFFs de várias páginas.
- **Fechar** o bitmap (`Close()` ou `with`) libera a memória nativa; esqueça disso e a memória vaza.

Cores: as funções de `Bitmap` usam **ARGB** (`0xAARRGGBB`); a função `GetPixelColor` do Windows (a global e a do `Control`) devolve **BGR**. Não misture.

---

## 14. ⏱️ Esperas, tempo limite e erros

### Os três relógios

| Relógio | Valor padrão | O que controla |
|---|---|---|
| `TIME_OUT_SECOND` | **10 s** | Quanto tempo esperar ao **acessar** um controle que ainda não foi achado. Mude com `auto.SetGlobalSearchTimeout(5)`. |
| `SEARCH_INTERVAL` | 0,5 s | Pausa entre tentativas de busca |
| `OPERATION_WAIT_TIME` | 0,5 s | Pausa **depois** de cada ação (clique, invocar, digitar…) |

Esses 0,5 s depois de cada ação somam rápido. Em sequências longas, passe `waitTime=0`:

```python
botao.GetInvokePattern().Invoke(waitTime=0)
campo.GetValuePattern().SetValue("texto", 0)
```

> ⚠️ **Pegadinha:** se você mudar `OPERATION_WAIT_TIME` ou `SEARCH_INTERVAL` *depois* do `import`, isso **não** afeta os valores padrão já gravados nas funções. Passe `waitTime=` explicitamente. (O timeout global e `MAX_MOVE_SECOND` são lidos na hora e funcionam normalmente.)

### O erro mais comum: `LookupError`

```
LookupError: Find Control Timeout(10s): {Name: 'Salvar', ControlType: ButtonControl}
```

Significa: *"esperei 10 segundos e não achei nenhum botão chamado Salvar"*. Causas típicas: nome diferente, o elemento ainda não apareceu, está num nível mais profundo que o `searchDepth`, ou pertence a outra janela.

Como lidar:

```python
botao = janela.ButtonControl(Name="Salvar")
if botao.Exists(5):
    botao.GetInvokePattern().Invoke()
else:
    print("Não achei o botão; veja a árvore.")
```

### Espere por estado, não por tempo fixo

Em vez de `time.sleep(5)` "por garantia":

```python
botao_ok = dialogo.ButtonControl(Name="OK")
if botao_ok.Exists(10):          # continua assim que aparecer
    ...
```

---

## 15. 💡 Truques e boas práticas

1. **Comece o script com `auto.Logger.SetLogFile("")`.** Por padrão a biblioteca escreve um arquivo de log com o conteúdo das telas.
2. **Prefira `AutomationId` a `Name`.** Não muda com o idioma.
3. **Limite a busca**: `searchDepth=1` para janelas; procure a partir da janela, não do Desktop.
4. **Guarde o controle achado em uma variável** e reutilize.
5. **Patterns primeiro, mouse e teclado por último.**
6. **Teste com o laboratório** antes de usar no programa real.
7. **Nunca automatize testando "ao vivo" em produção** (sistema real, dados reais) sem um ambiente de teste.
8. **Use `.Exists(timeout)` em vez de `sleep`.**
9. **Desligue a animação do mouse** quando precisar de velocidade (`MAX_MOVE_SECOND = 0`).
10. **Faça o robô "falar" o que está fazendo** (`print`) para depurar depois.
11. **Coloque um botão de emergência** (hotkey) em qualquer robô que use mouse e teclado.
12. **Não use o computador enquanto o robô usa mouse/teclado.** Se precisar, rode numa máquina/VM dedicada.
13. **Trate o `None`**: `GetPattern` devolve `None` quando o elemento não tem a habilidade.
14. **Teste de leitura é de graça; teste de escrita não.** Primeiro leia (`.Name`, `.Value`), depois escreva.
15. **Janela de outra conta/administrador**: um Python sem privilégios normalmente não consegue operar janelas elevadas (isso é regra geral do Windows; não foi testado neste estudo).

---

## 16. ⚠️ Armadilhas e bugs que ninguém te conta

Aqui está a parte que mais vale o tempo de leitura. São coisas que encontrei **lendo o código** (📖) ou **testando** (🧪).

### 16.1 Comportamentos que surpreendem

| # | Surpresa | Como se proteger |
|---|---|---|
| 1 | **A biblioteca grava um arquivo `@AutomationLog.txt`** na pasta atual, com logs que podem incluir textos das telas. 🧪 | `auto.Logger.SetLogFile("")` |
| 2 | **Importar a biblioteca muda configurações do processo** (consciência de DPI e algumas funções do Windows). 📖 | Saiba disso se misturar com outras bibliotecas gráficas |
| 3 | **Acessar um controle que não existe trava até 10 s** e dá erro. 🧪 | `Exists(0, 0)` para testar sem esperar |
| 4 | **`RegexName` compara desde o início** da frase. 🧪 | Use `.*trecho.*` para "contém" |
| 5 | **Parâmetro de busca inventado é ignorado em silêncio** (`Foo="bar"` não filtra nada). 🧪 | Use só os critérios da tabela da seção 6 |
| 6 | **`Name` nem sempre é o texto exibido**: se o programa define um "nome de acessibilidade", ele vence. 🧪 | Leia o conteúdo por `Value`/`Text` |
| 7 | **Os índices `janela[3]` mudam** se o programa mudar. 🧪 | Prefira `AutomationId` |
| 8 | **Elementos fora da tela podem ter tamanho zero** e o clique é ignorado. 🧪 | `ScrollIntoView()` antes |
| 9 | **A lista "multisseleção" pode mentir**: `CanSelectMultiple` voltou `False` mas aceitava vários. 🧪 | Teste de verdade |
| 10 | **Campos de senha não podem ser lidos**, só escritos. 🧪 | É proposital |
| 11 | **`GetWindowText` corta em 260 caracteres.** 📖 | Use `GetEditText(handle)` ou `ValuePattern` |
| 12 | **Os cliques e teclas vão para o que estiver em foco.** | Confirme o foco antes |
| 13 | **O print captura o que está visível na tela.** 📖 | Traga a janela para frente |
| 14 | **`EnumProcessByWMI` exige instalar `wmi`.** 🧪 | `pip install wmi` |
| 15 | **A árvore percorrida é a "Raw View"** (mostra mais elementos que a ferramenta Inspect "Control View"). 📖 | Use a própria biblioteca para olhar a árvore |

### 16.2 Bugs reais no código da biblioteca (versão 2.0.29)

Encontrados lendo o código-fonte. Útil se você algum dia ver um erro estranho:

| Onde | O que acontece |
|---|---|
| `TextPattern.RangeFromChild` | Passa o objeto errado (a classe em vez do elemento); não funciona |
| `TextRange.CompareEndpoints` | Passa o objeto errado; dá erro |
| `TableControl.GetTableItemsValue` | Usa `> 0` onde devia ser `>= 0`: a **linha 0 e a coluna 0 nunca são selecionáveis** |
| `GetClipboardText/Html/Bitmap` | Não fecham o clipboard quando o formato pedido não existe → clipboard preso |
| `Control.DoubleClick` | Quebra (`TypeError`) se o controle tem tamanho zero |
| `SendKeys("")` | Dá `IndexError` |
| `SendKeys` com `{RControl}` | Não "segura" a tecla como as outras de modificador |
| `WalkControl(maxDepth=0, includeTop=True)` | Ainda devolve o topo 🧪 |
| `GIF.ToGifFile(path, bitmaps)` | O parâmetro `delays` é opcional na assinatura, mas omitir dá erro |
| `Rect` | Não pode ser usado como chave de dicionário; `rect == None` dá erro |
| `ProcessInfo.__str__` | Esquece de fechar o parêntese (só estético) |

A lista completa e comentada está em [`docs/08-bugs-e-pegadinhas.md`](docs/08-bugs-e-pegadinhas.md).

---

## 17. 🔬 Como descobrir os "nomes" dos elementos (depuração)

Antes de escrever o robô, você precisa **ver** o que o Windows enxerga. Três caminhos:

### 17.1 A própria biblioteca (já instalada)

```python
# Despeje a árvore de uma janela:
for c, d in auto.WalkControl(janela, includeTop=True, maxDepth=6):
    print("  " * d, c.ControlTypeName, repr(c.AutomationId), repr(c.Name), c.ClassName)
```

(`auto.EnumAndLogControl(janela)` mostra mais detalhes, mas **grava no arquivo de log** e consulta 34 patterns por elemento: é bem mais lento.)

### 17.2 Ferramentas gráficas gratuitas da Microsoft

- **Accessibility Insights for Windows** — gratuita, mostra a árvore e as propriedades de qualquer elemento ao passar o mouse.
- **Inspect.exe** — vem no Windows SDK. Use o modo UIA.

### 17.3 "O que está debaixo do mouse?"

```python
c = auto.ControlFromCursor()
print(c)
```

### Checklist quando "não acha o elemento"

1. O programa roda como **administrador** e o seu Python não?
2. O elemento está **fora da tela/virtualizado** (listas longas)? Use `ScrollIntoView()`.
3. O app é **Electron / Chromium / Java / Qt / jogo**? A árvore pode ser mínima (regra geral).
4. O `Name` mudou por **idioma**?
5. O `searchDepth` está **curto demais**?
6. É um **popup**? Muitos popups são filhos do Desktop, não da janela: procure de `auto.GetRootControl()` com `searchDepth=1`.
7. Está em **outro monitor**?
8. Despeje a árvore e compare com o que você esperava.

---

## 18. 🛡️ Segurança, ética e bom senso

Automação é poder. Algumas regras de convivência:

- **Só automatize o que você tem direito de usar.** Leia os termos de uso do programa. Muitos contratos proíbem automação.
- **Prefira canais oficiais** (APIs, exportações, integrações do fabricante) sempre que existirem.
- **Não burle proteções** (CAPTCHAs, bloqueios de segurança, limites de uso). Não é o propósito da ferramenta e pode ser crime ou quebra de contrato.
- **Dados pessoais (LGPD):** se o robô lê telas com dados de clientes, ele está tratando dados pessoais. Não grave em logs, não envie para terceiros, não deixe em arquivos soltos.
- **Senhas:** não coloque senhas no código-fonte. Use variáveis de ambiente ou um cofre de senhas.
- **Cuidado com o repositório público:** nunca suba logs (`@AutomationLog.txt`), prints de tela com dados reais ou arquivos de configuração com segredos. Se você versiona o seu projeto, coloque `@AutomationLog.txt` e a pasta `.venv` no `.gitignore`.
- **Ações destrutivas** (excluir, enviar, pagar, encerrar processos à força): sempre teste antes em ambiente de teste e exija confirmação.
- **Quem opera um robô responde por ele.** Se ele errar, o erro é seu.

---

## 19. ❓ Perguntas frequentes

**Funciona em Mac ou Linux?**
Não. É exclusivo do Windows.

**Precisa ser administrador?**
Para a maioria dos casos, não. Mas um Python comum normalmente não consegue operar janelas de programas executados como administrador (regra geral do Windows). Nesse caso, rode o Python também como administrador (a biblioteca tem `RunScriptAsAdmin`, que pede a confirmação do Windows).

**Funciona com a tela bloqueada ou em segundo plano?**
Os *patterns* (Invoke, Value, etc.) normalmente funcionam com a janela em segundo plano. Mouse e teclado simulados exigem que a janela esteja visível e em foco. Tela bloqueada geralmente impede entrada simulada (`IsDesktopLocked()` serve para detectar).

**Funciona em sites?**
Dá para ler o navegador, mas não é o caminho ideal. Use ferramentas de navegador (Selenium/Playwright).

**Funciona em programas feitos com Electron (VS Code, Discord…)?**
Esses programas usam o motor do Chromium e costumam expor a árvore só de forma limitada; pode ser necessário ativar a acessibilidade deles. É regra geral, não testei neste estudo.

**É lento?**
A busca percorre a árvore elemento por elemento, então depende do tamanho dela. Limite a busca (`searchDepth`, procurar a partir da janela) e use patterns em vez de mouse.

**Posso rodar vários robôs ao mesmo tempo?**
Em threads, sim, com `UIAutomationInitializerInThread`. Mas mouse e teclado são **um só** para o computador inteiro: dois robôs usando mouse/teclado vão brigar.

**Meu robô parou de funcionar depois de uma atualização do programa.**
Normal. Procure por `AutomationId` (mais estável que `Name`), reveja a árvore e ajuste.

**Posso usar com Excel/Word?**
Dá, mas para planilhas e documentos existem bibliotecas bem melhores que lidam com o arquivo direto (openpyxl, python-docx…) ou o suporte COM do próprio Office. Use UI Automation só se o outro caminho não servir.

**O `python -m uiautomation.uiautomation` é uma ferramenta de inspeção?**
**Não**, e não rode. O final do arquivo tem um bloco de demonstração que abre o Bloco de Notas e **digita um texto na janela que estiver em foco**.

**Como atualizo a biblioteca?**
`.\.venv\Scripts\python.exe -m pip install --upgrade uiautomation`. Revise as armadilhas, o comportamento pode mudar entre versões. Este guia foi feito na **2.0.29**.

---

## 20. 📖 Glossário em português claro

| Termo | Significado simples |
|---|---|
| **UI Automation** | Recurso do Windows que descreve os elementos da tela para outros programas (feito para acessibilidade) |
| **Controle / elemento** | Qualquer "peça" da tela: botão, campo, janela, texto… |
| **Árvore** | A hierarquia dos controles (janela → painéis → botões…) |
| **Pattern (padrão)** | Uma "habilidade" que um controle sabe fazer (ser invocado, ter valor, expandir…) |
| **AutomationId** | O código interno e estável de um controle |
| **ClassName** | O tipo técnico do componente |
| **Handle (HWND)** | O "número do documento" de uma janela no Windows |
| **Foco** | Qual janela/campo vai receber o que você digitar |
| **Foreground / primeiro plano** | A janela ativa, por cima das outras |
| **Top-level** | Janela de nível mais alto (não é filha de outra) |
| **DPI** | Densidade da tela; afeta o tamanho dos pixels e das coordenadas |
| **Virtualizado** | Item de lista que só existe de verdade quando aparece na tela (para economizar memória) |
| **Raw View** | A visão "crua" da árvore, com todos os elementos (inclusive os pouco importantes) |
| **MSAA / Legacy** | O sistema de acessibilidade antigo, ainda usado por muitos programas |
| **COM** | Tecnologia do Windows pela qual programas conversam entre si |
| **Thread** | Uma "linha de execução"; programas podem ter várias ao mesmo tempo |
| **Hotkey** | Atalho global de teclado (funciona em qualquer janela) |
| **Clipboard** | A área de transferência (Ctrl+C / Ctrl+V) |
| **Venv** | Ambiente virtual do Python; uma "caixinha" isolada de bibliotecas |
| **Timeout** | Tempo máximo de espera antes de desistir |
| **Lazy (preguiçoso)** | Que só faz o trabalho na hora de usar (a busca de controles é assim) |

---

## 21. 🗂️ Onde está a documentação técnica

Este repositório tem **só documentação**. Os exemplos de código para cada parte estão aqui neste README.

```
UiAutomation-Doc/
├── README.md                          ← este guia (com os exemplos)
└── docs/                              ← documentação técnica detalhada
    ├── README.md                       índice da documentação
    ├── 01-arquitetura.md               como a biblioteca é montada
    ├── 02-constantes-e-enums.md        todas as constantes
    ├── 03-control.md                   a classe Control em detalhe
    ├── 04-controles-especificos.md     os 40 tipos e a matriz de habilidades
    ├── 05-patterns.md                  os 34 patterns
    ├── 06-funcoes-win32.md             mouse, teclado, janelas, processos, hotkeys
    ├── 07-bitmap-clipboard-logger.md   imagens, clipboard, logs
    ├── 08-bugs-e-pegadinhas.md         bugs e comportamentos surpreendentes
    ├── 09-dicas-e-receitas.md          receitas e depuração
    ├── 10-referencia-api-completa.md   TODAS as funções, classes e métodos
    └── 11-internos-algoritmos.md       como tudo funciona por dentro
```

Quer se aprofundar? Comece por [`docs/README.md`](docs/README.md). Leitura sugerida: **01 → 03 → 05 → 08 → 09**. Os demais servem de consulta.

---

## 22. 🧪 Como este estudo foi feito (e o que é certeza, o que é suposição)

Transparência é importante, ainda mais num material público.

### O método

1. **Instalação** da biblioteca (versão 2.0.29) em um ambiente virtual.
2. **Inventário automático**: um script percorreu o código e listou 140 classes, 549 métodos/propriedades e 117 funções.
3. **Leitura integral do código-fonte** (um único arquivo de ~10.800 linhas), seção por seção: constantes, funções do Windows, mouse, teclado, janelas, processos, clipboard, `Bitmap`, os 34 patterns, a classe `Control` e todos os 40 tipos de controle.
4. **Laboratório próprio** (`UIA-LAB`, o código está na seção 4): uma janela com um exemplar de cada controle para testar os patterns, a busca e a navegação sem tocar em programas reais.
5. **Segunda passada de leitura**, mais profunda, só no código, sobre os pontos que não foram testados.

### As etiquetas que você viu pelo texto

| Selo | Significa |
|---|---|
| ✅ / 🧪 | **Executado e conferido** no laboratório |
| 📖 | **Deduzido lendo o código-fonte** (não executado) |

### O que NÃO foi testado

- Cliques e digitação **reais** de mouse/teclado (propositalmente, para não interferir no computador em uso). O funcionamento deles está descrito pelo código-fonte.
- Programas além do laboratório (Office, navegadores, jogos, Electron, Java…). Qualquer afirmação sobre eles é **regra geral**, e está marcada como tal.
- Captura de imagem, clipboard e `Bitmap` (descritos pela leitura do código).
- Comportamento com privilégios de administrador.
- Outras versões da biblioteca ou do Windows além de Windows 11 / Python 3.12.

### Uma nota sobre um erro que cometi

No início do estudo, um script de teste procurou "o Bloco de Notas" e **acabou lendo uma janela real que já estava aberta**, em vez de uma nova. Nada foi enviado ou alterado, e os registros foram apagados — mas foi o que motivou criar o laboratório isolado. A lição vale para você também: **teste sempre num ambiente de treino antes de apontar o robô para algo real.**

---

## 23. 🙏 Créditos e licença

- A biblioteca **uiautomation** é de **yinkaisheng** e distribuída sob a licença **Apache 2.0**:
  - Código: <https://github.com/yinkaisheng/Python-UIAutomation-for-Windows>
  - Pacote: <https://pypi.org/project/uiautomation/>
- Este guia é um **estudo independente e não oficial**. Não tem vínculo com o autor da biblioteca nem com a Microsoft.
- Todas as marcas citadas pertencem aos seus donos.
- A documentação da Microsoft sobre UI Automation (padrões e tipos de controle) é a referência oficial por trás de tudo isso: <https://learn.microsoft.com/windows/win32/winauto/entry-uiauto-win32>.

> Achou um erro, uma afirmação duvidosa ou quer sugerir uma receita? Abra uma *issue* ou envie um *pull request*. Este guia melhora com a sua revisão.

---

⭐ **Gostou?** Deixe uma estrela no repositório e compartilhe com quem ainda faz à mão o que o Python faz sozinho.
