"""Inventário estático (AST) de uiautomation.py: classes, métodos, funções, constantes."""
import ast, sys, json, pathlib, uiautomation
src_path = pathlib.Path(uiautomation.__file__).parent / "uiautomation.py"
tree = ast.parse(src_path.read_text(encoding="utf-8"))
out = {"classes": [], "functions": [], "constants": [], "other": []}
def sig(fn):
    return ast.unparse(fn.args)
for n in tree.body:
    if isinstance(n, ast.ClassDef):
        c = {"name": n.name, "line": n.lineno, "bases": [ast.unparse(b) for b in n.bases],
             "doc": ast.get_docstring(n), "methods": [], "attrs": []}
        for m in n.body:
            if isinstance(m, (ast.FunctionDef, ast.AsyncFunctionDef)):
                deco = [ast.unparse(d) for d in m.decorator_list]
                c["methods"].append({"name": m.name, "line": m.lineno, "sig": sig(m), "deco": deco, "doc": ast.get_docstring(m), "end": m.end_lineno})
            elif isinstance(m, ast.Assign):
                for t in m.targets:
                    if isinstance(t, ast.Name):
                        c["attrs"].append((t.id, ast.unparse(m.value)[:80]))
        out["classes"].append(c)
    elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
        out["functions"].append({"name": n.name, "line": n.lineno, "sig": sig(n), "doc": ast.get_docstring(n), "end": n.end_lineno})
    elif isinstance(n, ast.Assign):
        for t in n.targets:
            if isinstance(t, ast.Name):
                out["constants"].append((t.id, n.lineno, ast.unparse(n.value)[:80]))
    else:
        out["other"].append((type(n).__name__, n.lineno))
pathlib.Path("dados").mkdir(exist_ok=True)
pathlib.Path("dados/inventario.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
print("classes", len(out["classes"]), "metodos", sum(len(c["methods"]) for c in out["classes"]))
print("funcoes", len(out["functions"]), "constantes", len(out["constants"]), "outros", len(out["other"]))
for c in out["classes"]:
    print(f'{c["line"]:5} {c["name"]}({", ".join(c["bases"])}) m={len(c["methods"])} a={len(c["attrs"])}')
