import configparser
import tkinter as tk
import tkinter.messagebox
from tkinter import font as tkfont
import classes
from interface.changeLogin import ChangeLogin
from interface.changePassword import ChangePassword
from interface.homePage import HomePage
from interface.login import Login
from interface.mainPage import MainPage
from interface.profile import Profile
from interface.registration import Registration

configData = "config.txt"

# the base frame of the interface
class Gui(tk.Frame):
    def __init__(self, master=None):
        self.program = classes.Program()
        self.rememberme = False
        self.logged = False
        self.config = configparser.ConfigParser()
        self.config.read(configData, "UTF8")
        tk.Frame.__init__(self, master)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        self.parent = master
        self.parent.geometry('800x520+50+50')
        self.parent.resizable(False, False)
        self.parent.protocol("WM_DELETE_WINDOW", self.quitApp)
        default = self.config["DEFAULT"]
        self.parent.geometry(default.get('geometry'))
        match default.get('remember'):
            case '0':
                self.rememberme = False
            case '1':
                self.rememberme = True
                self.logged = True
                login = default.get('login')
                self.program.account = self.program.data.accounts[login]

        self.create_basic_menu()
        self.add_menu_Account()

        self.pack(side="top", fill="both", expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, Login, Registration, MainPage, Profile, ChangeLogin, ChangePassword):
            page_name = F.__name__
            frame = F(parent=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.createStatusBar()

        if self.logged:
            self.show_frame("MainPage")
        else:
            self.show_frame("HomePage")

    def show_frame(self, pageName):    #Show a frame for the given page name
        frame = self.frames[pageName]
        frame.refresh()
        frame.tkraise()

    def create_basic_menu(self):
        self.menubar = tk.Menu(self.parent)
        self.parent["menu"] = self.menubar
        fileMenu = tk.Menu(self.menubar, tearoff=False)
        fileMenu.add_command(label="Zamknij", underline=0,command=self.quitApp, accelerator="Ctrl+Z")
        self.parent.bind("<Control-z>", self.quitApp)
        self.menubar.add_cascade(label="Plik", menu=fileMenu, underline=0)
        pass

    def add_menu_Account(self):
        fileMenu = tk.Menu(self.menubar, tearoff=False)
        for label, command, shortcut_text, shortcut in (
                ("Profil", self.goToProfile, "Ctrl+P", "<Control-p>"),
                ("Wyloguj", self.logOut, "Ctrl+W", "<Control-w>")):
            fileMenu.add_command(label=label, underline=0, command=command, accelerator=shortcut_text)
            self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="Konto", menu=fileMenu, underline=0)
        pass

    def goToProfile(self,event=None):
        if self.logged:
            self.show_frame("Profile")

    def logOut(self, event=None):
        if self.logged:
            self.show_frame("HomePage")
            self.logged = False
            self.setStatusBar("Wylogowano")

    def createStatusBar(self):
        self.frame = tk.Frame(self.parent)
        self.frame.pack(fill='x')
        self.statusbar = tk.Label(self.frame, text="Aplikacja gotowa do użytku",
                                  anchor=tk.W)
        self.statusbar.after(5000, self.clearStatusBar)
        self.statusbar.pack(side="left")
        pass

    def setStatusBar(self, txt):
        self.statusbar["text"] = txt
        self.statusbar.after(5000, self.clearStatusBar)

    def clearStatusBar(self):
        self.statusbar["text"] = ""

    def quitApp(self, event=None):
        reply = tkinter.messagebox.askyesno(
            "Zamknij",
            "Czy na pewno chcesz zamknąć aplikację?", parent=self.parent)
        if reply:
            self.program.save()

            self.config["DEFAULT"]["geometry"] = self.parent.winfo_geometry()
            if self.rememberme:
                self.config["DEFAULT"]["remember"] = '1'
                self.config["DEFAULT"]["login"] = self.program.account.login
            else:
                self.config["DEFAULT"]["remember"] = '0'

            with open(configData, 'w') as configFile:
                self.config.write(configFile)
            self.parent.destroy()
        pass

