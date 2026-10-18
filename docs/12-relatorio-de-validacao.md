# 12 — Relatório de validação (a documentação foi testada de verdade)

Depois de escrever esta documentação **lendo o código-fonte**, cada afirmação relevante foi **executada** contra aplicativos reais e comparada com o que a biblioteca faz. Este arquivo resume o que foi confirmado, o que foi corrigido e o que ficou sem verificação.

## Ambiente do teste
- Windows 11, Python 3.12, `uiautomation` **2.0.29**, `comtypes` 1.4.17 (mais `numpy`, `Pillow` e `wmi` instalados só para testar as integrações opcionais).
- Teclado **pt-BR (ABNT2)**, 2 monitores (um em coordenadas negativas), escala de 125% no principal.
- Alvos de teste:
  - uma janela **WinForms** própria, com todos os controles clássicos, `TopMost`, e log de eventos de mouse e teclado;
  - uma janela **WPF** própria (RichTextBox, DataGrid, ListBox com 500 itens virtualizados, Calendar, Expander, Slider, TreeView, Menu…);
  - janelas descartáveis para testar fechar/esconder/elemento morto;
  - processos filhos com nome único para `GetProcesses`/`TerminateProcess*`;
  - Paint e Calculadora abertos só para procurar patterns raros, e leitura (sem alterar nada) de patterns em janelas já abertas.
- Mouse e teclado só agiram sobre as janelas de laboratório, com checagem de primeiro plano antes de cada envio.

## Números
**773 verificações** (já sem duplicatas): **562 confirmadas**, **182 informativas** (mediram um valor sem ter expectativa), **29 refutadas, com erro ou abortadas**.

Dessas 29, **16 foram erro ou instabilidade do próprio teste** (listadas no fim) e **13 são achados reais** que levaram a correções na documentação.

| Área | Confirmadas | Observação |
|---|---:|---|
| `Control`, busca, navegação | 41 | inclui `Depth`, `RegexName`, `foundIndex`, `WalkTree` |
| `Invoke` e modais | 7 | descoberta importante: é **síncrono** |
| Patterns WinForms | 35 | |
| Patterns WPF | 57 | Text, Grid, Table, virtualização, MultipleView… |
| Mouse | 38 | fórmula do `MoveTo` conferida em milissegundos |
| Teclado / `SendKeys` | 36 | ordem real dos eventos conferida tecla a tecla |
| Janelas, tela, cores | 54 | |
| `Bitmap` | 85 | pixels, arquivos, GIF/TIFF, numpy, PIL, oclusão |
| Clipboard | 22 + 9 | |
| Processos | 23 | |
| `Logger`, `Rect` | 29 | |
| `import`, threads, hotkeys | 33 | hotkeys testados com teclas reais num processo filho |
| Receitas do README (seções 4 e 10) | 22 | todas executadas; só a 10.7 precisou de ajuste (linha de cabeçalho vazia) |

## Achados reais (o que mudou na documentação)

