# 06 — Funções de módulo (Win32): mouse, teclado, janelas, tela, processos, hotkeys

Todas usam `ctypes.windll` direto. Convenção: `waitTime` = espera **após** a ação (padrão `OPERATION_WAIT_TIME`=0.5 s). Coordenadas = pixels de tela (o processo é Per‑Monitor DPI aware desde o import).

## 6.1 Mouse
| Função | Descrição / detalhes |
|---|---|
| `GetCursorPos()` / `GetPhysicalCursorPos()` | `(x, y)` |
| `SetCursorPos(x, y)` | bool; aceita coordenadas negativas (monitor à esquerda/acima do primário) |
| `MoveTo(x, y, moveSpeed=1, waitTime)` | **animado**: duração `MAX_MOVE_SECOND/moveSpeed`, proporcional à distância, passos de ~20 px com `SetCursorPos`. `moveSpeed<=0` → duração 0. |
| `Click(x,y,waitTime)` / `RightClick` / `MiddleClick` | `SetCursorPos` + `mouse_event(Down|Absolute)`, dorme 0.05 s, `mouse_event(Up|Absolute)`. Não anima. |
| `PressMouse(x,y)` / `ReleaseMouse()` | idem botões esquerdo/direito (`RightPressMouse/RightReleaseMouse`) / meio (`MiddlePressMouse/MiddleReleaseMouse`) |
| `DragDrop(x1,y1,x2,y2,moveSpeed,waitTime)` / `RightDragDrop` / `MiddleDragDrop` | Press → MoveTo → Release |
| `WheelDown(wheelTimes=1, interval=0.05, waitTime)` / `WheelUp` | `mouse_event(Wheel, ±120)`; rola onde o cursor estiver |
| `mouse_event(flags,dx,dy,data,extra)` | wrapper cru |
| `MouseInput(dx,dy,mouseData,dwFlags,time_)` → `INPUT` + `SendInput(*inputs)` | via `SendInput` |
| `WindowFromPoint(x,y)` | HWND |

`Click` calcula `x*65535//screenWidth` com a **tela primária**; como não usa a flag `Move`, o clique acontece onde `SetCursorPos` deixou o cursor (por isso funciona com vários monitores).

## 6.2 Teclado
| Função | Descrição |
|---|---|
| `SendKey(key, waitTime)` | `keybd_event` down+up de **um** VK (`Keys.VK_*`) — sempre com `KeyboardEventFlag.ExtendedKey` |
| `PressKey(key)` / `ReleaseKey(key)` | segura / solta |
| `IsKeyPressed(key)` | `GetAsyncKeyState & 0x8000` |
| `SendKeys(text, interval=0.01, waitTime=0.5, charMode=True, debug=False)` | digitador completo (abaixo) |
| `SendUnicodeChar(char, charMode=True)` | uma letra Unicode via `SendInput`. `charMode=True` → `KEYEVENTF_UNICODE` (independe do teclado/IME). `False` → usa `VkKeyScanW` (depende do layout/IME) |
| `KeyboardInput(vk, scan, flags)`, `HardwareInput(msg, param)` | montam structs `INPUT` |
| `keybd_event(...)`, `PostMessage`, `SendMessage` | wrappers crus |

### Sintaxe do `SendKeys` (lida da implementação)
- Texto comum é digitado como caracteres Unicode (`'abc 123 çãõ'`, inclui espaço).
- `{Nome}` = tecla especial (sem diferenciar maiúscula): `{Enter}`, `{Ctrl}`, `{Shift}`, `{Alt}`, `{Win}`, `{Delete}`, `{PageDown}`, `{F5}`, etc. — os nomes estão em `SpecialKeyNames` (veja 02: LBUTTON…, ENTER, TAB, F1–F24, NUMPAD0–9, etc.).
- `{tecla N}` repete N vezes: `{a 3}` → `aaa`, `{Enter 2}`.
- Modificadores (`Win, LWin, RWin, Shift, LShift, RShift, Ctrl, Control, LCtrl, RCtrl, LControl, Alt, LAlt, RAlt`) **seguram** a(s) tecla(s) seguinte(s):
  - `{Ctrl}a` → Ctrl+A.
  - `{Ctrl}{Shift}s` → Ctrl+Shift+S.
  - `{Ctrl}(AB)` → Ctrl segurado enquanto A e B são pressionadas; o grupo `( ... )` mantém o modificador até o `)`.
  - `{Ctrl}({Shift}(123))` aninhamento.
  - `{Ctrl}{a 3}` → Ctrl+A pressionado "ao mesmo tempo" 3 vezes (a vez final solta).
