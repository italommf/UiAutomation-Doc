# 07 — Bitmap, Clipboard, Logger, Rect, ProcessInfo

## 7.1 `Rect` (L1702)
Parecido com `RECT` do Win32, mas é uma classe Python.
`Rect(left, top, right, bottom)` · `width()` · `height()` · `xcenter()` · `ycenter()` · `isempty()` (largura OU altura zero) · `contains(x, y)` (**semi‑aberto**: `left <= x < right`) · `intersect(rect)` → novo `Rect` (pode vir com tamanho negativo se não se cruzam) · `offset(dx, dy)` (muda **no próprio objeto**) · `==` · `str` → `(l,t,r,b)[WxH]`, `repr` → `Rect(l,t,r,b)[WxH]`.
⚠ Define `__eq__` sem `__hash__` ⇒ `Rect` **não é hashable** (não serve de chave de dict/set) e `rect == None` levanta `AttributeError`.

## 7.2 `Bitmap` — wrapper do GDI+ via DLL nativa
Formato de pixel: `PixelFormat32bppARGB` → inteiro `0xAARRGGBB`, bytes na ordem **B G R A**.
Requer a DLL em `bin/` (VC++ 2015 Redistributable). Se a DLL não carregar, `Bitmap` não funciona (o resto da lib sim).

### Criação
| API | Descrição |
|---|---|
| `Bitmap(width, height)` | bitmap vazio, **transparente preto** (`0x00000000`) |
| `Bitmap.FromControl(control, x=0, y=0, width=0, height=0, captureCursor=False)` | captura um controle. `width/height<=0` → tamanho do controle + valor (ex.: `-10` = 10 px a menos). Se o controle tem retângulo zero, **sobe pelos pais** até um com área. Para janelas top‑level usa `DwmGetWindowExtendFrameBounds` (sem borda invisível). Captura **da tela** (pixels visíveis), não da janela em memória: janela coberta por outra sai com o que está por cima. |
| `Bitmap.FromHandle(hwnd, left, top, right, bottom, captureCursor)` | por HWND, coordenadas internas |
| `Bitmap.FromFile(path)` | qualquer formato do GDI+ (BMP, JPEG, PNG, GIF, TIFF, EMF, WMF, ICO) → subclasse correta |
| `Bitmap.FromBytes(data, format=None, width=None, height=None)` | bytes de arquivo de imagem, ou `format='BGRA'` + width + height para pixels crus (`len == w*h*4`) |
| `Bitmap.FromNDArray(arr)` | numpy BGR(3) ou BGRA(4) → `MemoryBMP` (precisa numpy) |
| `Bitmap.FromPILImage(img)` | PIL `RGB`/`RGBA` → `MemoryBMP` (usa numpy se houver, senão laço lento em Python) |
| `Control.ToBitmap(...)`, `Control.CaptureToImage(path, ...)` | atalhos |
| `GetClipboardBitmap()` | veja 7.3 |

Subclasses por formato (devolvidas por `_FromGdiplusBitmap`): `MemoryBMP, BMP, JPEG, PNG, EMF, WMF, ICON, EXIF, GIF, TIFF` (+ `MultiFrameBitmap` base de GIF/TIFF). `RawFormat`: Undefined=0, MemoryBMP=1, BMP=2, EMF=3, WMF=4, JPEG=5, PNG=6, GIF=7, TIFF=8, EXIF=9, Icon=10.

### Salvar / converter
| API | Descrição |
|---|---|
| `ToFile(path, *, quality=None)` | formato pela **extensão**: `.bmp .jpg .jpeg .gif .tif .tiff .png`; **extensão desconhecida → PNG** (o arquivo terá o nome errado mas conteúdo PNG). `quality` 1–100 só para JPEG (padrão 80). GIF/TIFF salvam só 1 frame. Retorna bool. |
| `ToBytes(format, *, quality=None)` | `'BGRA'` (pixels crus) ou `'png'/'jpg'/...` → `bytearray` (ou `None`) |
| `ToPILImage()` / `ToNDArray()` | PIL RGBA / numpy `(h, w, 4)` BGRA (compatível com OpenCV) |
| `GIF.ToGifFile(path, bitmaps, delays_ms)` | GIF animado; delays em ms e **>10 ms**. ⚠ `delays=None` (o default!) dá `TypeError` |
| `TIFF.ToTiffFile(path, bitmaps)` | TIFF multi-frame |
| `MultiFrameBitmap`: `GetFrameCount()`, `SelectActiveFrame(i)`, iterável (cada item é `Copy()` do frame); `GIF.GetFrameDelay(i)`/`GetFrameDelays()` em ms |

