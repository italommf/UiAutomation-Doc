import uiautomation as auto, time
def lab():
    w = auto.WindowControl(searchDepth=1, Name="UIA-LAB"); w.Refind(5); return w
def t(label, fn, show=240):
    try:
        r = fn(); print(f"[OK ] {label} -> {repr(r)[:show]}"); return r
    except Exception as e:
        print(f"[ERR] {label} -> {type(e).__name__}: {str(e)[:160]}")