- Escapes: `{{}` → `{`, `{}}` → `}`, `{(}` e `{)}` → parênteses literais; `(` e `)` soltos fora de grupo são digitados normalmente.
- `{}` ou `{` sem fechar → `ValueError`; `{x y}` com `y` não numérico ou mais de 2 palavras → `ValueError`.
- Letras maiúsculas são digitadas como caracteres (`SendUnicodeChar`), não como Shift+letra — por isso `SendKeys('A')` funciona em qualquer layout, mas **não aciona atalhos**: para atalhos use `{Ctrl}a` (minúscula).
- `interval` = pausa entre teclas; entre combos usa 0.01 s fixo (`hotkeyInterval`). `debug=True` imprime cada evento.
- Teclas VK usam `MapVirtualKeyA` para o scancode (tabela `_SCKeys` para numpad/modificadores).

Detalhes da implementação (analisador, ordem de eventos, pausas, lista de nomes válidos como `{Back}` — **não existe `{Backspace}`** — e `{Capital}` — **não existe `{CapsLock}`**) estão em `11-internos-algoritmos.md` §11.3. Em hold, `{Ctrl}A` (maiúsculo) é Ctrl+A **sem Shift**.

⚠ `SendKeys('')` (texto vazio) gera `IndexError` (o laço acessa `text[0]` antes de checar o tamanho). Os modificadores de mão direita `RCONTROL` não estão em `holdKeys` (há `LCONTROL` duplicado) — `{RControl}` não "segura".

## 6.3 Janelas (por HWND)
`GetForegroundWindow`, `SetForegroundWindow`, `BringWindowToTop`, `SwitchToThisWindow`, `GetAncestor(h, GAFlag.Parent|Root|RootOwner)`, `IsTopLevelWindow` (Win7+), `IsIconic`, `IsZoomed`, `IsWindowVisible`, `ShowWindow(h, SW.*)`, `MoveWindow(h,x,y,w,h,repaint)`, `SetWindowPos(h, insertAfter, x,y,w,h, flags)`, `SetWindowTopmost(h, bool)`, `GetWindowLong/SetWindowLong(h, GWL.*)`, `GetWindowText(h)` (**trunca em 260 chars**), `SetWindowText`, `GetEditText(h)` (usa `WM_GETTEXTLENGTH/WM_GETTEXT`, sem limite de 260 — bom para Edit Win32 longo), `GetWindowRect(h)` → `Rect`, `DwmGetWindowExtendFrameBounds(h)` (retângulo sem a borda invisível de 7–8 px do Win10/11), `DwmIsCompositionEnabled()`.

`SW`: Hide, ShowNormal, ShowMinimized, ShowMaximized, Maximize, ShowNoActivate, Show, Minimize, ShowMinNoActive, ShowNA, Restore, ShowDefault, ForceMinimize… (lista completa em 02). `SWP`: flags + `HWND_Topmost/NoTopmost/Top/Bottom`. `GWL`: ExStyle, Style, WndProc, HInstance, Id, UserData…

