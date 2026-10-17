# Referência completa da API (gerada do código-fonte)

> Gerada automaticamente a partir da AST de `uiautomation/uiautomation.py` (v2.0.29). Cobre **todas** as funções, classes, métodos e propriedades. O número é a linha no arquivo.

Totais: **140 classes**, **549 métodos/propriedades**, **117 funções de módulo**.


## Funções de módulo

| Linha | Função | Descrição (docstring) |
|---|---|---|
| 1773 | `_GetDictKeyName(theDict: Dict[str, Any], theValue: Any, keyCondition: Optional[Callable[[str], bool]]=None)` |  |
| 1789 | `SetConsoleColor(color: int)` | Change the text color on console window. color: int, a value in class `ConsoleColor`. Return bool, True if succeed otherwise False. |
| 1808 | `ResetConsoleColor()` | Reset to the default text color on console window. Return bool, True if succeed otherwise False. |
| 1819 | `WindowFromPoint(x: int, y: int)` | WindowFromPoint from Win32. Return int, a native window handle. |
| 1827 | `GetCursorPos()` | GetCursorPos from Win32. Get current mouse cursor positon. Return Tuple[int, int], two ints tuple (x, y). |
| 1838 | `GetPhysicalCursorPos()` | GetPhysicalCursorPos from Win32. Get current mouse cursor positon. Return Tuple[int, int], two ints tuple (x, y). |
| 1849 | `SetCursorPos(x: int, y: int)` | SetCursorPos from Win32. Set mouse cursor to point x, y. x: int. |
| 1860 | `GetDoubleClickTime()` | GetDoubleClickTime from Win32. Return int, in milliseconds. |
| 1868 | `mouse_event(dwFlags: int, dx: int, dy: int, dwData: int, dwExtraInfo: int)` | mouse_event from Win32. |
| 1873 | `keybd_event(bVk: int, bScan: int, dwFlags: int, dwExtraInfo: int)` | keybd_event from Win32. |
| 1878 | `PostMessage(handle: int, msg: int, wParam: int, lParam: int)` | PostMessage from Win32. Return bool, True if succeed otherwise False. |
| 1886 | `SendMessage(handle: int, msg: int, wParam: int, lParam: int)` | SendMessage from Win32. Return int, the return value specifies the result of the message processing; it depends on the message sent. |
| 1895 | `Click(x: int, y: int, waitTime: float=OPERATION_WAIT_TIME)` | Simulate mouse click at point x, y. x: int. y: int. |
| 1910 | `MiddleClick(x: int, y: int, waitTime: float=OPERATION_WAIT_TIME)` | Simulate mouse middle click at point x, y. x: int. y: int. |
| 1925 | `RightClick(x: int, y: int, waitTime: float=OPERATION_WAIT_TIME)` | Simulate mouse right click at point x, y. x: int. y: int. |
| 1940 | `PressMouse(x: int, y: int, waitTime: float=OPERATION_WAIT_TIME)` | Press left mouse. x: int. y: int. |
| 1953 | `ReleaseMouse(waitTime: float=OPERATION_WAIT_TIME)` | Release left mouse. waitTime: float. |
| 1964 | `RightPressMouse(x: int, y: int, waitTime: float=OPERATION_WAIT_TIME)` | Press right mouse. x: int. y: int. |
| 1977 | `RightReleaseMouse(waitTime: float=OPERATION_WAIT_TIME)` | Release right mouse. waitTime: float. |
| 1988 | `MiddlePressMouse(x: int, y: int, waitTime: float=OPERATION_WAIT_TIME)` | Press middle mouse. x: int. y: int. |
| 2001 | `MiddleReleaseMouse(waitTime: float=OPERATION_WAIT_TIME)` | Release middle mouse. waitTime: float. |
| 2012 | `MoveTo(x: int, y: int, moveSpeed: float=1, waitTime: float=OPERATION_WAIT_TIME)` | Simulate mouse move to point x, y from current cursor. x: int. y: int. |
| 2052 | `DragDrop(x1: int, y1: int, x2: int, y2: int, moveSpeed: float=1, waitTime: float=OPERATION_WAIT_TIME)` | Simulate mouse left button drag from point x1, y1 drop to point x2, y2. x1: int. y1: int. |
| 2067 | `RightDragDrop(x1: int, y1: int, x2: int, y2: int, moveSpeed: float=1, waitTime: float=OPERATION_WAIT_TIME)` | Simulate mouse right button drag from point x1, y1 drop to point x2, y2. x1: int. y1: int. |
| 2082 | `MiddleDragDrop(x1: int, y1: int, x2: int, y2: int, moveSpeed: float=1, waitTime: float=OPERATION_WAIT_TIME)` | Simulate mouse middle button drag from point x1, y1 drop to point x2, y2. x1: int. y1: int. |
| 2097 | `WheelDown(wheelTimes: int=1, interval: float=0.05, waitTime: float=OPERATION_WAIT_TIME)` | Simulate mouse wheel down. wheelTimes: int. interval: float. |
| 2110 | `WheelUp(wheelTimes: int=1, interval: float=0.05, waitTime: float=OPERATION_WAIT_TIME)` | Simulate mouse wheel up. wheelTimes: int. interval: float. |
| 2123 | `GetScreenSize()` | Return Tuple[int, int], two ints tuple (width, height). |
| 2134 | `SetScreenSize(width: int, height: int)` | Return bool. |
| 2161 | `GetVirtualScreenSize()` | Return Tuple[int, int], two ints tuple (width, height). |
| 2172 | `GetMonitorsRect()` | Get monitors' rect. Return List[Rect]. |
| 2188 | `GetPixelColor(x: int, y: int, handle: int=0)` | Get pixel color of a native window. x: int. y: int. |
| 2210 | `MessageBox(content: str, title: str, flags: int=MB.Ok)` | MessageBox from Win32. content: str. title: str. |
| 2221 | `SetForegroundWindow(handle: int)` | SetForegroundWindow from Win32. handle: int, the handle of a native window. Return bool, True if succeed otherwise False. |
| 2230 | `BringWindowToTop(handle: int)` | BringWindowToTop from Win32. handle: int, the handle of a native window. Return bool, True if succeed otherwise False. |
| 2239 | `SwitchToThisWindow(handle: int)` | SwitchToThisWindow from Win32. handle: int, the handle of a native window. |
| 2247 | `GetAncestor(handle: int, flag: int)` | GetAncestor from Win32. handle: int, the handle of a native window. index: int, a value in class `GAFlag`. |
| 2257 | `IsTopLevelWindow(handle: int)` | IsTopLevelWindow from Win32. handle: int, the handle of a native window. Return bool. |
| 2267 | `GetWindowLong(handle: int, index: int)` | GetWindowLong from Win32. handle: int, the handle of a native window. index: int. |
| 2276 | `SetWindowLong(handle: int, index: int, value: int)` | SetWindowLong from Win32. handle: int, the handle of a native window. index: int. |
| 2287 | `IsIconic(handle: int)` | IsIconic from Win32. Determine whether a native window is minimized. handle: int, the handle of a native window. |
| 2297 | `IsZoomed(handle: int)` | IsZoomed from Win32. Determine whether a native window is maximized. handle: int, the handle of a native window. |
| 2307 | `IsWindowVisible(handle: int)` | IsWindowVisible from Win32. handle: int, the handle of a native window. Return bool. |
| 2316 | `ShowWindow(handle: int, cmdShow: int)` | ShowWindow from Win32. handle: int, the handle of a native window. cmdShow: int, a value in clas `SW`. |
| 2326 | `MoveWindow(handle: int, x: int, y: int, width: int, height: int, repaint: int=1)` | MoveWindow from Win32. handle: int, the handle of a native window. x: int. |
| 2340 | `SetWindowPos(handle: int, hWndInsertAfter: int, x: int, y: int, width: int, height: int, flags: int)` | SetWindowPos from Win32. handle: int, the handle of a native window. hWndInsertAfter: int, a value whose name starts with 'HWND' in class SWP. |
| 2355 | `SetWindowTopmost(handle: int, isTopmost: bool)` | handle: int, the handle of a native window. isTopmost: bool Return bool, True if succeed otherwise False. |
| 2365 | `GetWindowText(handle: int)` | GetWindowText from Win32. handle: int, the handle of a native window. Return str. |
| 2377 | `SetWindowText(handle: int, text: str)` | SetWindowText from Win32. handle: int, the handle of a native window. text: str. |
| 2387 | `GetEditText(handle: int)` | Get text of a native Win32 Edit. handle: int, the handle of a native window. Return str. |
| 2400 | `GetConsoleOriginalTitle()` | GetConsoleOriginalTitle from Win32. Return str. Only available on Windows Vista or higher. |
| 2415 | `GetConsoleTitle()` | GetConsoleTitle from Win32. Return str. |
| 2426 | `SetConsoleTitle(text: str)` | SetConsoleTitle from Win32. text: str. Return bool, True if succeed otherwise False. |
| 2435 | `GetForegroundWindow()` | GetForegroundWindow from Win32. Return int, the native handle of the foreground window. |
| 2443 | `DwmIsCompositionEnabled()` | DwmIsCompositionEnabled from dwmapi. Return bool. |
| 2461 | `DwmGetWindowExtendFrameBounds(handle: int)` | Get Native Window Rect without invisible resize borders. Return Rect or None. If handle is not top level, return None. |
| 2484 | `GetWindowRect(handle: int)` | GetWindowRect from user32. Return RECT. |
| 2497 | `IsDesktopLocked()` | Check if desktop is locked. Return bool. Desktop is locked if press Win+L, Ctrl+Alt+Del or in remote desktop mode. |
| 2511 | `PlayWaveFile(filePath: str='C:\\Windows\\Media\\notify.wav', isAsync: bool=False, isLoop: bool=False)` | Call PlaySound from Win32. filePath: str, if emtpy, stop playing the current sound. isAsync: bool, if True, the sound is played asynchronously and returns immediately. |
| 2535 | `IsProcess64Bit(processId: int)` | Return True if process is 64 bit. Return False if process is 32 bit. Return None if unknown, maybe caused by having no access right to the process. |
| 2557 | `IsUserAnAdmin()` | IsUserAnAdmin from Win32. Return bool. Minimum supported OS: Windows XP, Windows Server 2003 |
| 2566 | `RunScriptAsAdmin(argv: List[str], workingDirectory: str=None, showFlag: int=SW.ShowNormal)` | Run a python script as administrator. System will show a popup dialog askes you whether to elevate as administrator if UAC is enabled. argv: List[str], a str list like sys.argv, argv[0] is the script file, argv[1:] are other arguments. |
| 2579 | `SendKey(key: int, waitTime: float=OPERATION_WAIT_TIME)` | Simulate typing a key. key: int, a value in class `Keys`. |
| 2589 | `PressKey(key: int, waitTime: float=OPERATION_WAIT_TIME)` | Simulate a key down for key. key: int, a value in class `Keys`. waitTime: float. |
| 2599 | `ReleaseKey(key: int, waitTime: float=OPERATION_WAIT_TIME)` | Simulate a key up for key. key: int, a value in class `Keys`. waitTime: float. |
| 2609 | `IsKeyPressed(key: int)` | key: int, a value in class `Keys`. Return bool. |
| 2618 | `_CreateInput(structure)` | Create Win32 struct `INPUT` for `SendInput`. Return `INPUT`. |
| 2632 | `MouseInput(dx: int, dy: int, mouseData: int=0, dwFlags: int=MouseEventFlag.LeftDown, time_: int=0)` | Create Win32 struct `MOUSEINPUT` for `SendInput`. Return `INPUT`. |
| 2640 | `KeyboardInput(wVk: int, wScan: int, dwFlags: int=KeyboardEventFlag.KeyDown, time_: int=0)` | Create Win32 struct `KEYBDINPUT` for `SendInput`. |
| 2645 | `HardwareInput(uMsg: int, param: int=0)` | Create Win32 struct `HARDWAREINPUT` for `SendInput`. |
| 2650 | `SendInput(*inputs)` | SendInput from Win32. input: `INPUT`. Return int, the number of events that it successfully inserted into the keyboard or mouse input stream. |
| 2669 | `SendUnicodeChar(char: str, charMode: bool=True)` | Type a single unicode char. char: str, len(char) must equal to 1. charMode: bool, if False, the char typied is depend on the input method if a input method is on. |
| 2723 | `_VKtoSC(key: int)` | This function is only for internal use in SendKeys. key: int, a value in class `Keys`. Return int. |
| 2740 | `SendKeys(text: str, interval: float=0.01, waitTime: float=OPERATION_WAIT_TIME, charMode: bool=True, debug: bool=False)` | Simulate typing keys on keyboard. text: str, keys to type. interval: float, seconds between keys. |
| 2929 | `SetThreadDpiAwarenessContext(dpiAwarenessContext: int)` | SetThreadDpiAwarenessContext from Win32. dpiAwarenessContext: int, a value in class `DpiAwarenessContext` |
| 2944 | `SetProcessDpiAwareness(dpiAwareness: int)` | ProcessDpiAwareness from Win32. dpiAwareness: int, a value in class `ProcessDpiAwareness` |
| 2994 | `GetProcesses(detailedInfo: bool=True)` | Enum process by Win32 API. detailedInfo: bool, only get pid and exeName if False. You should run python as administrator to call this function. |
| 3085 | `EnumProcessByWMI()` | Maybe slower, but can get system processes' info |
| 3095 | `TerminateProcess(pid: int)` |  |
| 3105 | `TerminateProcessByName(exeName: str, killAll: bool=True)` | exeName: str, such as notepad.exe return int, process count that was terminated |
| 3341 | `_ExitHandler()` |  |
| 4184 | `_OpenClipboard(value)` |  |
| 4193 | `GetClipboardFormats()` | Get clipboard formats that system clipboard has currently. Return Dict[int, str]. The key is a int value in class `ClipboardFormat` or othes values that apps registered by ctypes.windll.user32.RegisterClipboardFormatW |
| 4218 | `GetClipboardText()` |  |
| 4233 | `SetClipboardText(text: str)` | Return bool, True if succeed otherwise False. |
| 4256 | `GetClipboardHtml()` | Return str. Note: the positions(StartHTML, EndHTML ...) are valid for utf-8 encoding html text, when the utf-8 encoding html text is decoded to Python unicode str, |
| 4277 | `SetClipboardHtml(htmlText: str)` | htmlText: str, such as '<h1>Title</h1><h3>Hello</h3><p>hello world</p>' Return bool, True if succeed otherwise False. Refer: https://docs.microsoft.com/en-us/troubleshoot/cpp/add-html-code-clipboard |
| 4312 | `GetClipboardBitmap()` |  |
| 4324 | `SetClipboardBitmap(bitmap: Bitmap)` | Return bool, True if succeed otherwise False. |
| 4356 | `Input(prompt: str, consoleColor: int=ConsoleColor.Default)` |  |
| 4361 | `InputColorfully(prompt: str, consoleColor: int=ConsoleColor.Default)` |  |
| 4369 | `GetPatternIdInterface(patternId: int)` | Get pattern COM interface by pattern id. patternId: int, a value in class `PatternId`. Return comtypes._cominterface_meta. |
| 6362 | `CreatePattern(patternId: int, pattern: ctypes.POINTER(comtypes.IUnknown))` | Create a concreate pattern by pattern id and pattern(POINTER(IUnknown)). |
| 10252 | `InitializeUIAutomationInCurrentThread()` | Initialize UIAutomation in a new thread. If you want to use functionalities related to Controls and Patterns in a new thread. You must call this function first in the new thread. |
| 10263 | `UninitializeUIAutomationInCurrentThread()` | Uninitialize UIAutomation in a new thread after calling InitializeUIAutomationInCurrentThread. You must call this function when the new thread exits if you have called InitializeUIAutomationInCurrentThread in the same thread. |
| 10271 | `SetGlobalSearchTimeout(seconds: float)` | seconds: float. To make this available, you need explicitly import uiautomation: from uiautomation import uiautomation as auto |
| 10282 | `WaitForExist(control: Control, timeout: float)` | Check if control exists in timeout seconds. control: `Control` or its subclass. timeout: float. |
| 10292 | `WaitForDisappear(control: Control, timeout: float)` | Check if control disappears in timeout seconds. control: `Control` or its subclass. timeout: float. |
| 10302 | `WalkTree(top, getChildren: Optional[Callable[[TreeNode], List[TreeNode]]]=None, getFirstChild: Optional[Callable[[TreeNode], TreeNode]]=None, getNextSibling: Optional[Callable[[TreeNode], TreeNode]]=None, yieldCondition: Optional[Callable[[TreeNode, int], bool]]=None, includeTop: bool=False, maxDepth: int=4294967295)` | Walk a tree not using recursive algorithm. top: a tree node. getChildren: Callable[[TreeNode], List[TreeNode]], function(treeNode: TreeNode) -> List[TreeNode]. |
| 10374 | `GetRootControl()` | Get root control, the Desktop window. Return `PaneControl`. |
| 10388 | `GetFocusedControl()` | Return `Control` subclass. |
| 10393 | `GetForegroundControl()` | Return `Control` subclass. |
| 10410 | `GetConsoleWindow()` | Return `WindowControl` or None, a console window that runs python. |
| 10419 | `ControlFromPoint(x: int, y: int)` | Call IUIAutomation ElementFromPoint x,y. May return None if mouse is over cmd's title bar icon. Return `Control` subclass or None. |
| 10428 | `ControlFromPoint2(x: int, y: int)` | Get a native handle from point x,y and call IUIAutomation.ElementFromHandle. Return `Control` subclass. |
| 10436 | `ControlFromCursor()` | Call ControlFromPoint with current cursor point. Return `Control` subclass. |
| 10445 | `ControlFromCursor2()` | Call ControlFromPoint2 with current cursor point. Return `Control` subclass. |
| 10454 | `ControlFromHandle(handle: int)` | Call IUIAutomation.ElementFromHandle with a native handle. handle: int, a native window handle. Return `Control` subclass or None. |
| 10465 | `ControlsAreSame(control1: Control, control2: Control)` | control1: `Control` or its subclass. control2: `Control` or its subclass. Return bool, True if control1 and control2 represent the same control otherwise False. |
| 10474 | `WalkControl(control: Control, includeTop: bool=False, maxDepth: int=4294967295)` | control: `Control` or its subclass. includeTop: bool, if True, yield (control, 0) first. maxDepth: int, enum depth. |
| 10504 | `LogControl(control: Control, depth: int=0, showAllName: bool=True, showPid: bool=False)` | Print and log control's properties. control: `Control` or its subclass. depth: int, current depth. |
| 10575 | `EnumAndLogControl(control: Control, maxDepth: int=4294967295, showAllName: bool=True, showPid: bool=False, startDepth: int=0)` | Print and log control and its descendants' propertyies. control: `Control` or its subclass. maxDepth: int, enum depth. |
| 10587 | `EnumAndLogControlAncestors(control: Control, showAllName: bool=True, showPid: bool=False)` | Print and log control and its ancestors' propertyies. control: `Control` or its subclass. showAllName: bool, if False, print the first 30 characters of control.Name. |
| 10602 | `FindControl(control: Optional[Control], compare: Callable[[Control, int], bool], maxDepth: int=4294967295, findFromSelf: bool=False, foundIndex: int=1)` | control: `Control` or its subclass. compare: Callable[[Control, int], bool], function(control: Control, depth: int) -> bool. maxDepth: int, enum depth. |
| 10625 | `ShowDesktop(waitTime: float=1)` | Show Desktop by pressing win + d |
| 10638 | `WaitHotKeyReleased(hotkey: Tuple[int, int])` | hotkey: Tuple[int, int], two ints tuple (modifierKey, key) |
| 10657 | `RunByHotKey(keyFunctions: Dict[Tuple[int, int], Callable], stopHotKey: Optional[Tuple[int, int]]=None, exitHotKey: Tuple[int, int]=(ModifierKey.Control, Keys.VK_D), waitHotKeyReleased: bool=True)` | Bind functions with hotkeys, the function will be run or stopped in another thread when the hotkey is pressed. keyFunctions: Dict[Tuple[int, int], Callable], such as {(uiautomation.ModifierKey.Control, uiautomation.Keys.VK_1) : function} stopHotKey: hotkey tup |

