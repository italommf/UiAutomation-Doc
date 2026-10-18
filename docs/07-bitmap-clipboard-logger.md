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
| `Clone()` | ⚠ 🧪 **QUEBRA**: `OSError: access violation` em 100% das chamadas (a DLL devolve ponteiro de 64 bits e o `restype` não foi definido). Use `Copy()`. |
| `Paste(x, y, bitmap)` / `PastePart(dstX,dstY,src,srcX,srcY,srcW,srcH)` | **modifica o original**; recorta o que sair dos limites |
| `Resize(w,h)` | novo bitmap |
| `Rotate(angle, backgroundColor=0xFFFFFFFF)` | horário, em torno do centro; tamanho do resultado pode mudar |
| `RotateWithSameSize(dx, dy, angle, bg)` | ⚠ 🧪 **QUEBRA** pelo mesmo motivo do `Clone` (`access violation`). Alternativa: `Rotate` + recorte com `Copy`/`Paste`. |
| `RotateFlip(RotateFlipType)` | giros de 90° e espelhamentos |
| `Close()` / `Release()` / `with Bitmap...` / `__del__` | **libera a memória nativa**; use `with` ou chame `Close()` |
| `GetRawFormat()`, `GetRawFormatStr()` | |

Cores: `GetPixelColor(x,y)` do módulo/`Control` usa **BGR** (GDI); `Bitmap` usa **ARGB**. Não misture.

## 7.3 Clipboard
Todas as funções usam um `threading.Lock` global e tentam abrir o clipboard por até 0,2 s.
| Função | Descrição |
|---|---|
| `GetClipboardFormats()` | `{id: nome}` dos formatos presentes 🧪 (ex.: `{13: 'CF_UNICODETEXT', 16: 'CF_LOCALE', 1: 'CF_TEXT', 7: 'CF_OEMTEXT'}` após `SetClipboardText`; `SetClipboard*` apaga o resto, inclusive formatos de outros apps) |
| `GetClipboardText()` / `SetClipboardText(text)` | `CF_UNICODETEXT`; `Get` devolve `''` se vazio/indisponível |
| `GetClipboardHtml()` / `SetClipboardHtml(html)` | formato "HTML Format" (monta cabeçalho `StartHTML/EndHTML/StartFragment/EndFragment` em UTF‑8) |
| `GetClipboardBitmap()` / `SetClipboardBitmap(bitmap)` | `CF_BITMAP` |
| `ClipboardFormat` | constantes `CF_*` + `CF_HTML` (registrado em runtime) |

⚠ 🧪 **Vazamento confirmado:** em `GetClipboardText`, `GetClipboardHtml` e `GetClipboardBitmap`, `CloseClipboard` só é chamado quando o formato existe. Se o clipboard não tiver aquele formato (ex.: só tem imagem e você chama `GetClipboardText()`), ele já foi aberto e nunca é fechado: **programas normais** (que abrem o clipboard com um *handle* de janela) ficam **bloqueados** (erro 5) até o seu Python terminar ou você chamar `ctypes.windll.user32.CloseClipboard()`. Chamadas normais (o formato existe) **não vazam**. Observação: dois processos que abrem com `NULL` convivem sem conflito, por isso só se nota o problema em apps "de janela". **Contorno testado:** `if 'CF_UNICODETEXT' in GetClipboardFormats().values():` antes de ler.
`SetClipboard*` sobrescreve o clipboard do usuário — **salve e restaure** se importar.

🧪 Outros achados do clipboard: (1) **emoji trunca**: `SetClipboardText('ok 😀 fim')` → `'ok 😀 fi'` (o tamanho usa `len(text)` em code points; falta 1 unidade UTF‑16 por caractere fora do BMP); (2) **`SetClipboardHtml` não grava `NUL` final** e não zera a memória: com a memória reaproveitada, `GetClipboardHtml` deu `UnicodeDecodeError`/lixo em 47 de 60 repetições (sem acento e em condições calmas funciona; os deslocamentos `StartFragment/EndFragment` são exatos em bytes UTF‑8 mesmo com acentos); (3) com o clipboard preso por outro processo, `SetClipboardText` tenta ~0,2 s e devolve `False`, `GetClipboardText` devolve `''` em ~0,2 s; (4) textos de 150 mil caracteres ida e volta ok; `SendKeys('{Ctrl}a{Ctrl}c')` e `{Ctrl}v` interagem corretamente com o clipboard; (5) `GetClipboardBitmap` devolve `MemoryBMP` e preserva cor e tamanho.

