# 01 — Arquitetura da lib

## Estrutura de arquivos instalados
```
uiautomation/
  __init__.py      -> "from .version import VERSION; from .uiautomation import *"
  version.py       -> VERSION = "2.0.29"
  uiautomation.py  -> TODO o código (≈10.850 linhas)
  py.typed         -> marca que há type hints
  bin/UIAutomationClient_VC140_X64.dll   (132 KB)  <- captura de imagem (GDI+)
  bin/UIAutomationClient_VC140_X86.dll   (108 KB)
```
Metadados: `Requires-Dist: comtypes>=1.2.1`, licença Apache 2.0, autor yinkaisheng.

## Camadas
1. **UIAutomationCore (COM)** — `comtypes.client.GetModule("UIAutomationCore.dll")` + `CreateObject("{ff48dba4-60ef-4201-aa87-54103eef594e}")` (CUIAutomation). Feito por `_AutomationClient` (L50), **singleton preguiçoso**: só cria o COM no primeiro uso (`_AutomationClient.instance()`), não no `import`. Tenta 3 vezes.
   - Guarda `UIAutomationCore`, `IUIAutomation` e `ViewWalker = IUIAutomation.RawViewWalker`.
   - **Importante:** o walker é o **RawViewWalker** (a linha do `ControlViewWalker` está comentada). Ou seja, a árvore percorrida é a *raw view*: inclui elementos que o Inspect "Control View" esconde (por isso aparecem `TitleBar`, `Thumb`, painéis internos etc.).
2. **`_DllClient`** (L79) — carrega a DLL nativa em `bin/` para `Bitmap` (GDI+). Se falhar, imprime aviso e **só as funções de Bitmap ficam indisponíveis**. Adiciona `bin` ao `PATH` e usa `os.add_dll_directory`.
3. **Wrappers ctypes de Win32** — user32/kernel32/gdi32/dwmapi/winmm/shell32 (mouse, teclado, janelas, processos, clipboard).
4. **Classes de Pattern** (L4484–6360) — cada uma embrulha uma interface `IUIAutomationXxxPattern`; guardam o ponteiro em `.pattern`.
5. **`Control` e subclasses** (L6369–10222) — embrulham `IUIAutomationElement` (em `._element`).

## Efeitos colaterais ao importar (IMPORTANTE)
| Efeito | Onde | Consequência |
|---|---|---|
| `SetProcessDpiAwareness(PerMonitorDpiAware)` | L2958 | O processo vira DPI-aware: coordenadas em pixels reais. Chamar de novo depois falha ("só uma vez por processo"). |
| restype de várias APIs Windows | L129–146 | Altera `ctypes.windll.user32.*` **globalmente** no processo (ex.: `GetForegroundWindow.restype=c_void_p`). |
| `atexit.register(_ExitHandler)` | L3346 | Fecha o arquivo de log ao sair. |
| Arquivo `@AutomationLog.txt` | `Logger.FilePath` | **Qualquer log da lib (inclusive `LogControl`/`EnumAndLogControl`, timeouts) é gravado em arquivo no diretório atual** (modo append, UTF‑8). Para desligar: `auto.Logger.SetLogFile('')`. Cuidado: pode vazar conteúdo de telas para disco. |

## Variáveis globais de configuração (módulo `uiautomation.uiautomation`)
| Nome | Padrão | Função |
|---|---|---|
| `SEARCH_INTERVAL` | 0.5 | Pausa entre tentativas de busca (valor *padrão capturado na definição* dos métodos — ver abaixo) |
| `MAX_MOVE_SECOND` | 1 | Duração máxima da animação do mouse (`MoveTo`). `0` desliga a animação (`SetCursorPos` direto) |
| `TIME_OUT_SECOND` | 10 | Timeout global de busca (usado por `Element`/`Refind`) |
| `OPERATION_WAIT_TIME` | 0.5 | `waitTime` padrão de quase todas as ações (clique, SendKeys, Invoke…) |
| `MAX_PATH` | 260 | Tamanho de buffers (`GetWindowText` trunca em 260!) |
| `DEBUG_SEARCH_TIME` | False | Loga tempo e nº de controles percorridos em cada busca |
| `DEBUG_EXIST_DISAPPEAR` | False | Loga quando controle não existe / não some |
| `METRO_WINDOW_CLASS_NAME` | `Windows.UI.Core.CoreWindow` | Janelas Metro do Win8 |
| `S_OK` | 0 | Comparado com o retorno dos métodos COM |

**Pegadinha dos defaults:** `waitTime: float = OPERATION_WAIT_TIME` é avaliado **na definição**. Alterar `auto.uiautomation.OPERATION_WAIT_TIME = 0.1` *depois do import* **não muda** os defaults já gravados nas assinaturas; passe `waitTime=` explicitamente. O mesmo vale para `SEARCH_INTERVAL`. Já `TIME_OUT_SECOND` é lido em tempo de execução (por `Element`), então `SetGlobalSearchTimeout()` funciona de verdade (testado: o timeout de acesso a controle inexistente passou a 3 s). `MAX_MOVE_SECOND` também é lido em runtime.

## Threads e COM
- UIAutomation usa COM; cada thread precisa inicializá-lo: `with auto.UIAutomationInitializerInThread(): ...` ou `InitializeUIAutomationInCurrentThread()` / `UninitializeUIAutomationInCurrentThread()` (`CoInitializeEx`/`CoUninitialize`).
- **Não passe `Control`/`Pattern` entre threads**; crie-os dentro da thread que os usa.
- `RunByHotKey` roda cada função de hotkey numa thread própria e termina o processo com `os._exit(0)`.

## Modelo de "Control preguiçoso" (lazy)
`auto.ButtonControl(Name="OK")` **não procura nada ao ser criado**. Guarda os critérios (`searchProperties`) e só busca quando você:
- acessa `.Element` ou qualquer propriedade (`.Name`, `.BoundingRectangle`…) → faz `Refind(TIME_OUT_SECOND)`; se não achar, **levanta `LookupError`**;
- chama `Exists()` / `Refind()` / `Disappears()` explicitamente.

Depois de encontrado o elemento fica em cache em `_element`. Se a UI mudar e o elemento ficar inválido, as propriedades darão erro COM; chame `Refind()` (ou `Exists()`, que procura de novo e substitui o cache).
Controles criados de um `element` direto (ex.: via `GetChildren()`, `ControlFromPoint`) têm `_elementDirectAssign=True` e **nunca são re-procurados**.

## Hierarquia de classes
```
Control
 ├─ 40 tipos (ButtonControl, EditControl, ...)
 ├─ PaneControl(Control, TopLevel)
 └─ WindowControl(Control, TopLevel)
TopLevel (mixin: Maximize, Minimize, Restore, SetTopmost, SetActive, MoveToCenter...)
```
Mapas internos: `ControlConstructors[ControlType]->classe`, `PatternConstructors[PatternId]->classe`, `ControlTypeNames`, `PatternIdNames`, `PropertyIdNames`.

`Control.CreateControlFromElement(element)` converte um `IUIAutomationElement` cru na classe certa; se `CurrentControlType` for desconhecido, loga em vermelho e devolve `None`.
