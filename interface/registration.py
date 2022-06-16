import os
import tkinter as tk
from tkinter import *


class Registration(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.frame1 = tk.Frame(self)
        self.frame1.pack(fill='x')
        self.createToolbar(self.frame1)

        label = tk.Label(self, text="Rejestracja", font=parent.title_font)
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

        labelPasswordAgain = tk.Label(self.frame2, text="powtórz hasło:")
        labelPasswordAgain.grid(column=2, row=3)
        self.entryPasswordAgain = tk.Entry(self.frame2, width=15, show='*')
        self.entryPasswordAgain.grid(column=3, row=3)

        self.frame3 = tk.Frame(self)
        self.frame3.pack()

        self.label1 = tk.Label(self.frame3, text="Użytkownik o podanym loginie już istnieje.", fg="red")
        self.label1.pack()
        self.label1.pack_forget()

        self.label2 = tk.Label(self.frame3, text="Podane hasła nie są takie same.", fg="red")
        self.label2.pack()
        self.label2.pack_forget()

        self.label3 = tk.Label(self.frame3, text="Hasło musi mieć co najmniej 8 znaków.", fg="red")
        self.label3.pack()
        self.label3.pack_forget()

        self.label4 = tk.Label(self.frame3, text="Wszystkie pola muszą być wypełnione.", fg="red")
        self.label4.pack()
        self.label4.pack_forget()

        button1 = tk.Button(self, text="Zarejestruj", command=lambda: self.registration
                            (self.entryLogin.get(), self.entryPassword.get(), self.entryPasswordAgain.get()))
        button1.pack(pady=5)

    def refresh(self):
        self.removeLabels()
        self.entryLogin.delete(0, END)
        self.entryPassword.delete(0, END)
        self.entryPasswordAgain.delete(0, END)

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
        self.parent.show_frame("HomePage")
        pass

    def registration(self, log, pas, pas2):
        if log == '' or pas == '' or pas2 == '':
            self.showLabel(4)
        elif len(pas)<8:
            self.showLabel(3)
            self.entryPassword.delete(0, END)
            self.entryPasswordAgain.delete(0, END)
        elif pas != pas2:
            self.showLabel(2)
            self.entryPassword.delete(0, END)
            self.entryPasswordAgain.delete(0, END)
        else:
            result = self.parent.program.data.addAccount(log,pas)
            match result:
                case 1:                                             #account correctly created
                    tk.messagebox.showinfo("Rejestracja","Konto zostało założone poprawnie.")
                    self.removeLabels()
                    self.parent.show_frame("Login")
                    self.parent.setStatusBar("Zarejestrowano")
                case 2:                                             #account with this login already exist
                    self.showLabel(1)
                    self.entryLogin.delete(0, END)
                    self.entryPassword.delete(0, END)
                    self.entryPasswordAgain.delete(0, END)
