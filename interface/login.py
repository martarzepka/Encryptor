import os
import tkinter as tk
from tkinter import *


class Login(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.rememberme = tk.BooleanVar()

        self.frame1 = tk.Frame(self)
        self.frame1.pack(fill='x')
        self.createToolbar(self.frame1)

        label = tk.Label(self, text="Logowanie", font=parent.title_font)
        label.pack()

        self.frame2 = tk.Frame(self)
        self.frame2.pack()

        labelLogin = tk.Label(self.frame2, text="login:")
        labelLogin.grid(column=2, row=1)
        self.entryLogin = tk.Entry(self.frame2, width=15)
        self.entryLogin.grid(column=3, row=1)

        labelPassword = tk.Label(self.frame2, text="hasło:")
        labelPassword.grid(column=2, row=2)
        self.entryPassword = tk.Entry(self.frame2, width=15, show='*')
        self.entryPassword.grid(column=3, row=2)

        checkbutton = tk.Checkbutton(self.frame2, text="zapamiętaj mnie", variable=self.rememberme)
        checkbutton.grid(column=2, row=3, columnspan=2)

        self.frame3 = tk.Frame(self)
        self.frame3.pack()

        self.label1 = tk.Label(self.frame3, text="Użytkownik o podanym loginie nie istnieje.", fg="red")
        self.label1.pack()
        self.label1.pack_forget()

        self.label2 = tk.Label(self.frame3, text="Niepoprawne hasło.", fg="red")
        self.label2.pack()
        self.label2.pack_forget()

        self.label3 = tk.Label(self.frame3, text="Wszystkie pola muszą być wypełnione.", fg="red")
        self.label3.pack()
        self.label3.pack_forget()

        button1 = tk.Button(self, text="Zaloguj",
                            command=lambda: self.login(self.entryLogin.get(), self.entryPassword.get()))
        button1.pack(pady=5)

    def refresh(self):
        self.removeLabels()
        self.rememberme.set(False)
        self.entryLogin.delete(0, END)
        self.entryPassword.delete(0, END)

    def removeLabels(self):
        self.label1.pack_forget()
        self.label2.pack_forget()
        self.label3.pack_forget()

    def showLabel(self, number):
        self.removeLabels()
        match number:
            case 1:
                self.label1.pack()
            case 2:
                self.label2.pack()
            case 3:
                self.label3.pack()

    def createToolbar(self, parent):
        self.toolbar_images = []
        self.toolbar = tk.Frame(parent)
        for image, command in (
                ("images/return.png", self.goBack),
                ("images/close.png", self.parent.quitApp)):
            image = os.path.join(os.path.dirname(__file__), image)
            try:
                image = tk.PhotoImage(file=image)
                self.toolbar_images.append(image)
                button = tk.Button(self.toolbar, image=image, command=command)
                button.grid(row=0, column=len(self.toolbar_images) - 1)
            except tk.TclError as err:
                print(err)
        self.toolbar.pack(side="left")

    def goBack(self):
        self.parent.show_frame("HomePage")
        pass

    def login(self, log, pas):
        if log == '' or pas == '':
            self.showLabel(3)
        else:
            result = self.parent.program.login(log,pas)
            match result:
                case 1:                                             #valid login and password
                    self.parent.show_frame("MainPage")
                    self.parent.setStatusBar("Zalogowano")
                    self.parent.rememberme = self.rememberme.get()
                    self.parent.logged = True
                    self.parent.frames['MainPage'].tabControl.select(0)
                    self.removeLabels()
                case 2:                                             #non-existent login
                    self.showLabel(1)
                    self.entryLogin.delete(0, END)
                    self.entryPassword.delete(0, END)
                case 3:                                             #wrong password
                    self.showLabel(2)
                    self.entryPassword.delete(0, END)
