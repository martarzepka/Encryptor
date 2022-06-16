import os
import tkinter as tk
from tkinter import *


class ChangeLogin(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.frame1 = tk.Frame(self)
        self.frame1.pack(fill='x')
        self.createToolbar(self.frame1)

        label = tk.Label(self, text="Zmiana loginu", font=parent.title_font)
        label.pack()

        self.frame2 = tk.Frame(self)
        self.frame2.pack()

        labelLogin = tk.Label(self.frame2, text="nowy login:")
        labelLogin.grid(column=2, row=1)
        self.entryLogin = tk.Entry(self.frame2, width=15)
        self.entryLogin.grid(column=3, row=1)

        self.frame3 = tk.Frame(self)
        self.frame3.pack()

        self.label1 = tk.Label(self.frame3, text="Użytkownik o podanym loginie już istnieje.", fg="red")
        self.label1.pack()
        self.label1.pack_forget()

        self.label2 = tk.Label(self.frame3, text='Pole "nowy login" nie może być puste.', fg="red")
        self.label1.pack()
        self.label1.pack_forget()

        button1 = tk.Button(self, text="Zmień login", command=lambda: self.changeLogin(self.entryLogin.get()))
        button1.pack(pady=5)

    def refresh(self):
        self.removeLabels()
        self.entryLogin.delete(0, END)

    def removeLabels(self):
        self.label1.pack_forget()
        self.label2.pack_forget()

    def showLabel(self, number):
        self.removeLabels()
        match number:
            case 1:
                self.label1.pack()
            case 2:
                self.label2.pack()

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
        self.parent.show_frame("Profile")

    def changeLogin(self, newLogin):
        if newLogin == '':
            self.showLabel(2)
        else:
            result = self.parent.program.data.changeLogin(newLogin,self.parent.program.account)
            match result:
                case 1:             # login changed
                    self.removeLabels()
                    tk.messagebox.showinfo("Zmiana loginu", "Login został zmieniony.")
                    self.parent.show_frame("Profile")
                    self.parent.setStatusBar("Zmieniono login")
                case 2:             # account with this login already exist
                    self.showLabel(1)
                    self.entryLogin.delete(0, END)
