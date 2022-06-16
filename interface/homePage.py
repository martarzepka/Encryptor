
import tkinter as tk


class HomePage(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        label = tk.Label(self, text="Witaj w Szyfratorze!!!", font=parent.title_font)
        label.pack(fill="x", pady=10)

        button1 = tk.Button(self, text="Zaloguj", command=lambda: parent.show_frame("Login"))
        button2 = tk.Button(self, text="Zarejestruj", command=lambda: parent.show_frame("Registration"))
        button1.pack(pady=5)
        button2.pack(pady=5)

    def refresh(self):
        self.parent.rememberme = False
        self.parent.parent["menu"] = ''