## 7.4 `Logger`
Saída colorida no console + arquivo (padrão `@AutomationLog.txt` no diretório atual, `a+`, UTF‑8).
| Método (todos `@staticmethod`) | Descrição |
|---|---|
| `Write(log, consoleColor, writeToFile=True, printToStdout=True, logFile=None, printTruncateLen=0)` | texto cru (corta com `...` se `printTruncateLen>0`) |
| `WriteLine` | com `\n` |
| `Log(log, ...)` / `LogColorfully`=`ColorfullyLog` | prefixa data/hora, **arquivo[linha] função ->** (descobre o chamador fora de `uiautomation.py` via `sys._getframe`) |
| `ColorfullyWrite(log, ...)` / `WriteColorfully`, `ColorfullyWriteLine` / `WriteLineColorfully` | aceita marcas `'Texto <Color=Green>verde</Color>'`; nomes em `Logger.ColorNames` (Black, DarkBlue…, White); **não aninha** | 🧪 Cor inexistente ou sem `</Color>` fica **literal**; aninhado não aninha: `<Color=Green>a <Color=Red>b</Color> c</Color>` imprime `a <Color=Red>b c</Color>`.
| `SetLogFile(file_or_path)` | `''` desliga o arquivo; fecha o anterior |
| `DeleteLog()` | apaga `Logger.FilePath` |
| `Logger.FilePath`, `Logger.FileObj`, `Logger.ColorNames` | |

Dicas: para silenciar o arquivo no início do script: `auto.Logger.SetLogFile('')`. As mensagens da própria lib ("Find Control Timeout", "Can not move cursor") passam por aqui. O flush do arquivo é feito a cada ≥2 s e no `atexit`.

Funções de log de árvore: `LogControl(control, depth, showAllName, showPid)` — imprime ControlType, ClassName, AutomationId, Rect, Name, Handle, Depth e valores de patterns (Value, Toggle, Selection, ExpandCollapse, Scroll, Grid, Text). **Chama `GetPattern` para os 34 ids em cada controle** (lento em árvores grandes). `EnumAndLogControl(control, maxDepth, showAllName, showPid, startDepth)`, `EnumAndLogControlAncestors(control, ...)`. ⚠ Escrevem no arquivo de log, incluindo textos dos controles. 🧪 Mede ~95 ms por controle (34 consultas de pattern) contra ~3 ms por controle do `WalkControl`.

## 7.5 `ProcessInfo`
Atributos: `pid, ppid, exeName, is64Bit, exePath, cmdLine`. `str()` não fecha o parêntese final (cosmético).

## Verificações (🧪) deste capítulo
- **`Bitmap`:** construção (preto transparente `0x00000000`), `Set/GetPixelColor`, `Clear` (inclusive parcial), `GetPixelColorsOfRect/Row/Column/Horizontally/Vertically/All/Rects` (devolvem `ctypes.Array` de `c_uint32`), `SetPixelColors*` (lista Python ou array), `Copy`, `Paste` (com recorte e coordenadas negativas) e `PastePart`, `Resize`/`Rotate`/`RotateFlip` (novo bitmap; original intacto; `Rotate(90)` troca largura/altura, `Rotate(45)` aumenta; `backgroundColor` preenche os cantos).
- **Arquivos:** `ToFile` em png/jpg/jpeg/bmp/gif/tif/tiff com o formato real conferido pelos primeiros bytes e `FromFile` devolvendo `PNG/JPEG/BMP/GIF/TIFF`; extensão desconhecida grava **PNG**; JPEG com `quality` maior gera arquivo maior; caminho inexistente → `False`/`None`; `ToBytes('BGRA')` em ordem B,G,R,A; `FromBytes` (BGRA e arquivo) e `AssertionError` com tamanho errado; formato desconhecido em `ToBytes` → PNG.
- **Integrações:** `ToNDArray` `(h,w,4)`; `FromNDArray` com 3 e 4 canais (alfa 0xFF/preservado) e `AssertionError` em 2D; `ToPILImage` (RGBA, cores certas) e `FromPILImage` (RGB/RGBA; `AssertionError` em modo `L`).
- **GIF/TIFF:** `GIF.ToGifFile` com atrasos (100/200/300 ms lidos de volta iguais), classe `GIF`, 3 quadros, iteração devolvendo `MemoryBMP`; sem `delays` → `TypeError`; `TIFF.ToTiffFile` multi-frame.
- **Ciclo de vida:** `Close()`/`Release()`/`with`/duplo `Close` seguros; `Width/Height` viram 0.
- **Captura:** `ToBitmap()` com o tamanho do controle e cor correta (`0xFFFF6347` no PictureBox "Tomato"); recortes `(x,y,w,h)`; `width/height < 0`; `CaptureToImage`; janela top‑level usa o retângulo DWM; `FromHandle`; `captureCursor=True`; elemento **sem HWND** (via ancestral); **janela por cima aparece no print** (não é a janela alvo); **janela minimizada sai preta** (bitmap 150×100 com o pixel central `0xFF000000`); controle de área zero captura o **pai**.
- **`Logger`/`Rect`:** `import` não cria `@AutomationLog.txt`; a 1ª mensagem cria no diretório atual; `SetLogFile('')` desliga; `SetLogFile(path)` com append; `DeleteLog`; formato de `Log` (`data hora.ms arquivo[linha] função -> msg`) e nome da função chamadora; `printTruncateLen`; `printToStdout=False`; `ResetConsoleColor` antes de `SetConsoleColor` → `AssertionError`; sem console `SetConsoleColor` devolve `False`; `Input`/`InputColorfully` leem do stdin; `LogControl` grava o `Name` no arquivo; todos os métodos de `Rect` (inclusive `intersect` negativo, `offset` que muda o próprio objeto, `==`/`hash`).
