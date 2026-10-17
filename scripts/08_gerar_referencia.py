"""Gera docs/10-referencia-api-completa.md a partir do inventário AST (todas as classes/funções/métodos)."""
import json, pathlib, textwrap
d = json.load(open("dados/inventario.json", encoding="utf-8"))
L = ["# Referência completa da API (gerada do código-fonte)\n",
     "> Gerada automaticamente por `scripts/08_gerar_referencia.py` a partir da AST de `uiautomation/uiautomation.py` (v2.0.29). "
     "Cobre **todas** as funções, classes, métodos e propriedades. O número é a linha no arquivo.\n",
     f"Totais: **{len(d['classes'])} classes**, **{sum(len(c['methods']) for c in d['classes'])} métodos/propriedades**, **{len(d['functions'])} funções de módulo**.\n"]
def first(doc):
    if not doc: return ""
    lines=[l.strip() for l in doc.strip().splitlines() if l.strip() and not l.strip().startswith("Refer ")]
    return " ".join(lines[:3])[:260]
L.append("\n## Funções de módulo\n")
L.append("| Linha | Função | Descrição (docstring) |\n|---|---|---|")
for f in d["functions"]:
    L.append(f"| {f['line']} | `{f['name']}({f['sig']})` | {first(f['doc']).replace('|','\|')} |")
skip_factory = set("AppBarControl ButtonControl CalendarControl CheckBoxControl ComboBoxControl CustomControl DataGridControl DataItemControl DocumentControl EditControl GroupControl HeaderControl HeaderItemControl HyperlinkControl ImageControl ListControl ListItemControl MenuControl MenuBarControl MenuItemControl PaneControl ProgressBarControl RadioButtonControl ScrollBarControl SemanticZoomControl SeparatorControl SliderControl SpinnerControl SplitButtonControl StatusBarControl TabControl TabItemControl TableControl TextControl ThumbControl TitleBarControl ToolBarControl ToolTipControl TreeControl TreeItemControl WindowControl".split())
L.append("\n## Classes\n")
for c in d["classes"]:
    bases = f"({', '.join(c['bases'])})" if c["bases"] else ""
    L.append(f"\n### `{c['name']}`{bases}  <sub>linha {c['line']}</sub>\n")
    if c["doc"]: L.append(textwrap.shorten(c["doc"].replace("\n"," "),300)+"\n")
    if c["attrs"]:
        L.append(f"Atributos de classe: {len(c['attrs'])} (veja `02-constantes-e-enums.md`)\n" if c["name"] in ("ControlType","PatternId","PropertyId","Keys","AccessibleRole","TextAttributeId") else
                 "Atributos: " + ", ".join(f"`{n}`" for n,_ in c['attrs'][:60]) + (" …" if len(c['attrs'])>60 else "") + "\n")
    ms=[m for m in c["methods"] if m["name"]!="__init__" or c["name"] in ("Control",)]
    if c["name"]=="Control":
        fac=[m for m in ms if m["name"] in skip_factory]
        ms=[m for m in ms if m["name"] not in skip_factory]
        L.append(f"*(+ {len(fac)} métodos-fábrica `xxxControl(...)` que criam o controle filho tipado: {', '.join(m['name'] for m in fac)})*\n")
    if ms:
        L.append("| Linha | Membro | Docstring |\n|---|---|---|")
        for m in ms:
            kind = "prop " if any("property" in x for x in m["deco"]) else ("static " if any("staticmethod" in x for x in m["deco"]) else "")
            sig = "" if kind=="prop " else f"({m['sig']})"
            L.append(f"| {m['line']} | `{kind}{m['name']}{sig}` | {first(m['doc']).replace('|','\|')} |")
pathlib.Path("docs/10-referencia-api-completa.md").write_text("\n".join(L), encoding="utf-8")
print("ok", len(L), "linhas")