### Pixels
| API | Descrição |
|---|---|
| `Width`, `Height` (properties) | |
| `GetPixelColor(x,y)` / `SetPixelColor(x,y,argb)` | um pixel (lento em laço) |
| `GetPixelColorsOfRect(x,y,w,h)`, `GetPixelColorsOfRects([(x,y,w,h),...])`, `GetPixelColorsOfRow(y)`, `GetPixelColorsOfColumn(x)`, `GetPixelColorsHorizontally(x,y,count)`, `GetPixelColorsVertically(x,y,count)`, `GetAllPixelColors()` | devolvem `ctypes.Array` de `c_uint32` (rápido). `bytes(memoryview(arr))` para bytes |
| `SetPixelColorsOfRect(...)`, `SetPixelColorsHorizontally/Vertically`, `SetAllPixelColors` | aceitam sequência; **passe um `ctypes.c_uint32 * n`** para ser rápido |
| `Clear(color=0xFFFFFFFF, x, y, w, h)` | preenche (0 = até a borda) |
| `Copy(x,y,w,h)` | novo `MemoryBMP` (um frame) |
| `Clone()` | mantém formato e frames |
| `Paste(x, y, bitmap)` / `PastePart(dstX,dstY,src,srcX,srcY,srcW,srcH)` | **modifica o original**; recorta o que sair dos limites |
| `Resize(w,h)` | novo bitmap |
| `Rotate(angle, backgroundColor=0xFFFFFFFF)` | horário, em torno do centro; tamanho do resultado pode mudar |
| `RotateWithSameSize(dx, dy, angle, bg)` | gira em volta de (dx,dy) mantendo o tamanho |
| `RotateFlip(RotateFlipType)` | giros de 90° e espelhamentos |
| `Close()` / `Release()` / `with Bitmap...` / `__del__` | **libera a memória nativa**; use `with` ou chame `Close()` |
| `GetRawFormat()`, `GetRawFormatStr()` | |

Cores: `GetPixelColor(x,y)` do módulo/`Control` usa **BGR** (GDI); `Bitmap` usa **ARGB**. Não misture.

## 7.3 Clipboard
Todas as funções usam um `threading.Lock` global e tentam abrir o clipboard por até 0,2 s.
| Função | Descrição |
|---|---|
| `GetClipboardFormats()` | `{id: nome}` dos formatos presentes (testado: HTML Format, CF_UNICODETEXT, CF_TEXT… e formatos registrados por apps) |
| `GetClipboardText()` / `SetClipboardText(text)` | `CF_UNICODETEXT`; `Get` devolve `''` se vazio/indisponível |
| `GetClipboardHtml()` / `SetClipboardHtml(html)` | formato "HTML Format" (monta cabeçalho `StartHTML/EndHTML/StartFragment/EndFragment` em UTF‑8) |
| `GetClipboardBitmap()` / `SetClipboardBitmap(bitmap)` | `CF_BITMAP` |
| `ClipboardFormat` | constantes `CF_*` + `CF_HTML` (registrado em runtime) |

⚠ **Vazamento de handle:** em `GetClipboardText`, `GetClipboardHtml` e `GetClipboardBitmap`, `CloseClipboard` só é chamado quando o formato existe. Se o clipboard não tiver aquele formato (ex.: só tem imagem e você chama `GetClipboardText()`), o `OpenClipboard` já foi feito e nunca é fechado: o processo continua dono do clipboard e outros apps não conseguem usá-lo até o Python terminar (deduzido do código; não reproduzi para não mexer no seu clipboard). Contorno: antes de ler, confira `ClipboardFormat.CF_UNICODETEXT in GetClipboardFormats()`, ou chame `ctypes.windll.user32.CloseClipboard()` depois.
`SetClipboard*` sobrescreve o clipboard do usuário — **salve e restaure** se importar.

## 7.4 `Logger`
Saída colorida no console + arquivo (padrão `@AutomationLog.txt` no diretório atual, `a+`, UTF‑8).
| Método (todos `@staticmethod`) | Descrição |
|---|---|
| `Write(log, consoleColor, writeToFile=True, printToStdout=True, logFile=None, printTruncateLen=0)` | texto cru (corta com `...` se `printTruncateLen>0`) |
| `WriteLine` | com `\n` |
| `Log(log, ...)` / `LogColorfully`=`ColorfullyLog` | prefixa data/hora, **arquivo[linha] função ->** (descobre o chamador fora de `uiautomation.py` via `sys._getframe`) |
| `ColorfullyWrite(log, ...)` / `WriteColorfully`, `ColorfullyWriteLine` / `WriteLineColorfully` | aceita marcas `'Texto <Color=Green>verde</Color>'`; nomes em `Logger.ColorNames` (Black, DarkBlue…, White); **não aninha** |
| `SetLogFile(file_or_path)` | `''` desliga o arquivo; fecha o anterior |
| `DeleteLog()` | apaga `Logger.FilePath` |
| `Logger.FilePath`, `Logger.FileObj`, `Logger.ColorNames` | |

Dicas: para silenciar o arquivo no início do script: `auto.Logger.SetLogFile('')`. As mensagens da própria lib ("Find Control Timeout", "Can not move cursor") passam por aqui. O flush do arquivo é feito a cada ≥2 s e no `atexit`.

Funções de log de árvore: `LogControl(control, depth, showAllName, showPid)` — imprime ControlType, ClassName, AutomationId, Rect, Name, Handle, Depth e valores de patterns (Value, Toggle, Selection, ExpandCollapse, Scroll, Grid, Text). **Chama `GetPattern` para os 34 ids em cada controle** (lento em árvores grandes). `EnumAndLogControl(control, maxDepth, showAllName, showPid, startDepth)`, `EnumAndLogControlAncestors(control, ...)`. ⚠ Escrevem no arquivo de log, incluindo textos dos controles.

## 7.5 `ProcessInfo`
Atributos: `pid, ppid, exeName, is64Bit, exePath, cmdLine`. `str()` não fecha o parêntese final (cosmético).