## Classes


### `_AutomationClient`  <sub>linha 50</sub>

Atributos: `_instance`

| Linha | Membro | Docstring |
|---|---|---|
| 54 | `instance(cls)` | Singleton instance (this prevents com creation on import). |

### `_DllClient`  <sub>linha 79</sub>

Atributos: `_instance`

| Linha | Membro | Docstring |
|---|---|---|
| 83 | `instance(cls)` | Singleton instance (this prevents com creation on import). |
| 123 | `__del__(self)` |  |

### `ControlType`  <sub>linha 149</sub>

ControlType from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/winauto/uiauto-controltype-ids

Atributos de classe: 41 (veja `02-constantes-e-enums.md`)


### `PatternId`  <sub>linha 242</sub>

PatternId from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/winauto/uiauto-controlpattern-ids

Atributos de classe: 34 (veja `02-constantes-e-enums.md`)


### `PropertyId`  <sub>linha 321</sub>

PropertyId from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/winauto/uiauto-automation-element-propids Refer https://docs.microsoft.com/en-us/windows/win32/winauto/uiauto-control-pattern-propids

Atributos de classe: 173 (veja `02-constantes-e-enums.md`)


### `AccessibleRole`  <sub>linha 679</sub>

AccessibleRole from IUIAutomation. Refer https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.accessiblerole?view=netframework-4.8

Atributos de classe: 64 (veja `02-constantes-e-enums.md`)


### `AccessibleState`  <sub>linha 750</sub>

AccessibleState from IUIAutomation. Refer https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.accessiblestates?view=netframework-4.8

Atributos: `Normal`, `Unavailable`, `Selected`, `Focused`, `Pressed`, `Checked`, `Mixed`, `Indeterminate`, `ReadOnly`, `HotTracked`, `Default`, `Expanded`, `Collapsed`, `Busy`, `Floating`, `Marqueed`, `Animated`, `Invisible`, `Offscreen`, `Sizeable`, `Moveable`, `SelfVoicing`, `Focusable`, `Selectable`, `Linked`, `Traversed`, `MultiSelectable`, `ExtSelectable`, `AlertLow`, `AlertMedium`, `AlertHigh`, `Protected`, `Valid`, `HasPopup`


### `AccessibleSelection`  <sub>linha 791</sub>

AccessibleSelection from IUIAutomation. Refer https://docs.microsoft.com/en-us/dotnet/api/system.windows.forms.accessibleselection?view=netframework-4.8

Atributos: `None_`, `TakeFocus`, `TakeSelection`, `ExtendSelection`, `AddSelection`, `RemoveSelection`


### `AnnotationType`  <sub>linha 804</sub>

AnnotationType from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/winauto/uiauto-annotation-type-identifiers

Atributos: `AdvancedProofingIssue`, `Author`, `CircularReferenceError`, `Comment`, `ConflictingChange`, `DataValidationError`, `DeletionChange`, `EditingLockedChange`, `Endnote`, `ExternalChange`, `Footer`, `Footnote`, `FormatChange`, `FormulaError`, `GrammarError`, `Header`, `Highlighted`, `InsertionChange`, `Mathematics`, `MoveChange`, `SpellingError`, `TrackChanges`, `Unknown`, `UnsyncedChange`


### `NavigateDirection`  <sub>linha 835</sub>

NavigateDirection from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/api/uiautomationcore/ne-uiautomationcore-navigatedirection

Atributos: `Parent`, `NextSibling`, `PreviousSibling`, `FirstChild`, `LastChild`


### `DockPosition`  <sub>linha 847</sub>

DockPosition from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/api/uiautomationcore/ne-uiautomationcore-dockposition

Atributos: `Top`, `Left`, `Bottom`, `Right`, `Fill`, `None_`


### `ScrollAmount`  <sub>linha 860</sub>

ScrollAmount from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/api/uiautomationcore/ne-uiautomationcore-scrollamount

Atributos: `LargeDecrement`, `SmallDecrement`, `NoAmount`, `LargeIncrement`, `SmallIncrement`


### `StyleId`  <sub>linha 872</sub>

StyleId from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/winauto/uiauto-style-identifiers

Atributos: `Custom`, `Heading1`, `Heading2`, `Heading3`, `Heading4`, `Heading5`, `Heading6`, `Heading7`, `Heading8`, `Heading9`, `Title`, `Subtitle`, `Normal`, `Emphasis`, `Quote`, `BulletedList`, `NumberedList`


### `RowOrColumnMajor`  <sub>linha 896</sub>

RowOrColumnMajor from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/api/uiautomationcore/ne-uiautomationcore-roworcolumnmajor

Atributos: `RowMajor`, `ColumnMajor`, `Indeterminate`


### `ExpandCollapseState`  <sub>linha 906</sub>

ExpandCollapseState from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/api/uiautomationcore/ne-uiautomationcore-expandcollapsestate

Atributos: `Collapsed`, `Expanded`, `PartiallyExpanded`, `LeafNode`


### `OrientationType`  <sub>linha 917</sub>

OrientationType from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/api/uiautomationcore/ne-uiautomationcore-orientationtype

Atributos: `None_`, `Horizontal`, `Vertical`


### `ToggleState`  <sub>linha 927</sub>

ToggleState from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/api/uiautomationcore/ne-uiautomationcore-togglestate

Atributos: `Off`, `On`, `Indeterminate`


### `TextPatternRangeEndpoint`  <sub>linha 937</sub>

TextPatternRangeEndpoint from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/api/uiautomationcore/ne-uiautomationcore-textpatternrangeendpoint

Atributos: `Start`, `End`


### `TextAttributeId`  <sub>linha 946</sub>

TextAttributeId from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/winauto/uiauto-textattribute-ids

Atributos de classe: 44 (veja `02-constantes-e-enums.md`)


### `TextUnit`  <sub>linha 997</sub>

TextUnit from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/api/uiautomationcore/ne-uiautomationcore-textunit

Atributos: `Character`, `Format`, `Word`, `Line`, `Paragraph`, `Page`, `Document`


### `ZoomUnit`  <sub>linha 1011</sub>

ZoomUnit from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/api/uiautomationcore/ne-uiautomationcore-zoomunit

Atributos: `NoAmount`, `LargeDecrement`, `SmallDecrement`, `LargeIncrement`, `SmallIncrement`


### `WindowInteractionState`  <sub>linha 1023</sub>

WindowInteractionState from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/api/uiautomationcore/ne-uiautomationcore-windowinteractionstate

Atributos: `Running`, `Closing`, `ReadyForUserInteraction`, `BlockedByModalWindow`, `NotResponding`


### `WindowVisualState`  <sub>linha 1035</sub>

