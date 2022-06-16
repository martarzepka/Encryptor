import os
import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as st


class AddTask(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.program = self.parent.program

        self.frame1 = tk.Frame(self)
        self.frame1.pack(fill='x')
        self.createToolbar(self.frame1)

        label = tk.Label(self, text="Dodawanie zadania", font=parent.master.title_font)
        label.pack()

        self.frame2 = tk.Frame(self)
        self.frame2.pack()

        label2 = tk.Label(self.frame2, text="Text jawny:")
        label2.grid(row=2, column=0, sticky='w')
        self.text1 = st.ScrolledText(self.frame2, width=45, height=20)
        self.text1.grid(row=3, column=0, rowspan=3, columnspan=2)

        label3 = tk.Label(self.frame2, text="Szyfrogram:")
        label3.grid(row=2, column=3, sticky='w')
        self.text2 = st.ScrolledText(self.frame2, width=45, height=20)
        self.text2.grid(row=3, column=3, rowspan=3, columnspan=2)

        self.frame3 = tk.Frame(self)
        self.frame3.pack()

        self.label4 = tk.Label(self.frame3, text="Długość tekstu jawnego i szyfrogramu musi być taka sama.", fg="red")
        self.label4.pack()
        self.label4.pack_forget()

        self.label5 = tk.Label(self.frame3, text="Oba pola muszą być wypełnione.", fg="red")
        self.label5.pack()
        self.label5.pack_forget()

        button = tk.Button(self, text="Dodaj", command=self.add, width=15)
        button.pack(pady=5)


    def refresh(self):
        self.text1.delete("1.0", END)
        self.text2.delete("1.0", END)
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
                button = tk.Button(self.toolbar, image=image, command=command)
                button.grid(row=0, column=len(self.toolbar_images) - 1)
            except tk.TclError as err:
                print(err)
        self.toolbar.pack(side="left")

    def goBack(self):
        self.parent.show_frame("TaskList")

    def add(self):
        t1 = self.text1.get("1.0", END)
        t1 = self.program.ciphers.prepareText(t1,'pl')
        t2 = self.text2.get("1.0", END)
        t2 = self.program.ciphers.prepareText(t2, 'pl')
        if len(t1) == 0 or len(t2) == 0:
            self.label4.pack_forget()
            self.label5.pack()
        elif len(t1) == len(t2):
            self.label4.pack_forget()
            self.label5.pack_forget()
            self.program.data.addTask(t2,t1)
            self.parent.show_frame("TaskList")
            self.parent.master.setStatusBar("Dodano zadanie")
        else:
            self.label5.pack_forget()
            self.label4.pack()