### Bugs confirmados na biblioteca (2.0.29)
| # | Onde | O que acontece (reproduzido) |
|---|---|---|
| 1 | `Bitmap.Clone()` e `Bitmap.RotateWithSameSize()` | **Falham 100% das vezes** (5 de 5) com `OSError: access violation reading 0xFFFFFFFF…` em Python 64 bits. Só essas duas funções da DLL ficaram sem `restype` de 64 bits, então o ponteiro é truncado. Use `Copy()` no lugar de `Clone()`. |
| 2 | `SetClipboardText` com caractere fora do BMP (emoji) | O texto volta **truncado**: `'ok 😀 fim'` → `'ok 😀 fi'` (o tamanho é calculado em *code points*, não em unidades UTF‑16). |
| 3 | `SetClipboardHtml` / `GetClipboardHtml` | O bloco gravado **não termina em NUL** e a memória não é zerada. Com a memória "suja", **47 de 60** repetições deram `UnicodeDecodeError` ou lixo depois de `</html>`. Em condições calmas funciona. |
| 4 | `GetClipboardText`, `GetClipboardHtml`, `GetClipboardBitmap` | Se o formato pedido não existe, **o clipboard fica aberto**. Programas normais (que abrem com um *handle* de janela) ficam **bloqueados** até o Python terminar ou você chamar `CloseClipboard`. Chamadas normais não vazam. |
| 5 | `SendKeys` com caractere acima de U+FFFF | **Corrompe** o caractere (`😀` vira ``), porque o código de varredura é truncado para 16 bits. |
| 6 | `SendKeys('{Backspace}')`, `{Foo}`, `{CapsLock}` (qualquer nome inexistente com mais de 1 letra) | Levanta `TypeError: ord() expected a character…`. **Não** vira texto literal. (`{x}` de uma letra só funciona.) |
| 7 | `SendKeys('')` | Levanta `IndexError`. |
| 8 | `SendKeys('{RControl}a')` | `RControl` **não segura** a tecla (o Ctrl solta antes do `a`). `LControl` e `Ctrl` seguram. |
| 9 | `SendKeys('{Alt}…')` | Todas as teclas vão com a flag "estendida"; `VK_MENU` estendido é **Alt Gr**. Em layouts com Alt Gr (como pt-BR) o Windows acrescenta **Ctrl**: `{Alt}x` chega como **Ctrl+Alt+X**. Use `{LAlt}` para Alt puro. |
| 10 | `SendUnicodeChar`, `SendInput` | Devolvem **1** (só o retorno da última chamada), mesmo com 2 eventos. |
| 11 | `ItemContainerPattern.FindItemByProperty(None, …)` | `AttributeError: 'NoneType' object has no attribute 'Element'`. Precisa passar um `Control` (a API nativa aceita "começar do início", a lib não). |
| 12 | `SynchronizedInputPattern.StartListening()` | `TypeError: required argument 'inputType' missing` (o método da lib não recebe o argumento obrigatório). `Cancel()` funciona. |
| 13 | `TextPattern.RangeFromChild`, `TextRange.CompareEndpoints` | Falham (`ArgumentError`), como previsto na leitura do código. `CompareEndpoints` funciona se chamado direto em `r.textRange`. |
| 14 | `Control.GetPatternAs` | Devolve um `int`, não um ponteiro COM utilizável (o próprio código marca "todo"). |
| 15 | `ShowWindow` e quem usa (`Control.ShowWindow/Show/Hide`, `Maximize`, `Minimize`, `Restore`…) | O retorno **não é "sucesso"**: é "a janela **estava visível** antes". `ShowWindow(SW.Show)` depois de um `Hide` devolve `False` mesmo tendo funcionado. |
| 16 | `Exists()` / `Refind()` / propriedades com elemento morto | Levantam `COMError` (`0x80040201`, elemento não disponível) em vez de devolver `False`. |
| 17 | `WindowPattern.WaitForInputIdle` | `COMError 0x80004001` ("Não implementado") em janelas WinForms e WPF. |
| 18 | `WalkControl(c, includeTop=True, maxDepth=0)`, `TableControl.GetTableItemsValue(row=0/column=0)`, `DoubleClick` em controle de área zero, `GIF.ToGifFile` sem `delays`, `Rect == None`, `hash(Rect)` | Todos reproduzidos como descritos em `08-bugs-e-pegadinhas.md`. |

### Comportamentos descobertos (não são bugs, mas mudam como usar)
- **`Invoke` é síncrono.** Só volta quando o *handler* do botão termina. Se o clique abre um diálogo modal, o `Invoke` **fica preso até o diálogo fechar**; se ninguém fechar, estoura com `COMError 0x80131505` (timeout) após **~66 segundos**. Nesse período qualquer outra chamada UIA ao mesmo programa também espera, e uma busca a partir do Desktop (que passa por essa janela) trava até o timeout. `LegacyIAccessiblePattern.DoDefaultAction()` se comporta igual. `Click()` (mouse) volta na hora.
- **`SelectionPattern.GetSelection()`** de um ListBox Win32 multisseleção pode devolver um item **antigo** quando sobra só um selecionado. Confie em `SelectionItemPattern.IsSelected` item a item.
- **`FrameworkId`** de um app WinForms é `'WinForm'` (não `'Win32'`).
- **`GetClickablePoint()` de uma janela** pode devolver um ponto válido `(x, y, True)`; não é sempre `(0,0,False)`.
- **`Name` + `SubName` juntos** não dão erro (valem os dois).
- **`ControlType`**: são **41** tipos (eu tinha escrito 40).
- **`{Ctrl}(ab)`** aperta A e B **juntas** (A↓ B↓ B↑ A↑), não em sequência.
- **Uma thread sem `UIAutomationInitializerInThread`** funcionou nos testes, e até um `Control` criado na thread principal funcionou em outra. A biblioteca diz que não é suportado; trate como não garantido.
- Células de `DataGrid` do WPF vêm como `CustomControl` (sem atalhos `GetValuePattern`); `DatePicker` vem como `Control` genérico.
- `LogControl` custa ~95 ms por controle (34 consultas de pattern); `WalkControl` custa ~3 ms por controle.
- `cmdLine` de `GetProcesses` **funciona** (0 de 140 vazias): a suspeita levantada na leitura do código (buffer lido com o dobro do tamanho) **não se confirmou**.

