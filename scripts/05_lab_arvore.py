import uiautomation as auto
w = auto.WindowControl(searchDepth=1, Name="UIA-LAB")
w.Refind()
n=0
for c, d in auto.WalkControl(w, True, 4):
    n+=1
    pats=[nm.replace("Pattern","") for pid,nm in auto.PatternIdNames.items() if c.GetPattern(pid)]
    print("  "*d + f"{c.ControlTypeName[:-7]} id={c.AutomationId!r} name={c.Name[:28]!r} cls={c.ClassName.split('.')[-1][:22]!r} {pats}")
print("total", n)
