import tkinter as tk
from interface.gui import Gui

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Szyfrator')
    app = Gui(root)
    app.mainloop()
    pass