### Confirmado como a documentação dizia (principais)
Fórmula do `MoveTo` (medido 0,041 s/0,160 s/0,347 s/0,596 s contra 0,039/0,152/0,339/0,579 s previstos); cliques com coordenadas negativas e `ratio`; `Wheel*` restaurando o cursor; `DoubleClick` com 2 `MouseDown`; ordem exata de eventos do `SendKeys` (`{Ctrl}a`, `{Ctrl}{Shift}s`, `{Ctrl}!`, `{Ctrl}{a 3}`); `{Ctrl}A` sem Shift; `GetWindowText` truncando em 259; `GetEditText` sem limite; GIF/TIFF multi-frame; captura de tela mostra a janela por cima e janela minimizada sai preta; hotkeys (registrar, disparar, "already running", parar, reiniciar, sair, hotkey duplicado); `import` sem criar COM, DPI por monitor, `restype` global, defaults de `waitTime` congelados; `TerminateProcessByName` com comparação exata e `killAll`; formatos GIF/PNG/JPEG/BMP/TIFF; `ToFile` com extensão desconhecida gravando PNG; BGRA/ARGB; numpy e PIL.

## O que NÃO foi verificado (continua como "lido no código")
- **Patterns que só existem em Office e similares**: `AnnotationPattern`, `CustomNavigationPattern`, `DockPattern`, `ObjectModelPattern`, `SpreadsheetPattern`, `SpreadsheetItemPattern`, `StylesPattern`, `TextChildPattern`, `TransformPattern2`. Nenhum dos programas disponíveis os expôs.
- `ShowDesktop()` (envia Win+D e minimizaria as janelas em uso), `RunScriptAsAdmin` (abre o UAC), `SetScreenSize` com resolução diferente (mudaria o monitor), reprodução real de som em `PlayWaveFile`.
- `SendKeys` com `{Win}` (abriria o menu Iniciar ou dispararia atalhos do Windows).
- Programas elevados (administrador), Electron/Chromium, Java, Qt, jogos, sessão remota e outras versões do Windows ou da biblioteca.
- `MetroClose` (só Windows 8).

## Erros do próprio teste (não são achados da biblioteca)
Para ser transparente, estes resultados apareceram como "refutado/erro" e **foram falhas minhas**:
1. `RemoveFromSelection` e `Legacy.Select` pareciam falhar porque o teste lia `GetSelection()` do contêiner (que devolve item antigo); lendo `IsSelected` por item, **ambos funcionam**.
2. `ScrollIntoView` num item de ListBox WinForms: esse item não tem o pattern (o teste assumiu que tinha).
3. `Grid.GetItem` / `DatePicker`: usei atalhos `GetValuePattern` em controles que não os têm (`CustomControl`/`Control`).
4. `Control()` sem critérios: o teste esperava outra coisa; o `LookupError` é o comportamento documentado.
5. `GetPatternIdInterface(1)`: o `KeyError` ocorreu (era o esperado); só o formato do meu teste estava errado.
6. `DeleteLog`: um `x` impresso quebrou minha comparação; o arquivo foi apagado.
7. Três testes de vazamento e dois de "clipboard preso" usaram `OpenClipboard(NULL)` como observador. Descobri que **dois processos com NULL abrem juntos**; refeitos com um observador que usa *handle* de janela (como um app real), **o vazamento e o limite de 0,2 s se confirmaram**.
8. O laboratório inicial usava `ShowDialog`; esconder o formulário encerrava o diálogo e os testes seguintes falhavam em cascata. Troquei por `Application.Run`.
9. "O `Invoke` não mexe no mouse" apareceu como refutado numa rodada porque **o usuário mexeu o mouse** durante a medição (o cursor andou 2 a 8 pixels); nas outras rodadas o cursor ficou idêntico antes e depois.
10. "Botão coberto: o `Click` não chega ao botão" falhou numa rodada porque o laboratório era "sempre no topo" e a ordem entre duas janelas "sempre no topo" variou. Refeito com o laboratório fora do topo, de forma determinística: **`Invoke` funciona e o `Click` cai na janela de cima**.

## Adendo: validação do guia prático (`13-guia-pratico.md`)
Os exemplos do capítulo 13 foram executados em 56 verificações: navegação pai/filho/irmão/ancestral, índices, `GetChildren` (uma lista de 60 itens devolve **61 filhos**, por causa da barra de rolagem), `WalkControl` e filtros, percorrer uma `TreeView` inteira, tabelas (ListView e DataGrid), menus por `Invoke`, `esperar_ate`, `inspecionar_cursor`, e as medições de **Invoke × Click** (`4 ms` / `58 ms` / `129 ms`; `Invoke` funciona com a janela minimizada e com o botão coberto).