## 6.4 Tela e cor
| Função | Descrição |
|---|---|
| `GetScreenSize()` | monitor primário `(w, h)` (testado: 2560×1440) |
| `GetVirtualScreenSize()` | área virtual somada de todos (3640×1920 no ambiente de teste) |
| `GetMonitorsRect()` | lista de `Rect` — a ordem não é "primário primeiro" |
| `SetScreenSize(w,h)` | **altera a resolução do monitor** (`ChangeDisplaySettingsW(devMode, 0)`: mudança dinâmica, sem a flag de gravar no registro). Não chamei; use com muito cuidado. Se a resolução já for a pedida, só devolve True. |
| `GetPixelColor(x,y,handle=0)` | `GetPixel` GDI → **BGR** `0x00BBGGRR` (handle 0 = desktop). Não funciona em console. Em várias leituras use `Bitmap` |

## 6.5 Sistema, processos, som
| Função | Descrição |
|---|---|
| `IsUserAnAdmin()` | bool |
| `RunScriptAsAdmin(argv, workingDirectory=None, showFlag=SW.ShowNormal)` | `ShellExecuteW "runas"` (mostra UAC); True se `>32` |
| `IsDesktopLocked()` | True com Win+L, Ctrl+Alt+Del ou RDP desconectado |
| `IsProcess64Bit(pid)` | True/False/None (sem acesso) |
| `GetProcesses(detailedInfo=True)` | `ProcessInfo(pid, ppid, exeName, is64Bit, exePath, cmdLine)`. Lê a PEB do processo (`ReadProcessMemory`) p/ cmdLine; sem admin muitos campos ficam vazios (`ppid=-1`, `is64Bit=None`). |
| `EnumProcessByWMI()` | gerador; **requer `pip install wmi`** (importa `wmi` na hora — testado: `ModuleNotFoundError` sem ele) |
| `TerminateProcess(pid)` | `TerminateProcess` — mata sem aviso |
| `TerminateProcessByName(exeName, killAll=True)` | compara `exeName` **exato** (`'notepad.exe'`); retorna quantos matou |
| `PlayWaveFile(path, isAsync, isLoop)` | `PlaySoundW`; `path=''/None` para parar |
| `MessageBox(content, title, flags=MB.Ok)` | bloqueante; retorna `MB.IdOk` etc. |
| `SetConsoleColor/ResetConsoleColor`, `GetConsoleTitle/OriginalTitle/SetConsoleTitle` | cores/título do console |
| `ShowDesktop(waitTime)` | `SendKeys('{Win}d')` |
| `SetProcessDpiAwareness(v)`, `SetThreadDpiAwarenessContext(ctx)` | DPI (já definido no import) |
| `Input(prompt)`, `InputColorfully(prompt)` | `input()` com cor |

## 6.6 Hotkeys globais
`RunByHotKey({(ModifierKey.Control, Keys.VK_1): func}, stopHotKey=None, exitHotKey=(ModifierKey.Control, Keys.VK_D), waitHotKeyReleased=True)`
- Registra com `RegisterHotKey`; roda `func(stopEvent)` numa **thread** por hotkey. `func` deve checar `stopEvent.is_set()` para parar quando o `stopHotKey` for pressionado.
- Bloqueia no laço de mensagens (`GetMessageW`) e ao sair chama **`os._exit(0)`** (encerra o processo).
- No `finally` de cada thread solta todas as teclas VK que estiverem pressionadas.
- `WaitHotKeyReleased((mod, key))` espera as teclas do atalho soltarem (para não contaminar `SendKeys`).
- `ModifierKey`: Alt=1, Control=2, Shift=4, Win=8 (+ `NoRepeat`). Combine com `|`.
- Se um hotkey já estiver registrado por outro programa, imprime aviso e **não inicia**.

## 6.7 Constantes úteis para mouse/teclado
`MouseEventFlag` (Move, LeftDown/Up, RightDown/Up, MiddleDown/Up, Wheel, Absolute, XDown/XUp, HWheel, MoveNoCoalesce, VirtualDesk), `KeyboardEventFlag` (KeyDown=0, ExtendedKey=1, KeyUp=2, KeyUnicode=4, KeyScanCode=8), `InputType` (Mouse=0, Keyboard=1, Hardware=2), `MB`, `GAFlag`, `Keys` (176 VK_*), `ConsoleColor`.
