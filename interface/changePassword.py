import os
import tkinter as tk
from tkinter import *


class ChangePassword(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.frame1 = tk.Frame(self)
        self.frame1.pack(fill='x')
        self.createToolbar(self.frame1)

        label = tk.Label(self, text="Zmiana hasła", font=parent.title_font)
        label.pack()

        self.frame2 = tk.Frame(self)
        self.frame2.pack()

        labelPassword = tk.Label(self.frame2, text="stare hasło:")
        labelPassword.grid(column=2, row=1)
        self.entryPassword = tk.Entry(self.frame2, width=15, show='*')
        self.entryPassword.grid(column=3, row=1)

        labelNewPassword = tk.Label(self.frame2, text="nowe hasło:")
        labelNewPassword.grid(column=2, row=2)
        self.entryNewPassword = tk.Entry(self.frame2, width=15, show='*')
        self.entryNewPassword.grid(column=3, row=2)

        labelNewPasswordAgain = tk.Label(self.frame2, text="powtórz nowe hasło:")
        labelNewPasswordAgain.grid(column=2, row=3)
        self.entryNewPasswordAgain = tk.Entry(self.frame2, width=15, show='*')
        self.entryNewPasswordAgain.grid(column=3, row=3)

        self.frame3 = tk.Frame(self)
        self.frame3.pack()

        self.label1 = tk.Label(self.frame3, text="Błędne stare hasło.", fg="red")
        self.label1.pack()
        self.label1.pack_forget()

        self.label2 = tk.Label(self.frame3, text="Podane hasła nie są takie same.", fg="red")
        self.label1.pack()
        self.label1.pack_forget()

        self.label3 = tk.Label(self.frame3, text="Nowe hasło musi mieć co najmniej 8 znaków.", fg="red")
        self.label1.pack()
        self.label1.pack_forget()

        self.label4 = tk.Label(self.frame3, text="Wszystkie pola muszą być wypełnione.", fg="red")
        self.label1.pack()
        self.label1.pack_forget()

        button1 = tk.Button(self, text="Zmień hasło", command=lambda: self.changePassword(
            self.entryPassword.get(), self.entryNewPassword.get(), self.entryNewPasswordAgain.get()))
        button1.pack(pady=5)

    def refresh(self):
        self.removeLabels()
        self.entryPassword.delete(0, END)
        self.entryNewPassword.delete(0, END)
        self.entryNewPasswordAgain.delete(0, END)

    def removeLabels(self):
        self.label1.pack_forget()
        self.label2.pack_forget()
        self.label3.pack_forget()
        self.label4.pack_forget()

    def showLabel(self, number):
        self.removeLabels()
        match number:
            case 1:
                self.label1.pack()
            case 2:
                self.label2.pack()
            case 3:
                self.label3.pack()
            case 4:
                self.label4.pack()

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

    def changePassword(self, pas, newPas, newPas2):
        acc = self.parent.program.account
        if pas == '' or newPas == '' or newPas2 == '':
            self.showLabel(4)
        elif pas != acc.password:
            self.showLabel(1)
            self.entryPassword.delete(0, END)
            self.entryNewPassword.delete(0, END)
            self.entryNewPasswordAgain.delete(0, END)
        elif len(newPas)<8:
            self.showLabel(3)
            self.entryNewPassword.delete(0, END)
            self.entryNewPasswordAgain.delete(0, END)
        elif newPas != newPas2:
            self.showLabel(2)
            self.entryNewPassword.delete(0, END)
            self.entryNewPasswordAgain.delete(0, END)
        else:
            self.parent.program.data.changePassword(newPas, acc)
            self.removeLabels()
            tk.messagebox.showinfo("Zmiana hasła","Hasło zostało zmienione.")
            self.parent.show_frame("Profile")
            self.parent.setStatusBar("Zmieniono hasło")
