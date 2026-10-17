"""Despeja todas as constantes/enums/estruturas da lib em dados/constantes.md"""
import uiautomation as auto, inspect, ctypes
from uiautomation import uiautomation as u
out=[]
enums=[n for n,c in inspect.getmembers(u, inspect.isclass) if c.__module__==u.__name__ and not inspect.getmembers(c, inspect.isfunction) and n not in ('Keys',) and not issubclass(c,(ctypes.Structure,ctypes.Union))]
for n in enums:
    c=getattr(u,n)
    items=[(k,v) for k,v in vars(c).items() if not k.startswith('_')]
    if not items: continue
    out.append(f"\n### {n} ({len(items)})\n")
    for k,v in items:
        out.append(f"- `{k}` = `{v!r}`" + (f" (0x{v:X})" if isinstance(v,int) and v>9 else ""))
Keys=[(k,v) for k,v in vars(u.Keys).items() if not k.startswith('_')]
out.append(f"\n### Keys ({len(Keys)})\n")
out.append(", ".join(f"`{k}`={v}" for k,v in Keys))
out.append(f"\n### SpecialKeyNames ({len(u.SpecialKeyNames)})\n"+", ".join(f"`{{{k}}}`" for k in u.SpecialKeyNames))
out.append(f"\n### CharacterCodes ({len(u.CharacterCodes)})\n"+" ".join(f"`{k}`" for k in u.CharacterCodes))
out.append("\n### Globais configuráveis\n")
for k in "METRO_WINDOW_CLASS_NAME SEARCH_INTERVAL MAX_MOVE_SECOND TIME_OUT_SECOND OPERATION_WAIT_TIME MAX_PATH DEBUG_SEARCH_TIME DEBUG_EXIST_DISAPPEAR S_OK IsPy38OrHigher IsNT6orHigher CurrentProcessIs64Bit".split():
    out.append(f"- `{k}` = `{getattr(u,k)!r}`")
out.append("\n### Structs ctypes\n")
for n,c in inspect.getmembers(u, inspect.isclass):
    if c.__module__==u.__name__ and issubclass(c,(ctypes.Structure,ctypes.Union)):
        out.append(f"- `{n}`: {[(f[0],f[1].__name__) for f in c._fields_]}")
open("dados/constantes.md","w",encoding="utf-8").write("\n".join(out))
print(len(out),"blocos;", len(enums),"enums")
print("ControlTypeNames",len(u.ControlTypeNames),"PatternIdNames",len(u.PatternIdNames),"PropertyIdNames",len(u.PropertyIdNames))
print("__all__" , hasattr(u,"__all__"), "exportados via import *:", len([n for n in dir(auto) if not n.startswith('_')]))
