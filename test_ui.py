import sys, os, traceback
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
errors = []

def chk(name, fn):
    try:
        fn(); print(f"OK   {name}")
    except Exception as e:
        errors.append((name, e))
        print(f"ERR  {name}: {e}")
        traceback.print_exc()

chk("i18n",          lambda: __import__("i18n"))
chk("config",        lambda: __import__("config"))
chk("core.engine",   lambda: __import__("core.engine",      fromlist=["*"]))
chk("widgets",       lambda: __import__("ui.widgets",       fromlist=["*"]))
chk("overlay",       lambda: __import__("ui.overlay",       fromlist=["*"]))
chk("splash",        lambda: __import__("ui.splash",        fromlist=["*"]))
chk("tab_dashboard", lambda: __import__("ui.tab_dashboard", fromlist=["*"]))
chk("tab_clips",     lambda: __import__("ui.tab_clips",     fromlist=["*"]))
chk("tab_settings",  lambda: __import__("ui.tab_settings",  fromlist=["*"]))
chk("tab_about",     lambda: __import__("ui.tab_about",     fromlist=["*"]))
chk("main_window",   lambda: __import__("ui.main_window",   fromlist=["*"]))
chk("main.pyw",      lambda: __import__("ast") and compile(
    open("main.pyw", encoding="utf-8").read(), "main.pyw", "exec"))

# Widget runtime test
try:
    import tkinter as tk
    from config import THEME as T
    from ui.widgets import Card, ProgressBar, KeyBadge, StatCard, StatusDot, LogBox, Btn
    root = tk.Tk(); root.withdraw()
    f  = tk.Frame(root, bg=T["bg"])
    c  = Card(f)
    pb = ProgressBar(c, bg=T["card"])
    kb = KeyBadge(c, key="F8", bg=T["card"])
    sc = StatCard(f, "Test", color=T["green"])
    sd = StatusDot(f)
    lb = LogBox(f); lb.log("test", "ok")
    root.after(300, root.destroy); root.mainloop()
    print("OK   widget runtime")
except Exception as e:
    errors.append(("widgets_runtime", e))
    print(f"ERR  widgets_runtime: {e}"); traceback.print_exc()

# Tab sistemi — grid+tkraise testi
try:
    import tkinter as tk
    from config import THEME as T
    from ui.tab_dashboard import DashboardTab
    from ui.tab_clips     import ClipsTab
    from core.engine      import Engine

    root = tk.Tk(); root.withdraw()
    root.geometry("1200x780")
    area = tk.Frame(root, bg=T["bg"])
    area.pack(fill="both", expand=True)
    area.grid_rowconfigure(0, weight=1)
    area.grid_columnconfigure(0, weight=1)

    eng = Engine()
    d = DashboardTab(area, eng)
    c = ClipsTab(area)
    d.grid(row=0, column=0, sticky="nsew")
    c.grid(row=0, column=0, sticky="nsew")
    d.tkraise()   # dashboard öne çıksın

    root.after(300, root.destroy); root.mainloop()
    print("OK   tab grid+tkraise")
except Exception as e:
    errors.append(("tab_grid", e))
    print(f"ERR  tab_grid: {e}"); traceback.print_exc()

print()
if errors:
    print(f"FAILED: {len(errors)} error(s)")
    for n, e in errors: print(f"  - {n}: {e}")
    sys.exit(1)
else:
    print("ALL PASSED")