WindowVisualState from IUIAutomation. Refer https://docs.microsoft.com/en-us/windows/win32/api/uiautomationcore/ne-uiautomationcore-windowvisualstate

Atributos: `Normal`, `Maximized`, `Minimized`


### `ConsoleColor`  <sub>linha 1045</sub>

ConsoleColor from Win32.

Atributos: `Default`, `Black`, `DarkBlue`, `DarkGreen`, `DarkCyan`, `DarkRed`, `DarkMagenta`, `DarkYellow`, `Gray`, `DarkGray`, `Blue`, `Green`, `Cyan`, `Red`, `Magenta`, `Yellow`, `White`


### `GAFlag`  <sub>linha 1066</sub>

GAFlag from Win32.

Atributos: `Parent`, `Root`, `RootOwner`


### `MouseEventFlag`  <sub>linha 1073</sub>

MouseEventFlag from Win32.

Atributos: `Move`, `LeftDown`, `LeftUp`, `RightDown`, `RightUp`, `MiddleDown`, `MiddleUp`, `XDown`, `XUp`, `Wheel`, `HWheel`, `MoveNoCoalesce`, `VirtualDesk`, `Absolute`


### `KeyboardEventFlag`  <sub>linha 1091</sub>

KeyboardEventFlag from Win32.

Atributos: `KeyDown`, `ExtendedKey`, `KeyUp`, `KeyUnicode`, `KeyScanCode`


### `InputType`  <sub>linha 1100</sub>

InputType from Win32

Atributos: `Mouse`, `Keyboard`, `Hardware`


### `ModifierKey`  <sub>linha 1107</sub>

ModifierKey from Win32.

Atributos: `Alt`, `Control`, `Shift`, `Win`, `NoRepeat`


### `SW`  <sub>linha 1116</sub>

ShowWindow params from Win32.

Atributos: `Hide`, `ShowNormal`, `Normal`, `ShowMinimized`, `ShowMaximized`, `Maximize`, `ShowNoActivate`, `Show`, `Minimize`, `ShowMinNoActive`, `ShowNA`, `Restore`, `ShowDefault`, `ForceMinimize`, `Max`


### `SWP`  <sub>linha 1135</sub>

SetWindowPos params from Win32.

Atributos: `HWND_Top`, `HWND_Bottom`, `HWND_Topmost`, `HWND_NoTopmost`, `SWP_NoSize`, `SWP_NoMove`, `SWP_NoZOrder`, `SWP_NoRedraw`, `SWP_NoActivate`, `SWP_FrameChanged`, `SWP_ShowWindow`, `SWP_HideWindow`, `SWP_NoCopyBits`, `SWP_NoOwnerZOrder`, `SWP_NoSendChanging`, `SWP_DrawFrame`, `SWP_NoReposition`, `SWP_DeferErase`, `SWP_AsyncWindowPos`


### `MB`  <sub>linha 1158</sub>

MessageBox flags from Win32.

Atributos: `Ok`, `OkCancel`, `AbortRetryIgnore`, `YesNoCancel`, `YesNo`, `RetryCancel`, `CancelTryContinue`, `IconHand`, `IconQuestion`, `IconExclamation`, `IconAsterisk`, `UserIcon`, `IconWarning`, `IconError`, `IconInformation`, `IconStop`, `DefButton1`, `DefButton2`, `DefButton3`, `DefButton4`, `ApplModal`, `SystemModal`, `TaskModal`, `Help`, `NoFocus`, `SetForeground`, `DefaultDesktopOnly`, `Topmost`, `Right`, `RtlReading`, `ServiceNotification`, `ServiceNotificationNT3X`, `TypeMask`, `IconMask`, `DefMask`, `ModeMask`, `MiscMask`, `IdOk`, `IdCancel`, `IdAbort`, `IdRetry`, `IdIgnore`, `IdYes`, `IdNo`, `IdClose`, `IdHelp`, `IdTryAgain`, `IdContinue`, `IdTimeout`


### `GWL`  <sub>linha 1213</sub>

Atributos: `ExStyle`, `HInstance`, `HwndParent`, `ID`, `Style`, `UserData`, `WndProc`


### `ProcessDpiAwareness`  <sub>linha 1223</sub>

Atributos: `DpiUnaware`, `SystemDpiAware`, `PerMonitorDpiAware`


### `DpiAwarenessContext`  <sub>linha 1229</sub>

Atributos: `Unaware`, `SystemAware`, `PerMonitorAware`, `PerMonitorAwareV2`, `UnawareGdiScaled`


### `Keys`  <sub>linha 1237</sub>

Key codes from Win32.

Atributos de classe: 176 (veja `02-constantes-e-enums.md`)


### `ConsoleScreenBufferInfo`(ctypes.Structure)  <sub>linha 1658</sub>

Atributos: `_fields_`


### `MOUSEINPUT`(ctypes.Structure)  <sub>linha 1668</sub>

Atributos: `_fields_`


### `KEYBDINPUT`(ctypes.Structure)  <sub>linha 1677</sub>

Atributos: `_fields_`


### `HARDWAREINPUT`(ctypes.Structure)  <sub>linha 1685</sub>

Atributos: `_fields_`


### `_INPUTUnion`(ctypes.Union)  <sub>linha 1691</sub>

Atributos: `_fields_`


### `INPUT`(ctypes.Structure)  <sub>linha 1697</sub>

Atributos: `_fields_`


### `Rect`  <sub>linha 1702</sub>

class Rect, like `ctypes.wintypes.RECT`.

| Linha | Membro | Docstring |
|---|---|---|
| 1713 | `width(self)` |  |
| 1716 | `height(self)` |  |
| 1719 | `xcenter(self)` |  |
| 1722 | `ycenter(self)` |  |
| 1725 | `isempty(self)` |  |
| 1728 | `contains(self, x: int, y: int)` |  |
| 1731 | `intersect(self, rect: 'Rect')` |  |
| 1735 | `offset(self, x: int, y: int)` |  |
| 1741 | `__eq__(self, rect)` |  |
| 1744 | `__str__(self)` |  |
| 1747 | `__repr__(self)` |  |

### `ClipboardFormat`  <sub>linha 1751</sub>

Atributos: `CF_TEXT`, `CF_BITMAP`, `CF_METAFILEPICT`, `CF_SYLK`, `CF_DIF`, `CF_TIFF`, `CF_OEMTEXT`, `CF_DIB`, `CF_PALETTE`, `CF_PENDATA`, `CF_RIFF`, `CF_WAVE`, `CF_UNICODETEXT`, `CF_ENHMETAFILE`, `CF_HDROP`, `CF_LOCALE`, `CF_DIBV5`, `CF_MAX`, `CF_HTML`


### `tagPROCESSENTRY32`(ctypes.Structure)  <sub>linha 2961</sub>

Atributos: `_fields_`


### `ProcessInfo`  <sub>linha 2976</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 2985 | `__str__(self)` |  |
| 2989 | `__repr__(self)` |  |

### `Logger`  <sub>linha 3120</sub>

Logger for print and log. Support for printing log with different colors on console.

Atributos: `FilePath`, `FileObj`, `FlushTime`, `_SelfFileName`, `ColorNames`, `LogColorfully`, `WriteColorfully`, `WriteLineColorfully`

| Linha | Membro | Docstring |
|---|---|---|
| 3148 | `static SetLogFile(logFile: Union[TextIOWrapper, str])` | logFile: file object or str. If logFile is '', no log file will be written. The previous log file will be closed immediately. |
| 3165 | `static Write(log: Any, consoleColor: int=ConsoleColor.Default, writeToFile: bool=True, printToStdout: bool=True, logFile: Optional[str]=None, printTruncateLen: int=0)` | log: any type. consoleColor: int, a value in class `ConsoleColor`, such as `ConsoleColor.DarkGreen`. writeToFile: bool. |
| 3223 | `static WriteLine(log: Any, consoleColor: int=ConsoleColor.Default, writeToFile: bool=True, printToStdout: bool=True, logFile: Optional[str]=None)` | log: any type. consoleColor: int, a value in class `ConsoleColor`, such as `ConsoleColor.DarkGreen`. writeToFile: bool. |
| 3234 | `static ColorfullyWrite(log: str, consoleColor: int=ConsoleColor.Default, writeToFile: bool=True, printToStdout: bool=True, logFile: Optional[str]=None)` | log: str. consoleColor: int, a value in class `ConsoleColor`, such as `ConsoleColor.DarkGreen`. writeToFile: bool. |
| 3272 | `static ColorfullyWriteLine(log: str, consoleColor: int=ConsoleColor.Default, writeToFile: bool=True, printToStdout: bool=True, logFile: Optional[str]=None)` | log: str. consoleColor: int, a value in class `ConsoleColor`, such as `ConsoleColor.DarkGreen`. writeToFile: bool. |
| 3285 | `static Log(log: Any='', consoleColor: int=ConsoleColor.Default, writeToFile: bool=True, printToStdout: bool=True, logFile: Optional[str]=None)` | log: any type. consoleColor: int, a value in class `ConsoleColor`, such as `ConsoleColor.DarkGreen`. writeToFile: bool. |
| 3307 | `static ColorfullyLog(log: str='', consoleColor: int=ConsoleColor.Default, writeToFile: bool=True, printToStdout: bool=True, logFile: Optional[str]=None)` | log: any type. consoleColor: int, a value in class `ConsoleColor`, such as `ConsoleColor.DarkGreen`. writeToFile: bool. |
| 3331 | `static DeleteLog()` | Delete log file. |

### `RotateFlipType`  <sub>linha 3349</sub>

Atributos: `RotateNoneFlipNone`, `Rotate90FlipNone`, `Rotate180FlipNone`, `Rotate270FlipNone`, `RotateNoneFlipX`, `Rotate90FlipX`, `Rotate180FlipX`, `Rotate270FlipX`, `RotateNoneFlipY`, `Rotate90FlipY`, `Rotate180FlipY`, `Rotate270FlipY`, `RotateNoneFlipXY`, `Rotate90FlipXY`, `Rotate180FlipXY`, `Rotate270FlipXY`


### `RawFormat`  <sub>linha 3368</sub>

Atributos: `Undefined`, `MemoryBMP`, `BMP`, `EMF`, `WMF`, `JPEG`, `PNG`, `GIF`, `TIFF`, `EXIF`, `Icon`


### `Bitmap`  <sub>linha 3382</sub>

A simple Bitmap class wraps Windows GDI+ Gdiplus::Bitmap, but may not have high efficiency. The color format is Gdiplus::PixelFormat32bppARGB 0xAARRGGBB, byte order is B G R A.

Atributos: `Release`

