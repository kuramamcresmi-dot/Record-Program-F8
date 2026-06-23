"""
ShivaClips v2.0 - Clip Recorder
Entry point (.pyw = no CMD window)
"""
import sys, os, tkinter as tk
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.engine    import Engine
from ui.splash      import SplashScreen
from ui.main_window import MainWindow


def main():
    root = tk.Tk()
    root.withdraw()

    engine = Engine()

    def launch_app():
        root.destroy()
        app = MainWindow(engine)   # watcher yok
        app.mainloop()

    SplashScreen(root, on_done=launch_app)
    root.mainloop()


if __name__ == "__main__":
    main()
