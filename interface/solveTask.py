import os
import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as st
import time


class SolveTask(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.program = self.parent.program
        self.task = None

        self.frame1 = tk.Frame(self)
        self.frame1.pack(fill='x')
        self.createToolbar(self.frame1)

        label = tk.Label(self, text="Rozwiąż zadanie", font=parent.master.title_font)
        label.pack()

        self.frame2 = tk.Frame(self)
        self.frame2.pack()

        label1 = tk.Label(self.frame2, text="Szyfrogram:")
        label1.grid(row=2, column=0, sticky='w')
        self.text1 = st.ScrolledText(self.frame2, width=45, height=20)
        self.text1.grid(row=3, column=0, rowspan=3, columnspan=2)

        label2 = tk.Label(self.frame2, text="Rozwiązanie:")
        label2.grid(row=2, column=3, sticky='w')
        self.text2 = st.ScrolledText(self.frame2, width=45, height=20)
        self.text2.grid(row=3, column=3, rowspan=3, columnspan=2)

        self.frame3 = tk.Frame(self)
        self.frame3.pack()

        self.label3 = tk.Label(self.frame3, text="Błędne rozwiązanie!", fg="red")
        self.label3.pack()
        self.label3.pack_forget()

        self.label4 = tk.Label(self.frame3, text="Poprawna odpowiedź!\nOtrzymujesz 3 pkt.", fg="green")
        self.label4.pack()
        self.label4.pack_forget()

        self.label5 = tk.Label(self.frame3, text="Poprawna odpowiedź!", fg="green")
        self.label5.pack()
        self.label5.pack_forget()

        button = tk.Button(self, text="Sprawdź", command=self.check, width=15)
        button.pack(pady=5)

    def refresh(self):
        self.text1.configure(state='normal')
        self.text1.delete("1.0", END)
        self.text1.insert(INSERT, self.task.cryptogram)
        self.text1.config(state="disabled")
        self.text2.delete("1.0", END)
        self.label3.pack_forget()
        self.label4.pack_forget()
        self.label5.pack_forget()

    def createToolbar(self, parent):
        self.toolbar_images = []
        self.toolbar = tk.Frame(parent)
        for image, command in (
                ("images/return.png", self.goBack),
                ("images/close.png", self.parent.master.quitApp)):
            image = os.path.join(os.path.dirname(__file__), image)
            try:
                image = tk.PhotoImage(file=image)
                self.toolbar_images.append(image)
                button = tk.Button(self.toolbar, image=image,
                                        command=command)
                button.grid(row=0, column=len(self.toolbar_images) - 1)
            except tk.TclError as err:
                print(err)
        self.toolbar.pack(side="left")

    def goBack(self):
        self.parent.show_frame("TaskList")
        pass

    def check(self):
        tmp = self.program.ciphers.prepareText(self.text2.get("1.0", END), 'pl', False, False)
        self.text2.delete("1.0", END)
        self.text2.insert(INSERT, tmp)
        self.update()
        if tmp == self.task.plainText:
            res = self.program.account.addCompletedTask(self.task.number)
            self.label3.pack_forget()
            if res == 1:
                self.label4.pack()
                self.label5.pack_forget()
            else:
                self.label5.pack()
                self.label4.pack_forget()
            self.update()

            time.sleep(2)
            self.parent.show_frame("TaskList")
            if res == 1:
                self.parent.master.setStatusBar("Dodano punkty do konta")
        else:
            self.label3.pack()
            self.label4.pack_forget()
            self.label5.pack_forget()