| Linha | Membro | Docstring |
|---|---|---|
| 3400 | `__del__(self)` |  |
| 3403 | `__enter__(self)` |  |
| 3406 | `__exit__(self, exceptionType, exceptionValue, exceptionTraceback)` |  |
| 3409 | `__bool__(self)` |  |
| 3412 | `_GetSize(self)` |  |
| 3417 | `Close(self)` | Close the underlying Gdiplus::Bitmap object. |
| 3428 | `prop Width` | Property Width. Return int. |
| 3436 | `prop Height` | Property Height. Return int. |
| 3444 | `static FromHandle(handle: int, left: int, top: int, right: int, bottom: int, captureCursor: bool=False)` | Create a `Bitmap` from a native window handle. handle: int, the handle of a native window. left: int. |
| 3473 | `static FromControl(control: 'Control', x: int=0, y: int=0, width: int=0, height: int=0, captureCursor: bool=False)` | Create a `Bitmap` from a `Control`. control: `Control` or its subclass. x: int. |
| 3532 | `static _FromGdiplusBitmap(cbmp: int)` | Return `Bitmap`'s subclass instance or None. |
| 3572 | `static FromBytes(data: Union[bytes, bytearray], format: str=None, width: int=None, height: int=None)` | Create a `Bitmap` instance from raw BGRA pixel data or image file byte content. data: bytes or bytearray. format (str, optional): Specifies the format of the input data. |
| 3599 | `static FromFile(filePath: str)` | Create a `Bitmap` from a file path. filePath: str. Return `Bitmap`'s subclass instance or None. |
| 3609 | `static FromNDArray(image: 'numpy.ndarray')` | Create a `MemoryBMP` from a numpy.ndarray(BGR or BGRA). |
| 3630 | `static FromPILImage(image: 'PIL.Image.Image')` | Create a `MemoryBMP` from a PIL Image. |
| 3659 | `ToFile(self, savePath: str, *, quality: int=None)` | Save to a file. savePath: str, should end with .bmp, .jpg, .jpeg, .png, .gif, .tif, .tiff. quality: int, 1-100, only used when save to jpeg. |
| 3681 | `ToBytes(self, format: str, *, quality: int=None)` | Convert to a bytearray in the specified format. format: str, The desired output format. Supported formats include: - 'BGRA': Raw pixel data without any file header, byte order is B G R A. |
| 3721 | `ToPILImage(self)` | Convert to a PIL image. usage: image = bitmap.ToPILImage() |
| 3733 | `ToNDArray(self)` | Convert to a numpy.ndarray(shape=(height,width,4), compatible with OpenCV). usage: bgraImage = bitmap.ToNDArray() |
| 3744 | `GetRawFormat(self)` | return a int value in class `RawFormat` |
| 3754 | `GetRawFormatStr(self)` | return the string description of `RawFormat` value |
| 3762 | `GetPixelColor(self, x: int, y: int)` | Get color value of a pixel. x: int. y: int. |
| 3775 | `SetPixelColor(self, x: int, y: int, argb: int)` | Set color value of a pixel. x: int. y: int. |
| 3786 | `GetPixelColorsHorizontally(self, x: int, y: int, count: int)` | x: int. y: int. count: int. |
| 3799 | `SetPixelColorsHorizontally(self, x: int, y: int, colors: Sequence[int])` | Set pixel colors form x,y horizontally. x: int. y: int. |
| 3816 | `GetPixelColorsVertically(self, x: int, y: int, count: int)` | x: int. y: int. count: int. |
| 3829 | `SetPixelColorsVertically(self, x: int, y: int, colors: Sequence[int])` | Set pixel colors form x,y vertically. x: int. y: int. |
| 3846 | `GetPixelColorsOfRow(self, y: int)` | y: int, row index. Return `ctypes.Array`, an iterable array of int values in ARGB(0xAARRGGBB) color format of y row. |
| 3853 | `GetPixelColorsOfColumn(self, x: int)` | x: int, column index. Return `ctypes.Array`, an iterable array of int values in ARGB(0xAARRGGBB) color format of x column. |
| 3860 | `GetPixelColorsOfRect(self, x: int, y: int, width: int, height: int)` | x: int. y: int. width: int. |
| 3873 | `SetPixelColorsOfRect(self, x: int, y: int, width: int, height: int, colors: Sequence[int])` | x: int. y: int. width: int. |
| 3890 | `GetPixelColorsOfRects(self, rects: List[Tuple[int, int, int, int]])` | rects: List[Tuple[int, int, int, int]], such as [(0,0,10,10), (10,10,20,20), (x,y,width,height)]. Return List[ctypes.Array], a list whose elements are ctypes.Array which is an iterable array of int values in ARGB(0xAARRGGBB) color format. |
| 3898 | `GetAllPixelColors(self)` | Return `ctypes.Array`, an iterable array of int values in ARGB(0xAARRGGBB) color format. |
| 3904 | `SetAllPixelColors(self, colors: Sequence[int])` | colors: Sequence[int], a sequence of int values in ARGB(0xAARRGGBB) color format, it's length must equal to width*height, use ctypes.Array for better performance, such as `ctypes.c_uint32 * (width*height)`. Return bool. |
| 3912 | `Clear(self, color: int=4294967295, x: int=0, y: int=0, width: int=0, height: int=0)` | Set the color of rect(x,y,width,height). color: int, ARGB(0xAARRGGBB) color format. x: int. |
| 3930 | `Clone(self)` | Return `Bitmap`'s subclass instance. The cloned Bitmap's RawFormat is same as original Bitmap. If Bitmap is multiple frames, the cloned Bitmap is also multiple frames. |
| 3939 | `Copy(self, x: int=0, y: int=0, width: int=0, height: int=0)` | x: int, must >= 0. y: int, must >= 0. width: int, must <= self.Width-x. |
| 3959 | `Paste(self, x: int, y: int, bitmap: 'Bitmap')` | Paste bitmap to (x,y) of self, modify the original Bitmap, if x < 0 or x+bitmap.Width > self.Width, only the intersection part of bitmap is pasted, if y < 0 or y+bitmap.Height > self.Height, only the intersection part of bitmap is pasted. |
| 3978 | `PastePart(self, dstX: int, dstY: int, srcBitmap: 'Bitmap', srcX: int=0, srcY: int=0, srcWidth: int=0, srcHeight: int=0)` | Paste (srcX, srcY, srcWidth, srcHeight) of bitmap to (dstX, dstY) of self, modify the original Bitmap, only the intersection part of the bitmap is pasted. dstX: int, must >= 0. |
| 4002 | `Resize(self, width: int, height: int)` | Resize a copy of the original to size (width, height), the original Bitmap is not modified. width: int. height: int. |
| 4012 | `Rotate(self, angle: float, backgroundColor: int=4294967295)` | Rotate angle degrees clockwise around the center point. Return a copy of the original with angle, the original Bitmap is not modified. angle: float, closewise. |
| 4023 | `RotateFlip(self, rotateFlip: int)` | Rotate 90*n or Filp a copy of the original, the original Bitmap is not modified. rotateFlip: int, a value in class `RotateFlipType`. Return a new `MemoryBMP`, the original is not modified. |
| 4034 | `RotateWithSameSize(self, dx: float, dy: float, angle: float, backgroundColor: int=4294967295)` | Rotate angle degrees clockwise around the point (dx, dy) from a copy, the original Bitmap is not modified. angle: float, closewise. backgroundColor: int, ARGB(0xAARRGGBB) color format. |
| 4045 | `__str__(self)` |  |
| 4048 | `__repr__(self)` |  |

### `MultiFrameBitmap`(Bitmap)  <sub>linha 4052</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 4058 | `SelectActiveFrame(self, index: int)` |  |
| 4062 | `GetFrameCount(self)` |  |
| 4065 | `__iter__(self)` |  |
| 4069 | `__next__(self)` |  |
| 4078 | `__str__(self)` |  |
| 4081 | `__repr__(self)` |  |

### `MemoryBMP`(Bitmap)  <sub>linha 4085</sub>


### `BMP`(Bitmap)  <sub>linha 4089</sub>


### `JPEG`(Bitmap)  <sub>linha 4093</sub>


### `PNG`(Bitmap)  <sub>linha 4097</sub>


### `EMF`(Bitmap)  <sub>linha 4101</sub>


### `WMF`(Bitmap)  <sub>linha 4105</sub>


### `ICON`(Bitmap)  <sub>linha 4109</sub>


### `EXIF`(Bitmap)  <sub>linha 4113</sub>


### `TIFF`(MultiFrameBitmap)  <sub>linha 4117</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 4119 | `static ToTiffFile(path: str, bitmaps: List['Bitmap'])` | Save a list of bitmaps to a multi frame tiff file. path: str, file path. bitmaps: List[Bitmap]. |

### `GIF`(MultiFrameBitmap)  <sub>linha 4133</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 4138 | `_GetGifDealy(self)` |  |
| 4149 | `GetFrameDelay(self, index: int)` | return frame delay in milliseconds |
| 4155 | `GetFrameDelays(self)` | return a list of frame delays in milliseconds |
| 4162 | `static ToGifFile(path: str, bitmaps: List[Bitmap], delays: List[int]=None)` | Save a list of bitmaps to a multi frame gif file. path: str, file path. bitmaps: List[Bitmap]. |

### `AnnotationPattern`  <sub>linha 4484</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 4490 | `prop AnnotationTypeId` | Property AnnotationTypeId. Call IUIAutomationAnnotationPattern::get_CurrentAnnotationTypeId. Return int, a value in class `AnnotationType`. |
| 4500 | `prop AnnotationTypeName` | Property AnnotationTypeName. Call IUIAutomationAnnotationPattern::get_CurrentAnnotationTypeName. |
| 4509 | `prop Author` | Property Author. Call IUIAutomationAnnotationPattern::get_CurrentAuthor. |
| 4518 | `prop DateTime` | Property DateTime. Call IUIAutomationAnnotationPattern::get_CurrentDateTime. |
| 4527 | `prop Target` | Property Target. Call IUIAutomationAnnotationPattern::get_CurrentTarget. Return `Control` subclass, the element that is being annotated. |

### `CustomNavigationPattern`  <sub>linha 4538</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 4543 | `Navigate(self, direction: int)` | Call IUIAutomationCustomNavigationPattern::Navigate. Get the next control in the specified direction within the logical UI tree. direction: int, a value in class `NavigateDirection`. |

### `DockPattern`  <sub>linha 4555</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 4561 | `prop DockPosition` | Property DockPosition. Call IUIAutomationDockPattern::get_CurrentDockPosition. Return int, a value in class `DockPosition`. |
| 4570 | `SetDockPosition(self, dockPosition: int, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationDockPattern::SetDockPosition. dockPosition: int, a value in class `DockPosition`. waitTime: float. |

### `DragPattern`  <sub>linha 4582</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 4588 | `prop DropEffect` | Property DropEffect. Call IUIAutomationDragPattern::get_CurrentDropEffect. Return str, a localized string that indicates what happens |
| 4599 | `prop DropEffects` | Property DropEffects. Call IUIAutomationDragPattern::get_CurrentDropEffects, todo SAFEARRAY. Return List[str], a list of localized strings that enumerate the full set of effects |
| 4610 | `prop IsGrabbed` | Property IsGrabbed. Call IUIAutomationDragPattern::get_CurrentIsGrabbed. Return bool, indicates whether the user has grabbed this element as part of a drag-and-drop operation. |
| 4619 | `GetGrabbedItems(self)` | Call IUIAutomationDragPattern::GetCurrentGrabbedItems. Return List[Control], a list of `Control` subclasses that represent the full set of items that the user is dragging as part of a drag operation. |

### `DropTargetPattern`  <sub>linha 4638</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 4644 | `prop DropTargetEffect` | Property DropTargetEffect. Call IUIAutomationDropTargetPattern::get_CurrentDropTargetEffect. Return str, a localized string that describes what happens |
| 4655 | `prop DropTargetEffects` | Property DropTargetEffects. Call IUIAutomationDropTargetPattern::get_CurrentDropTargetEffects, todo SAFEARRAY. Return List[str], a list of localized strings that enumerate the full set of effects |

### `ExpandCollapsePattern`  <sub>linha 4667</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 4673 | `prop ExpandCollapseState` | Property ExpandCollapseState. Call IUIAutomationExpandCollapsePattern::get_CurrentExpandCollapseState. Return int, a value in class ExpandCollapseState. |
| 4682 | `Collapse(self, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationExpandCollapsePattern::Collapse. waitTime: float. Return bool, True if succeed otherwise False. |
| 4697 | `Expand(self, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationExpandCollapsePattern::Expand. waitTime: float. Return bool, True if succeed otherwise False. |

### `GridItemPattern`  <sub>linha 4713</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 4719 | `prop Column` | Property Column. Call IUIAutomationGridItemPattern::get_CurrentColumn. Return int, the zero-based index of the column that contains the item. |
| 4729 | `prop ColumnSpan` | Property ColumnSpan. Call IUIAutomationGridItemPattern::get_CurrentColumnSpan. Return int, the number of columns spanned by the grid item. |
| 4739 | `prop ContainingGrid` | Property ContainingGrid. Call IUIAutomationGridItemPattern::get_CurrentContainingGrid. Return `Control` subclass, the element that contains the grid item. |
| 4749 | `prop Row` | Property Row. Call IUIAutomationGridItemPattern::get_CurrentRow. Return int, the zero-based index of the row that contains the grid item. |
| 4759 | `prop RowSpan` | Property RowSpan. Call IUIAutomationGridItemPattern::get_CurrentRowSpan. Return int, the number of rows spanned by the grid item. |

### `GridPattern`  <sub>linha 4769</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 4775 | `prop ColumnCount` | Property ColumnCount. Call IUIAutomationGridPattern::get_CurrentColumnCount. Return int, the number of columns in the grid. |
| 4785 | `prop RowCount` | Property RowCount. Call IUIAutomationGridPattern::get_CurrentRowCount. Return int, the number of rows in the grid. |
| 4794 | `GetItem(self, row: int, column: int)` | Call IUIAutomationGridPattern::GetItem. Return `Control` subclass, a control representing an item in the grid. |

### `InvokePattern`  <sub>linha 4803</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 4808 | `Invoke(self, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationInvokePattern::Invoke. Invoke the action of a control, such as a button click. waitTime: float. |

### `ItemContainerPattern`  <sub>linha 4821</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 4826 | `FindItemByProperty(self, control: 'Control', propertyId: int, propertyValue)` | Call IUIAutomationItemContainerPattern::FindItemByProperty. control: `Control` or its subclass. propertyValue: COM VARIANT according to propertyId? todo. |

### `LegacyIAccessiblePattern`  <sub>linha 4839</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 4845 | `prop ChildId` | Property ChildId. Call IUIAutomationLegacyIAccessiblePattern::get_CurrentChildId. Return int, the Microsoft Active Accessibility child identifier for the element. |
| 4855 | `prop DefaultAction` | Property DefaultAction. Call IUIAutomationLegacyIAccessiblePattern::get_CurrentDefaultAction. Return str, the Microsoft Active Accessibility current default action for the element. |
| 4865 | `prop Description` | Property Description. Call IUIAutomationLegacyIAccessiblePattern::get_CurrentDescription. Return str, the Microsoft Active Accessibility description of the element. |
| 4875 | `prop Help` | Property Help. Call IUIAutomationLegacyIAccessiblePattern::get_CurrentHelp. Return str, the Microsoft Active Accessibility help string for the element. |
| 4885 | `prop KeyboardShortcut` | Property KeyboardShortcut. Call IUIAutomationLegacyIAccessiblePattern::get_CurrentKeyboardShortcut. Return str, the Microsoft Active Accessibility keyboard shortcut property for the element. |
| 4895 | `prop Name` | Property Name. Call IUIAutomationLegacyIAccessiblePattern::get_CurrentName. Return str, the Microsoft Active Accessibility name property of the element. |
| 4905 | `prop Role` | Property Role. Call IUIAutomationLegacyIAccessiblePattern::get_CurrentRole. Return int, a value in calss `AccessibleRole`, the Microsoft Active Accessibility role identifier. |
| 4915 | `prop State` | Property State. Call IUIAutomationLegacyIAccessiblePattern::get_CurrentState. Return int, a value in calss `AccessibleState`, the Microsoft Active Accessibility state identifier. |
| 4925 | `prop Value` | Property Value. Call IUIAutomationLegacyIAccessiblePattern::get_CurrentValue. Return str, the Microsoft Active Accessibility value property. |
| 4934 | `DoDefaultAction(self, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationLegacyIAccessiblePattern::DoDefaultAction. Perform the Microsoft Active Accessibility default action for the element. waitTime: float. |
| 4946 | `GetSelection(self)` | Call IUIAutomationLegacyIAccessiblePattern::GetCurrentSelection. Return List[Control], a list of `Control` subclasses, the Microsoft Active Accessibility property that identifies the selected children of this element. |
| 4964 | `GetIAccessible(self)` | Call IUIAutomationLegacyIAccessiblePattern::GetIAccessible, todo. Return an IAccessible object that corresponds to the Microsoft UI Automation element. |
| 4973 | `Select(self, flagsSelect: int, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationLegacyIAccessiblePattern::Select. Perform a Microsoft Active Accessibility selection. flagsSelect: int, a value in `AccessibleSelection`. |
| 4986 | `SetValue(self, value: str, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationLegacyIAccessiblePattern::SetValue. Set the Microsoft Active Accessibility value property for the element. value: str. |

### `MultipleViewPattern`  <sub>linha 5000</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5006 | `prop CurrentView` | Property CurrentView. Call IUIAutomationMultipleViewPattern::get_CurrentCurrentView. Return int, the control-specific identifier of the current view of the control. |
| 5015 | `GetSupportedViews(self)` | Call IUIAutomationMultipleViewPattern::GetCurrentSupportedViews, todo. Return List[int], a list of int, control-specific view identifiers. |
| 5023 | `GetViewName(self, view: int)` | Call IUIAutomationMultipleViewPattern::GetViewName. view: int, the control-specific view identifier. Return str, the name of a control-specific view. |
| 5032 | `SetView(self, view: int)` | Call IUIAutomationMultipleViewPattern::SetCurrentView. Set the view of the control. view: int, the control-specific view identifier. |

### `ObjectModelPattern`  <sub>linha 5043</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5048 | `GetUnderlyingObjectModel(self)` | Call IUIAutomationObjectModelPattern::GetUnderlyingObjectModel, todo. Return `ctypes.POINTER(comtypes.IUnknown)`, an interface used to access the underlying object model of the provider. |

### `RangeValuePattern`  <sub>linha 5057</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5063 | `prop IsReadOnly` | Property IsReadOnly. Call IUIAutomationRangeValuePattern::get_CurrentIsReadOnly. Return bool, indicates whether the value of the element can be changed. |
| 5073 | `prop LargeChange` | Property LargeChange. Call IUIAutomationRangeValuePattern::get_CurrentLargeChange. Return float, the value that is added to or subtracted from the value of the control |
| 5084 | `prop Maximum` | Property Maximum. Call IUIAutomationRangeValuePattern::get_CurrentMaximum. Return float, the maximum value of the control. |
| 5094 | `prop Minimum` | Property Minimum. Call IUIAutomationRangeValuePattern::get_CurrentMinimum. Return float, the minimum value of the control. |
| 5104 | `prop SmallChange` | Property SmallChange. Call IUIAutomationRangeValuePattern::get_CurrentSmallChange. Return float, the value that is added to or subtracted from the value of the control |
| 5115 | `prop Value` | Property Value. Call IUIAutomationRangeValuePattern::get_CurrentValue. Return float, the value of the control. |
| 5124 | `SetValue(self, value: float, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationRangeValuePattern::SetValue. Set the value of the control. value: int. |

### `ScrollItemPattern`  <sub>linha 5138</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5143 | `ScrollIntoView(self, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationScrollItemPattern::ScrollIntoView. waitTime: float. Return bool, True if succeed otherwise False. |

### `ScrollPattern`  <sub>linha 5155</sub>

Atributos: `NoScrollValue`

| Linha | Membro | Docstring |
|---|---|---|
| 5163 | `prop HorizontallyScrollable` | Property HorizontallyScrollable. Call IUIAutomationScrollPattern::get_CurrentHorizontallyScrollable. Return bool, indicates whether the element can scroll horizontally. |
| 5173 | `prop HorizontalScrollPercent` | Property HorizontalScrollPercent. Call IUIAutomationScrollPattern::get_CurrentHorizontalScrollPercent. Return float, the horizontal scroll position. |
| 5183 | `prop HorizontalViewSize` | Property HorizontalViewSize. Call IUIAutomationScrollPattern::get_CurrentHorizontalViewSize. Return float, the horizontal size of the viewable region of a scrollable element. |
| 5193 | `prop VerticallyScrollable` | Property VerticallyScrollable. Call IUIAutomationScrollPattern::get_CurrentVerticallyScrollable. Return bool, indicates whether the element can scroll vertically. |
| 5203 | `prop VerticalScrollPercent` | Property VerticalScrollPercent. Call IUIAutomationScrollPattern::get_CurrentVerticalScrollPercent. Return float, the vertical scroll position. |
| 5213 | `prop VerticalViewSize` | Property VerticalViewSize. Call IUIAutomationScrollPattern::get_CurrentVerticalViewSize. Return float, the vertical size of the viewable region of a scrollable element. |
| 5222 | `Scroll(self, horizontalAmount: int, verticalAmount: int, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationScrollPattern::Scroll. Scroll the visible region of the content area horizontally and vertically. horizontalAmount: int, a value in ScrollAmount. |
| 5236 | `SetScrollPercent(self, horizontalPercent: float, verticalPercent: float, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationScrollPattern::SetScrollPercent. Set the horizontal and vertical scroll positions as a percentage of the total content area within the UI Automation element. horizontalPercent: float or int, a value in [0, 100] or ScrollPattern.NoScrollValue( |

### `SelectionItemPattern`  <sub>linha 5251</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5256 | `AddToSelection(self, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationSelectionItemPattern::AddToSelection. Add the current element to the collection of selected items. waitTime: float. |
| 5269 | `prop IsSelected` | Property IsSelected. Call IUIAutomationScrollPattern::get_CurrentIsSelected. Return bool, indicates whether this item is selected. |
| 5279 | `prop SelectionContainer` | Property SelectionContainer. Call IUIAutomationScrollPattern::get_CurrentSelectionContainer. Return `Control` subclass, the element that supports IUIAutomationSelectionPattern and acts as the container for this item. |
| 5289 | `RemoveFromSelection(self, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationSelectionItemPattern::RemoveFromSelection. Remove this element from the selection. waitTime: float. |
| 5301 | `Select(self, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationSelectionItemPattern::Select. Clear any selected items and then select the current element. waitTime: float. |

### `SelectionPattern`  <sub>linha 5314</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5320 | `prop CanSelectMultiple` | Property CanSelectMultiple. Call IUIAutomationSelectionPattern::get_CurrentCanSelectMultiple. Return bool, indicates whether more than one item in the container can be selected at one time. |
| 5330 | `prop IsSelectionRequired` | Property IsSelectionRequired. Call IUIAutomationSelectionPattern::get_CurrentIsSelectionRequired. Return bool, indicates whether at least one item must be selected at all times. |
| 5339 | `GetSelection(self)` | Call IUIAutomationSelectionPattern::GetCurrentSelection. Return List[Control], a list of `Control` subclasses, the selected elements in the container.. |

### `SpreadsheetItemPattern`  <sub>linha 5357</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5363 | `prop Formula` | Property Formula. Call IUIAutomationSpreadsheetItemPattern::get_CurrentFormula. Return str, the formula for this cell. |
| 5372 | `GetAnnotationObjects(self)` | Call IUIAutomationSelectionPattern::GetCurrentAnnotationObjects. Return List[Control], a list of `Control` subclasses representing the annotations associated with this spreadsheet cell. |
| 5389 | `GetAnnotationTypes(self)` | Call IUIAutomationSelectionPattern::GetCurrentAnnotationTypes. Return List[int], a list of int values in class `AnnotationType`, indicating the types of annotations that are associated with this spreadsheet cell. |

### `SpreadsheetPattern`  <sub>linha 5399</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5404 | `GetItemByName(self, name: str)` | Call IUIAutomationSpreadsheetPattern::GetItemByName. name: str. Return `Control` subclass or None, represents the spreadsheet cell that has the specified name.. |

### `StylesPattern`  <sub>linha 5415</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5421 | `prop ExtendedProperties` | Property ExtendedProperties. Call IUIAutomationStylesPattern::get_CurrentExtendedProperties. Return str, a localized string that contains the list of extended properties for an element in a document. |
| 5431 | `prop FillColor` | Property FillColor. Call IUIAutomationStylesPattern::get_CurrentFillColor. Return int, the fill color of an element in a document. |
| 5441 | `prop FillPatternColor` | Property FillPatternColor. Call IUIAutomationStylesPattern::get_CurrentFillPatternColor. Return int, the color of the pattern used to fill an element in a document. |
| 5451 | `prop Shape` | Property Shape. Call IUIAutomationStylesPattern::get_CurrentShape. Return str, the shape of an element in a document. |
| 5461 | `prop StyleId` | Property StyleId. Call IUIAutomationStylesPattern::get_CurrentStyleId. Return int, a value in class `StyleId`, the visual style associated with an element in a document. |
| 5471 | `prop StyleName` | Property StyleName. Call IUIAutomationStylesPattern::get_CurrentStyleName. Return str, the name of the visual style associated with an element in a document. |

### `SynchronizedInputPattern`  <sub>linha 5481</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5486 | `Cancel(self)` | Call IUIAutomationSynchronizedInputPattern::Cancel. Cause the Microsoft UI Automation provider to stop listening for mouse or keyboard input. Return bool, True if succeed otherwise False. |
| 5495 | `StartListening(self)` | Call IUIAutomationSynchronizedInputPattern::StartListening. Cause the Microsoft UI Automation provider to start listening for mouse or keyboard input. Return bool, True if succeed otherwise False. |

### `TableItemPattern`  <sub>linha 5505</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5510 | `GetColumnHeaderItems(self)` | Call IUIAutomationTableItemPattern::GetCurrentColumnHeaderItems. Return List[Control], a list of `Control` subclasses, the column headers associated with a table item or cell. |
| 5527 | `GetRowHeaderItems(self)` | Call IUIAutomationTableItemPattern::GetCurrentRowHeaderItems. Return List[Control], a list of `Control` subclasses, the row headers associated with a table item or cell. |

### `TablePattern`  <sub>linha 5545</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5551 | `prop RowOrColumnMajor` | Property RowOrColumnMajor. Call IUIAutomationTablePattern::get_CurrentRowOrColumnMajor. Return int, a value in class `RowOrColumnMajor`, the primary direction of traversal for the table. |
| 5560 | `GetColumnHeaders(self)` | Call IUIAutomationTablePattern::GetCurrentColumnHeaders. Return List[Control], a list of `Control` subclasses, representing all the column headers in a table.. |
| 5577 | `GetRowHeaders(self)` | Call IUIAutomationTablePattern::GetCurrentRowHeaders. Return List[Control], a list of `Control` subclasses, representing all the row headers in a table. |

### `TextRange`  <sub>linha 5595</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5602 | `AddToSelection(self, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationTextRange::AddToSelection. Add the text range to the collection of selected text ranges in a control that supports multiple, disjoint spans of selected text. waitTime: float. |
| 5614 | `Clone(self)` | Call IUIAutomationTextRange::Clone. return `TextRange`, identical to the original and inheriting all properties of the original. |
| 5622 | `Compare(self, textRange: 'TextRange')` | Call IUIAutomationTextRange::Compare. textRange: `TextRange`. Return bool, specifies whether this text range has the same endpoints as another text range. |
| 5631 | `CompareEndpoints(self, srcEndPoint: int, textRange: 'TextRange', targetEndPoint: int)` | Call IUIAutomationTextRange::CompareEndpoints. srcEndPoint: int, a value in class `TextPatternRangeEndpoint`. textRange: `TextRange`. |
| 5644 | `ExpandToEnclosingUnit(self, unit: int, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationTextRange::ExpandToEnclosingUnit. Normalize the text range by the specified text unit. The range is expanded if it is smaller than the specified unit, |
| 5659 | `FindAttribute(self, textAttributeId: int, val, backward: bool)` | Call IUIAutomationTextRange::FindAttribute. textAttributeID: int, a value in class `TextAttributeId`. val: COM VARIANT according to textAttributeId? todo. |
| 5673 | `FindText(self, text: str, backward: bool, ignoreCase: bool)` | Call IUIAutomationTextRange::FindText. text: str, backward: bool, True if the last occurring text range should be returned instead of the first; otherwise False. |
| 5687 | `GetAttributeValue(self, textAttributeId: int)` | Call IUIAutomationTextRange::GetAttributeValue. textAttributeId: int, a value in class `TextAttributeId`. Return `ctypes.POINTER(comtypes.IUnknown)` or None, the value of the specified text attribute across the entire text range, todo. |
| 5696 | `GetBoundingRectangles(self)` | Call IUIAutomationTextRange::GetBoundingRectangles. textAttributeId: int, a value in class `TextAttributeId`. Return List[Rect], a list of `Rect`. |
| 5715 | `GetChildren(self)` | Call IUIAutomationTextRange::GetChildren. textAttributeId: int, a value in class `TextAttributeId`. Return List[Control], a list of `Control` subclasses, embedded objects that fall within the text range.. |
| 5733 | `GetEnclosingControl(self)` | Call IUIAutomationTextRange::GetEnclosingElement. Return `Control` subclass, the innermost UI Automation element that encloses the text range. |
| 5741 | `GetText(self, maxLength: int=-1)` | Call IUIAutomationTextRange::GetText. maxLength: int, the maximum length of the string to return, or -1 if no limit is required. Return str, the plain text of the text range. |
| 5750 | `Move(self, unit: int, count: int, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationTextRange::Move. Move the text range forward or backward by the specified number of text units. unit: int, a value in class `TextUnit`. |
| 5766 | `MoveEndpointByRange(self, srcEndPoint: int, textRange: 'TextRange', targetEndPoint: int, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationTextRange::MoveEndpointByRange. Move one endpoint of the current text range to the specified endpoint of a second text range. srcEndPoint: int, a value in class `TextPatternRangeEndpoint`. |
| 5781 | `MoveEndpointByUnit(self, endPoint: int, unit: int, count: int, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationTextRange::MoveEndpointByUnit. Move one endpoint of the text range the specified number of text units within the document range. endPoint: int, a value in class `TextPatternRangeEndpoint`. |
| 5799 | `RemoveFromSelection(self, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationTextRange::RemoveFromSelection. Remove the text range from an existing collection of selected text in a text container that supports multiple, disjoint selections. waitTime: float. |
| 5811 | `ScrollIntoView(self, alignTop: bool=True, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationTextRange::ScrollIntoView. Cause the text control to scroll until the text range is visible in the viewport. alignTop: bool, True if the text control should be scrolled so that the text range is flush with the top of the viewport; |
| 5825 | `Select(self, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationTextRange::Select. Select the span of text that corresponds to this text range, and remove any previous selection. waitTime: float. |

### `TextChildPattern`  <sub>linha 5838</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5844 | `prop TextContainer` | Property TextContainer. Call IUIAutomationSelectionContainer::get_TextContainer. Return `Control` subclass, the nearest ancestor element that supports the Text control pattern. |
| 5854 | `prop TextRange` | Property TextRange. Call IUIAutomationSelectionContainer::get_TextRange. Return `TextRange`, a text range that encloses this child element. |

### `TextEditPattern`  <sub>linha 5864</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5869 | `GetActiveComposition(self)` | Call IUIAutomationTextEditPattern::GetActiveComposition. Return `TextRange` or None, the active composition. |
| 5880 | `GetConversionTarget(self)` | Call IUIAutomationTextEditPattern::GetConversionTarget. Return `TextRange` or None, the current conversion target range.. |

### `TextPattern`  <sub>linha 5892</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5898 | `prop DocumentRange` | Property DocumentRange. Call IUIAutomationTextPattern::get_DocumentRange. Return `TextRange`, a text range that encloses the main text of a document. |
| 5908 | `prop SupportedTextSelection` | Property SupportedTextSelection. Call IUIAutomationTextPattern::get_SupportedTextSelection. Return bool, specifies the type of text selection that is supported by the control. |
| 5917 | `GetSelection(self)` | Call IUIAutomationTextPattern::GetSelection. Return List[TextRange], a list of `TextRange`, represents the currently selected text in a text-based control. |
| 5932 | `GetVisibleRanges(self)` | Call IUIAutomationTextPattern::GetVisibleRanges. Return List[TextRange], a list of `TextRange`, disjoint text ranges from a text-based control where each text range represents a contiguous span of visible text. |
| 5948 | `RangeFromChild(self, child)` | Call IUIAutomationTextPattern::RangeFromChild. child: `Control` or its subclass. Return `TextRange` or None, a text range enclosing a child element such as an image, |
| 5961 | `RangeFromPoint(self, x: int, y: int)` | Call IUIAutomationTextPattern::RangeFromPoint. child: `Control` or its subclass. Return `TextRange` or None, the degenerate (empty) text range nearest to the specified screen coordinates. |

### `TextPattern2`  <sub>linha 5974</sub>


### `TogglePattern`  <sub>linha 5980</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 5986 | `prop ToggleState` | Property ToggleState. Call IUIAutomationTogglePattern::get_CurrentToggleState. Return int, a value in class `ToggleState`, the state of the control. |
| 5995 | `Toggle(self, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationTogglePattern::Toggle. Cycle through the toggle states of the control. waitTime: float. |
| 6007 | `SetToggleState(self, toggleState: int, waitTime: float=OPERATION_WAIT_TIME)` |  |

### `TransformPattern`  <sub>linha 6015</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 6021 | `prop CanMove` | Property CanMove. Call IUIAutomationTransformPattern::get_CurrentCanMove. Return bool, indicates whether the element can be moved. |
| 6031 | `prop CanResize` | Property CanResize. Call IUIAutomationTransformPattern::get_CurrentCanResize. Return bool, indicates whether the element can be resized. |
| 6041 | `prop CanRotate` | Property CanRotate. Call IUIAutomationTransformPattern::get_CurrentCanRotate. Return bool, indicates whether the element can be rotated. |
| 6050 | `Move(self, x: int, y: int, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationTransformPattern::Move. Move the UI Automation element. x: int. |
| 6064 | `Resize(self, width: int, height: int, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationTransformPattern::Resize. Resize the UI Automation element. width: int. |
| 6078 | `Rotate(self, degrees: int, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationTransformPattern::Rotate. Rotates the UI Automation element. degrees: int. |

### `TransformPattern2`  <sub>linha 6092</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 6098 | `prop CanZoom` | Property CanZoom. Call IUIAutomationTransformPattern2::get_CurrentCanZoom. Return bool, indicates whether the control supports zooming of its viewport. |
| 6108 | `prop ZoomLevel` | Property ZoomLevel. Call IUIAutomationTransformPattern2::get_CurrentZoomLevel. Return float, the zoom level of the control's viewport. |
| 6118 | `prop ZoomMaximum` | Property ZoomMaximum. Call IUIAutomationTransformPattern2::get_CurrentZoomMaximum. Return float, the maximum zoom level of the control's viewport. |
| 6128 | `prop ZoomMinimum` | Property ZoomMinimum. Call IUIAutomationTransformPattern2::get_CurrentZoomMinimum. Return float, the minimum zoom level of the control's viewport. |
| 6137 | `Zoom(self, zoomLevel: float, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationTransformPattern2::Zoom. Zoom the viewport of the control. zoomLevel: float for int. |
| 6150 | `ZoomByUnit(self, zoomUnit: int, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationTransformPattern2::ZoomByUnit. Zoom the viewport of the control by the specified unit. zoomUnit: int, a value in class `ZoomUnit`. |

### `ValuePattern`  <sub>linha 6164</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 6170 | `prop IsReadOnly` | Property IsReadOnly. Call IUIAutomationTransformPattern2::IUIAutomationValuePattern::get_CurrentIsReadOnly. Return bool, indicates whether the value of the element is read-only. |
| 6180 | `prop Value` | Property Value. Call IUIAutomationTransformPattern2::IUIAutomationValuePattern::get_CurrentValue. Return str, the value of the element. |
| 6189 | `SetValue(self, value: str, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationTransformPattern2::IUIAutomationValuePattern::SetValue. Set the value of the element. value: str. |

### `VirtualizedItemPattern`  <sub>linha 6203</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 6208 | `Realize(self, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationVirtualizedItemPattern::Realize. Create a full UI Automation element for a virtualized item. waitTime: float. |

### `WindowPattern`  <sub>linha 6221</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 6226 | `Close(self, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationWindowPattern::Close. Close the window. waitTime: float. |
| 6238 | `prop CanMaximize` | Property CanMaximize. Call IUIAutomationWindowPattern::get_CurrentCanMaximize. Return bool, indicates whether the window can be maximized. |
| 6248 | `prop CanMinimize` | Property CanMinimize. Call IUIAutomationWindowPattern::get_CurrentCanMinimize. Return bool, indicates whether the window can be minimized. |
| 6258 | `prop IsModal` | Property IsModal. Call IUIAutomationWindowPattern::get_CurrentIsModal. Return bool, indicates whether the window is modal. |
| 6268 | `prop IsTopmost` | Property IsTopmost. Call IUIAutomationWindowPattern::get_CurrentIsTopmost. Return bool, indicates whether the window is the topmost element in the z-order. |
| 6278 | `prop WindowInteractionState` | Property WindowInteractionState. Call IUIAutomationWindowPattern::get_CurrentWindowInteractionState. Return int, a value in class `WindowInteractionState`, |
| 6289 | `prop WindowVisualState` | Property WindowVisualState. Call IUIAutomationWindowPattern::get_CurrentWindowVisualState. Return int, a value in class `WindowVisualState`, |
| 6299 | `SetWindowVisualState(self, state: int, waitTime: float=OPERATION_WAIT_TIME)` | Call IUIAutomationWindowPattern::SetWindowVisualState. Minimize, maximize, or restore the window. state: int, a value in class `WindowVisualState`. |
| 6312 | `WaitForInputIdle(self, milliseconds: int)` | Call IUIAutomationWindowPattern::WaitForInputIdle. Cause the calling code to block for the specified time or until the associated process enters an idle state, whichever completes first. |

### `Control`  <sub>linha 6369</sub>

Atributos: `ValidKeys`

*(+ 40 métodos-fábrica `xxxControl(...)` que criam o controle filho tipado: ButtonControl, CalendarControl, CheckBoxControl, ComboBoxControl, CustomControl, DataGridControl, DataItemControl, DocumentControl, EditControl, GroupControl, HeaderControl, HeaderItemControl, HyperlinkControl, ImageControl, ListControl, ListItemControl, MenuControl, MenuBarControl, MenuItemControl, PaneControl, ProgressBarControl, RadioButtonControl, ScrollBarControl, SemanticZoomControl, SeparatorControl, SliderControl, SpinnerControl, SplitButtonControl, StatusBarControl, TabControl, TabItemControl, TableControl, TextControl, ThumbControl, TitleBarControl, ToolBarControl, ToolTipControl, TreeControl, TreeItemControl, WindowControl)*

| Linha | Membro | Docstring |
|---|---|---|
| 6372 | `__init__(self, searchFromControl: Optional['Control']=None, searchDepth: int=4294967295, searchInterval: float=SEARCH_INTERVAL, foundIndex: int=1, element=None, ControlType: Optional[int]=None, Name: Optional[str]=None, SubName: Optional[str]=None, RegexName: Optional[str]=None, ClassName: Optional[str]=None, AutomationId: Optional[str]=None, Depth: Optional[int]=None, Compare: Optional[Callable[[TreeNode], bool]]=None, **searchProperties)` | searchFromControl: `Control` or its subclass, if it is None, search from root control(Desktop). searchDepth: int, max search depth from searchFromControl. foundIndex: int, starts with 1, >= 1. |
| 6434 | `__str__(self)` |  |
| 6438 | `__repr__(self)` |  |
| 6442 | `__getitem__(self, pos: int)` |  |
| 6465 | `static CreateControlFromElement(element)` | Create a concreate `Control` from a com type `IUIAutomationElement`. element: `ctypes.POINTER(IUIAutomationElement)`. Return a subclass of `Control`, an instance of the control's real type. |
| 6480 | `static CreateControlFromControl(control: 'Control')` | Create a concreate `Control` from a control instance, copy it. control: `Control` or its subclass. Return a subclass of `Control`, an instance of the control's real type. |
| 6490 | `SetSearchFromControl(self, searchFromControl: 'Control')` | searchFromControl: `Control` or its subclass |
| 6494 | `SetSearchDepth(self, searchDepth: int)` |  |
| 6497 | `AddSearchProperties(self, **searchProperties)` | Add search properties using `dict.update`. searchProperties: dict, same as searchProperties in `Control.__init__`. |
| 6509 | `RemoveSearchProperties(self, **searchProperties)` | searchProperties: dict, same as searchProperties in `Control.__init__`. |
| 6518 | `GetSearchPropertiesStr(self)` |  |
| 6522 | `GetColorfulSearchPropertiesStr(self, keyColor='DarkGreen', valueColor='DarkCyan')` | keyColor, valueColor: str, color name in class ConsoleColor |
| 6563 | `prop AcceleratorKey` | Property AcceleratorKey. Call IUIAutomationElement::get_CurrentAcceleratorKey. |
| 6572 | `prop AccessKey` | Property AccessKey. Call IUIAutomationElement::get_CurrentAccessKey. |
| 6581 | `prop AriaProperties` | Property AriaProperties. Call IUIAutomationElement::get_CurrentAriaProperties. |
| 6590 | `prop AriaRole` | Property AriaRole. Call IUIAutomationElement::get_CurrentAriaRole. |
| 6599 | `prop AutomationId` | Property AutomationId. Call IUIAutomationElement::get_CurrentAutomationId. |
| 6608 | `prop BoundingRectangle` | Property BoundingRectangle. Call IUIAutomationElement::get_CurrentBoundingRectangle. Return `Rect`. |
| 6622 | `prop ClassName` | Property ClassName. Call IUIAutomationElement::get_CurrentClassName. |
| 6631 | `prop ControlType` | Property ControlType. Return int, a value in class `ControlType`. Call IUIAutomationElement::get_CurrentControlType. |
| 6645 | `prop Culture` | Property Culture. Call IUIAutomationElement::get_CurrentCulture. |
| 6662 | `prop FrameworkId` | Property FrameworkId. Call IUIAutomationElement::get_CurrentFrameworkId. Return str, such as Win32, WPF... |
| 6672 | `prop HasKeyboardFocus` | Property HasKeyboardFocus. Call IUIAutomationElement::get_CurrentHasKeyboardFocus. |
| 6681 | `prop HelpText` | Property HelpText. Call IUIAutomationElement::get_CurrentHelpText. |
| 6690 | `prop IsContentElement` | Property IsContentElement. Call IUIAutomationElement::get_CurrentIsContentElement. |
| 6699 | `prop IsControlElement` | Property IsControlElement. Call IUIAutomationElement::get_CurrentIsControlElement. |
| 6708 | `prop IsDataValidForForm` | Property IsDataValidForForm. Call IUIAutomationElement::get_CurrentIsDataValidForForm. |
| 6717 | `prop IsEnabled` | Property IsEnabled. Call IUIAutomationElement::get_CurrentIsEnabled. |
| 6726 | `prop IsKeyboardFocusable` | Property IsKeyboardFocusable. Call IUIAutomationElement::get_CurrentIsKeyboardFocusable. |
| 6735 | `prop IsOffscreen` | Property IsOffscreen. Call IUIAutomationElement::get_CurrentIsOffscreen. |
| 6744 | `prop IsPassword` | Property IsPassword. Call IUIAutomationElement::get_CurrentIsPassword. |
| 6753 | `prop IsRequiredForForm` | Property IsRequiredForForm. Call IUIAutomationElement::get_CurrentIsRequiredForForm. |
| 6762 | `prop ItemStatus` | Property ItemStatus. Call IUIAutomationElement::get_CurrentItemStatus. |
| 6771 | `prop ItemType` | Property ItemType. Call IUIAutomationElement::get_CurrentItemType. |
| 6784 | `prop LocalizedControlType` | Property LocalizedControlType. Call IUIAutomationElement::get_CurrentLocalizedControlType. |
| 6793 | `prop Name` | Property Name. Call IUIAutomationElement::get_CurrentName. |
| 6802 | `prop NativeWindowHandle` | Property NativeWindowHandle. Call IUIAutomationElement::get_CurrentNativeWindowHandle. |
| 6815 | `prop Orientation` | Property Orientation. Return int, a value in class `OrientationType`. Call IUIAutomationElement::get_CurrentOrientation. |
| 6825 | `prop ProcessId` | Property ProcessId. Call IUIAutomationElement::get_CurrentProcessId. |
| 6834 | `prop ProviderDescription` | Property ProviderDescription. Call IUIAutomationElement::get_CurrentProviderDescription. |
| 6853 | `GetClickablePoint(self)` | Call IUIAutomationElement::GetClickablePoint. Return Tuple[int, int, bool], three items tuple (x, y, gotClickable), such as (20, 10, True) |
| 6862 | `GetPattern(self, patternId: int)` | Call IUIAutomationElement::GetCurrentPattern. Get a new pattern by pattern id if it supports the pattern. patternId: int, a value in class `PatternId`. |
| 6878 | `GetPatternAs(self, patternId: int, riid)` | Call IUIAutomationElement::GetCurrentPatternAs. Get a new pattern by pattern id if it supports the pattern, todo. patternId: int, a value in class `PatternId`. |
| 6888 | `GetPropertyValue(self, propertyId: int)` | Call IUIAutomationElement::GetCurrentPropertyValue. propertyId: int, a value in class `PropertyId`. Return Any, corresponding type according to propertyId. |
| 6897 | `GetPropertyValueEx(self, propertyId: int, ignoreDefaultValue: int)` | Call IUIAutomationElement::GetCurrentPropertyValueEx. propertyId: int, a value in class `PropertyId`. ignoreDefaultValue: int, 0 or 1. |
| 6907 | `GetRuntimeId(self)` | Call IUIAutomationElement::GetRuntimeId. Return List[int], a list of int. |
| 6918 | `SetFocus(self)` | Call IUIAutomationElement::SetFocus. |
| 6929 | `prop Element` | Property Element. Return `ctypes.POINTER(IUIAutomationElement)`. |
| 6939 | `prop ControlTypeName` | Property ControlTypeName. |
| 6945 | `GetCachedPattern(self, patternId: int, cache: bool)` | Get a pattern by patternId. patternId: int, a value in class `PatternId`. Return a pattern if it supports the pattern else None. |
| 6967 | `GetLegacyIAccessiblePattern(self)` | Return `LegacyIAccessiblePattern` if it supports the pattern else None. |
| 6973 | `GetAncestorControl(self, condition: Callable[['Control', int], bool])` | Get an ancestor control that matches the condition. condition: Callable[[Control, int], bool], function(control: Control, depth: int) -> bool, depth starts with -1 and decreses when search goes up. |
| 6990 | `GetParentControl(self)` | Return `Control` subclass or None. |
| 6997 | `GetFirstChildControl(self)` | Return `Control` subclass or None. |
| 7004 | `GetLastChildControl(self)` | Return `Control` subclass or None. |
| 7011 | `GetNextSiblingControl(self)` | Return `Control` subclass or None. |
| 7018 | `GetPreviousSiblingControl(self)` | Return `Control` subclass or None. |
| 7025 | `GetSiblingControl(self, condition: Callable[['Control'], bool], forward: bool=True)` | Get a sibling control that matches the condition. forward: bool, if True, only search next siblings, if False, search pervious siblings first, then search next siblings. condition: Callable[[Control], bool], function(control: Control) -> bool. |
| 7050 | `GetChildren(self)` | Return List[Control], a list of `Control` subclasses. |
| 7061 | `_CompareFunction(self, control: 'Control', depth: int)` | Define how to search. control: `Control` or its subclass. depth: int, tree depth from searchFromControl. |
| 7098 | `Exists(self, maxSearchSeconds: float=5, searchIntervalSeconds: float=SEARCH_INTERVAL, printIfNotExist: bool=False)` | maxSearchSeconds: float searchIntervalSeconds: float Find control every searchIntervalSeconds seconds in maxSearchSeconds seconds. |
| 7150 | `Disappears(self, maxSearchSeconds: float=5, searchIntervalSeconds: float=SEARCH_INTERVAL, printIfNotDisappear: bool=False)` | maxSearchSeconds: float searchIntervalSeconds: float Check if control disappears every searchIntervalSeconds seconds in maxSearchSeconds seconds. |
| 7174 | `Refind(self, maxSearchSeconds: float=TIME_OUT_SECOND, searchIntervalSeconds: float=SEARCH_INTERVAL, raiseException: bool=True)` | Refind the control every searchIntervalSeconds seconds in maxSearchSeconds seconds. maxSearchSeconds: float. searchIntervalSeconds: float. |
| 7190 | `GetPosition(self, ratioX: float=0.5, ratioY: float=0.5)` | Gets the position of the center of the control. ratioX: float. ratioY: float. |
| 7206 | `MoveCursorToInnerPos(self, x: Optional[int]=None, y: Optional[int]=None, ratioX: float=0.5, ratioY: float=0.5, simulateMove: bool=True)` | Move cursor to control's internal position, default to center. x: int, if < 0, move to self.BoundingRectangle.right + x, if not None, ignore ratioX. y: int, if < 0, move to self.BoundingRectangle.bottom + y, if not None, ignore ratioY. |
| 7236 | `MoveCursorToMyCenter(self, simulateMove: bool=True)` | Move cursor to control's center. Return Tuple[int, int], two ints tuple (x, y), the cursor positon relative to screen(0, 0) after moving. |
| 7243 | `Click(self, x: Optional[int]=None, y: Optional[int]=None, ratioX: float=0.5, ratioY: float=0.5, simulateMove: bool=True, waitTime: float=OPERATION_WAIT_TIME)` | x: int, if < 0, click self.BoundingRectangle.right + x, if not None, ignore ratioX. y: int, if < 0, click self.BoundingRectangle.bottom + y, if not None, ignore ratioY. ratioX: float. |
| 7260 | `MiddleClick(self, x: Optional[int]=None, y: Optional[int]=None, ratioX: float=0.5, ratioY: float=0.5, simulateMove: bool=True, waitTime: float=OPERATION_WAIT_TIME)` | x: int, if < 0, middle click self.BoundingRectangle.right + x, if not None, ignore ratioX. y: int, if < 0, middle click self.BoundingRectangle.bottom + y, if not None, ignore ratioY. ratioX: float. |
| 7277 | `RightClick(self, x: Optional[int]=None, y: Optional[int]=None, ratioX: float=0.5, ratioY: float=0.5, simulateMove: bool=True, waitTime: float=OPERATION_WAIT_TIME)` | x: int, if < 0, right click self.BoundingRectangle.right + x, if not None, ignore ratioX. y: int, if < 0, right click self.BoundingRectangle.bottom + y, if not None, ignore ratioY. ratioX: float. |
| 7294 | `DoubleClick(self, x: Optional[int]=None, y: Optional[int]=None, ratioX: float=0.5, ratioY: float=0.5, simulateMove: bool=True, waitTime: float=OPERATION_WAIT_TIME)` | x: int, if < 0, right click self.BoundingRectangle.right + x, if not None, ignore ratioX. y: int, if < 0, right click self.BoundingRectangle.bottom + y, if not None, ignore ratioY. ratioX: float. |
| 7311 | `DragDrop(self, x1: int, y1: int, x2: int, y2: int, moveSpeed: float=1, waitTime: float=OPERATION_WAIT_TIME)` |  |
| 7323 | `RightDragDrop(self, x1: int, y1: int, x2: int, y2: int, moveSpeed: float=1, waitTime: float=OPERATION_WAIT_TIME)` |  |
| 7335 | `WheelDown(self, x: Optional[int]=None, y: Optional[int]=None, ratioX: float=0.5, ratioY: float=0.5, wheelTimes: int=1, interval: float=0.05, waitTime: float=OPERATION_WAIT_TIME)` | Make control have focus first, move cursor to the specified position and mouse wheel down. x: int, if < 0, move x cursor to self.BoundingRectangle.right + x, if not None, ignore ratioX. y: int, if < 0, move y cursor to self.BoundingRectangle.bottom + y, if not |
| 7352 | `WheelUp(self, x: Optional[int]=None, y: Optional[int]=None, ratioX: float=0.5, ratioY: float=0.5, wheelTimes: int=1, interval: float=0.05, waitTime: float=OPERATION_WAIT_TIME)` | Make control have focus first, move cursor to the specified position and mouse wheel up. x: int, if < 0, move x cursor to self.BoundingRectangle.right + x, if not None, ignore ratioX. y: int, if < 0, move y cursor to self.BoundingRectangle.bottom + y, if not N |
| 7369 | `ShowWindow(self, cmdShow: int, waitTime: float=OPERATION_WAIT_TIME)` | Get a native handle from self or ancestors until valid and call native `ShowWindow` with cmdShow. cmdShow: int, a value in in class `SW`. waitTime: float. |
| 7392 | `Show(self, waitTime: float=OPERATION_WAIT_TIME)` | Call native `ShowWindow(SW.Show)`. Return bool, True if succeed otherwise False and None if the handle could not be gotten. |
| 7399 | `Hide(self, waitTime: float=OPERATION_WAIT_TIME)` | Call native `ShowWindow(SW.Hide)`. waitTime: float Return bool, True if succeed otherwise False and None if the handle could not be gotten. |
| 7407 | `MoveWindow(self, x: int, y: int, width: int, height: int, repaint: bool=True)` | Call native MoveWindow if control has a valid native handle. x: int. y: int. |
| 7422 | `GetWindowText(self)` | Call native GetWindowText if control has a valid native handle. |
| 7431 | `SetWindowText(self, text: str)` | Call native SetWindowText if control has a valid native handle. |
| 7440 | `SendKey(self, key: int, waitTime: float=OPERATION_WAIT_TIME)` | Make control have focus first and type a key. `self.SetFocus` may not work for some controls, you may need to click it to make it have focus. key: int, a key code value in class Keys. |
| 7450 | `SendKeys(self, text: str, interval: float=0.01, waitTime: float=OPERATION_WAIT_TIME, charMode: bool=True)` | Make control have focus first and type keys. `self.SetFocus` may not work for some controls, you may need to click it to make it have focus. text: str, keys to type, see the docstring of `SendKeys`. |
| 7462 | `GetPixelColor(self, x: int, y: int)` | Call native `GetPixelColor` if control has a valid native handle. Use `self.ToBitmap` if control doesn't have a valid native handle or you get many pixels. x: int, internal x position. |
| 7478 | `ToBitmap(self, x: int=0, y: int=0, width: int=0, height: int=0, captureCursor: bool=False)` | Capture control to a `Bitmap` object. x, y: int, the point in control's internal position(from 0,0). width, height: int, image's width and height from x, y, use 0 for entire area. |
| 7488 | `CaptureToImage(self, savePath: str, x: int=0, y: int=0, width: int=0, height: int=0, captureCursor: bool=False)` | Capture control to a image file. savePath: str, should end with .bmp, .jpg, .jpeg, .png, .gif, .tif, .tiff. x, y: int, the point in control's internal position(from 0,0). |
| 7504 | `IsTopLevel(self)` | Determine whether current control is top level. |
| 7511 | `GetTopLevelControl(self)` | Get the top level control which current control lays. If current control is top level, return self. If current control is root control, return None. |
| 7541 | `Control(self, searchDepth=4294967295, searchInterval=SEARCH_INTERVAL, foundIndex=1, element=0, Name: Optional[str]=None, SubName: Optional[str]=None, RegexName: Optional[str]=None, ClassName: Optional[str]=None, AutomationId: Optional[str]=None, Depth: Optional[int]=None, Compare: Optional[Callable[[TreeNode], bool]]=None, **searchProperties)` |  |

### `AppBarControl`(Control)  <sub>linha 8362</sub>


### `ButtonControl`(Control)  <sub>linha 8388</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 8413 | `GetExpandCollapsePattern(self)` | Return `ExpandCollapsePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 8419 | `GetInvokePattern(self)` | Return `InvokePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 8425 | `GetTogglePattern(self)` | Return `TogglePattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `CalendarControl`(Control)  <sub>linha 8432</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 8457 | `GetGridPattern(self)` | Return `GridPattern` if it supports the pattern else None(Must support according to MSDN). |
| 8463 | `GetTablePattern(self)` | Return `TablePattern` if it supports the pattern else None(Must support according to MSDN). |
| 8469 | `GetScrollPattern(self)` | Return `ScrollPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 8475 | `GetSelectionPattern(self)` | Return `SelectionPattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `CheckBoxControl`(Control)  <sub>linha 8482</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 8507 | `GetTogglePattern(self)` | Return `TogglePattern` if it supports the pattern else None(Must support according to MSDN). |
| 8513 | `SetChecked(self, checked: bool)` | Return True if set successfully |

### `ComboBoxControl`(Control)  <sub>linha 8521</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 8546 | `GetExpandCollapsePattern(self)` | Return `ExpandCollapsePattern` if it supports the pattern else None(Must support according to MSDN). |
| 8552 | `GetSelectionPattern(self)` | Return `SelectionPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 8558 | `GetValuePattern(self)` | Return `ValuePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 8564 | `Select(self, itemName: str='', condition: Optional[Callable[[str], bool]]=None, simulateMove: bool=True, waitTime: float=OPERATION_WAIT_TIME)` | Show combobox's popup menu and select a item by name. itemName: str. condition: Callable[[str], bool], function(comboBoxItemName: str) -> bool, if condition is valid, ignore itemName. |

### `CustomControl`(Control)  <sub>linha 8615</sub>


### `DataGridControl`(Control)  <sub>linha 8641</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 8666 | `GetGridPattern(self)` | Return `GridPattern` if it supports the pattern else None(Must support according to MSDN). |
| 8672 | `GetScrollPattern(self)` | Return `ScrollPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 8678 | `GetSelectionPattern(self)` | Return `SelectionPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 8684 | `GetTablePattern(self)` | Return `TablePattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `DataItemControl`(Control)  <sub>linha 8691</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 8716 | `GetSelectionItemPattern(self)` | Return `SelectionItemPattern` if it supports the pattern else None(Must support according to MSDN). |
| 8722 | `GetExpandCollapsePattern(self)` | Return `ExpandCollapsePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 8728 | `GetGridItemPattern(self)` | Return `GridItemPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 8734 | `GetScrollItemPattern(self)` | Return `ScrollItemPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 8740 | `GetTableItemPattern(self)` | Return `TableItemPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 8746 | `GetTogglePattern(self)` | Return `TogglePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 8752 | `GetValuePattern(self)` | Return `ValuePattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `DocumentControl`(Control)  <sub>linha 8759</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 8784 | `GetTextPattern(self)` | Return `TextPattern` if it supports the pattern else None(Must support according to MSDN). |
| 8790 | `GetScrollPattern(self)` | Return `ScrollPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 8796 | `GetValuePattern(self)` | Return `ValuePattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `EditControl`(Control)  <sub>linha 8803</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 8828 | `GetRangeValuePattern(self)` | Return `RangeValuePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 8834 | `GetTextPattern(self)` | Return `TextPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 8840 | `GetValuePattern(self)` | Return `ValuePattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `GroupControl`(Control)  <sub>linha 8847</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 8872 | `GetExpandCollapsePattern(self)` | Return `ExpandCollapsePattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `HeaderControl`(Control)  <sub>linha 8879</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 8904 | `GetTransformPattern(self)` | Return `TransformPattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `HeaderItemControl`(Control)  <sub>linha 8911</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 8936 | `GetInvokePattern(self)` | Return `InvokePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 8942 | `GetTransformPattern(self)` | Return `TransformPattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `HyperlinkControl`(Control)  <sub>linha 8949</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 8974 | `GetInvokePattern(self)` | Return `InvokePattern` if it supports the pattern else None(Must support according to MSDN). |
| 8980 | `GetValuePattern(self)` | Return `ValuePattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `ImageControl`(Control)  <sub>linha 8987</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9012 | `GetGridItemPattern(self)` | Return `GridItemPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9018 | `GetTableItemPattern(self)` | Return `TableItemPattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `ListControl`(Control)  <sub>linha 9025</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9050 | `GetGridPattern(self)` | Return `GridPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9056 | `GetMultipleViewPattern(self)` | Return `MultipleViewPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9062 | `GetScrollPattern(self)` | Return `ScrollPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9068 | `GetSelectionPattern(self)` | Return `SelectionPattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `ListItemControl`(Control)  <sub>linha 9075</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9100 | `GetSelectionItemPattern(self)` | Return `SelectionItemPattern` if it supports the pattern else None(Must support according to MSDN). |
| 9106 | `GetExpandCollapsePattern(self)` | Return `ExpandCollapsePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9112 | `GetGridItemPattern(self)` | Return `GridItemPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9118 | `GetInvokePattern(self)` | Return `InvokePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9124 | `GetScrollItemPattern(self)` | Return `ScrollItemPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9130 | `GetTogglePattern(self)` | Return `TogglePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9136 | `GetValuePattern(self)` | Return `ValuePattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `MenuControl`(Control)  <sub>linha 9143</sub>


### `MenuBarControl`(Control)  <sub>linha 9169</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9194 | `GetDockPattern(self)` | Return `DockPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9200 | `GetExpandCollapsePattern(self)` | Return `ExpandCollapsePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9206 | `GetTransformPattern(self)` | Return `TransformPattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `MenuItemControl`(Control)  <sub>linha 9213</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9238 | `GetExpandCollapsePattern(self)` | Return `ExpandCollapsePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9244 | `GetInvokePattern(self)` | Return `InvokePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9250 | `GetSelectionItemPattern(self)` | Return `SelectionItemPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9256 | `GetTogglePattern(self)` | Return `TogglePattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `TopLevel`  <sub>linha 9263</sub>

Class TopLevel

| Linha | Membro | Docstring |
|---|---|---|
| 9266 | `SetTopmost(self, isTopmost: bool=True, waitTime: float=OPERATION_WAIT_TIME)` | Set top level window topmost. isTopmost: bool. waitTime: float. |
| 9278 | `IsTopmost(self)` |  |
| 9284 | `SwitchToThisWindow(self, waitTime: float=OPERATION_WAIT_TIME)` |  |
| 9289 | `Maximize(self, waitTime: float=OPERATION_WAIT_TIME)` | Set top level window maximize. |
| 9297 | `IsMaximize(self)` |  |
| 9302 | `Minimize(self, waitTime: float=OPERATION_WAIT_TIME)` |  |
| 9307 | `IsMinimize(self)` |  |
| 9312 | `Restore(self, waitTime: float=OPERATION_WAIT_TIME)` | Restore window to normal state. Similar to SwitchToThisWindow. |
| 9321 | `MoveToCenter(self)` | Move window to screen center. |
| 9336 | `SetActive(self, waitTime: float=OPERATION_WAIT_TIME)` | Set top level window active. |

### `PaneControl`(Control, TopLevel)  <sub>linha 9350</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9375 | `GetDockPattern(self)` | Return `DockPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9381 | `GetScrollPattern(self)` | Return `ScrollPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9387 | `GetTransformPattern(self)` | Return `TransformPattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `ProgressBarControl`(Control)  <sub>linha 9394</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9419 | `GetRangeValuePattern(self)` | Return `RangeValuePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9425 | `GetValuePattern(self)` | Return `ValuePattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `RadioButtonControl`(Control)  <sub>linha 9432</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9457 | `GetSelectionItemPattern(self)` | Return `SelectionItemPattern` if it supports the pattern else None(Must support according to MSDN). |

### `ScrollBarControl`(Control)  <sub>linha 9464</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9489 | `GetRangeValuePattern(self)` | Return `RangeValuePattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `SemanticZoomControl`(Control)  <sub>linha 9496</sub>


### `SeparatorControl`(Control)  <sub>linha 9522</sub>


### `SliderControl`(Control)  <sub>linha 9548</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9573 | `GetRangeValuePattern(self)` | Return `RangeValuePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9579 | `GetSelectionPattern(self)` | Return `SelectionPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9585 | `GetValuePattern(self)` | Return `ValuePattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `SpinnerControl`(Control)  <sub>linha 9592</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9617 | `GetRangeValuePattern(self)` | Return `RangeValuePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9623 | `GetSelectionPattern(self)` | Return `SelectionPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9629 | `GetValuePattern(self)` | Return `ValuePattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `SplitButtonControl`(Control)  <sub>linha 9636</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9661 | `GetExpandCollapsePattern(self)` | Return `ExpandCollapsePattern` if it supports the pattern else None(Must support according to MSDN). |
| 9667 | `GetInvokePattern(self)` | Return `InvokePattern` if it supports the pattern else None(Must support according to MSDN). |

### `StatusBarControl`(Control)  <sub>linha 9674</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9699 | `GetGridPattern(self)` | Return `GridPattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `TabControl`(Control)  <sub>linha 9706</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9731 | `GetSelectionPattern(self)` | Return `SelectionPattern` if it supports the pattern else None(Must support according to MSDN). |
| 9737 | `GetScrollPattern(self)` | Return `ScrollPattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `TabItemControl`(Control)  <sub>linha 9744</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9769 | `GetSelectionItemPattern(self)` | Return `SelectionItemPattern` if it supports the pattern else None(Must support according to MSDN). |

### `TableControl`(Control)  <sub>linha 9776</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9801 | `GetGridPattern(self)` | Return `GridPattern` if it supports the pattern else None(Must support according to MSDN). |
| 9807 | `GetGridItemPattern(self)` | Return `GridItemPattern` if it supports the pattern else None(Must support according to MSDN). |
| 9813 | `GetTablePattern(self)` | Return `TablePattern` if it supports the pattern else None(Must support according to MSDN). |
| 9819 | `GetTableItemPattern(self)` | Return `TableItemPattern` if it supports the pattern else None(Must support according to MSDN). |
| 9825 | `GetTableItemsValue(self, row: int=-1, column: int=-1)` | Get the value of a table row: int. Position of the row in the table column: int. Position of the column in the table |

### `TextControl`(Control)  <sub>linha 9844</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9869 | `GetGridItemPattern(self)` | Return `GridItemPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9875 | `GetTableItemPattern(self)` | Return `TableItemPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9881 | `GetTextPattern(self)` | Return `TextPattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `ThumbControl`(Control)  <sub>linha 9888</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9913 | `GetTransformPattern(self)` | Return `TransformPattern` if it supports the pattern else None(Must support according to MSDN). |

### `TitleBarControl`(Control)  <sub>linha 9920</sub>


### `ToolBarControl`(Control)  <sub>linha 9946</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 9971 | `GetDockPattern(self)` | Return `DockPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9977 | `GetExpandCollapsePattern(self)` | Return `ExpandCollapsePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 9983 | `GetTransformPattern(self)` | Return `TransformPattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `ToolTipControl`(Control)  <sub>linha 9990</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 10015 | `GetTextPattern(self)` | Return `TextPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 10021 | `GetWindowPattern(self)` | Return `WindowPattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `TreeControl`(Control)  <sub>linha 10028</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 10053 | `GetScrollPattern(self)` | Return `ScrollPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 10059 | `GetSelectionPattern(self)` | Return `SelectionPattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `TreeItemControl`(Control)  <sub>linha 10066</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 10091 | `GetExpandCollapsePattern(self)` | Return `ExpandCollapsePattern` if it supports the pattern else None(Must support according to MSDN). |
| 10097 | `GetInvokePattern(self)` | Return `InvokePattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 10103 | `GetScrollItemPattern(self)` | Return `ScrollItemPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 10109 | `GetSelectionItemPattern(self)` | Return `SelectionItemPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 10115 | `GetTogglePattern(self)` | Return `TogglePattern` if it supports the pattern else None(Conditional support according to MSDN). |

### `WindowControl`(Control, TopLevel)  <sub>linha 10122</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 10149 | `GetTransformPattern(self)` | Return `TransformPattern` if it supports the pattern else None(Must support according to MSDN). |
| 10155 | `GetWindowPattern(self)` | Return `WindowPattern` if it supports the pattern else None(Must support according to MSDN). |
| 10161 | `GetDockPattern(self)` | Return `DockPattern` if it supports the pattern else None(Conditional support according to MSDN). |
| 10167 | `MetroClose(self, waitTime: float=OPERATION_WAIT_TIME)` | Only work on Windows 8/8.1, if current window is Metro UI. waitTime: float. |

### `UIAutomationInitializerInThread`  <sub>linha 10225</sub>

| Linha | Membro | Docstring |
|---|---|---|
| 10234 | `__del__(self)` |  |
| 10237 | `__enter__(self)` |  |
| 10240 | `__exit__(self, exceptionType, exceptionValue, exceptionTraceback)` |  |
| 10243 | `Uninitialize(self)` |  |