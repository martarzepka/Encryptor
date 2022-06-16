import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import tkinter.scrolledtext as st
from interface.taskList import TaskList
from interface.addTask import AddTask
from interface.solveTask import SolveTask


class MainPage(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.program = self.parent.program
        self.createWorkingWindow()
        self.refresh()

    def refresh(self):
        self.tab1.deafaultSettings()
        self.parent.parent["menu"] = self.parent.menubar
        self.tab2.frames["TaskList"].refresh()

    def createWorkingWindow(self):
        self.workWindow = tk.Frame(self)
        self.workWindow.grid(row=1, column=0, columnspan=10, rowspan=1, sticky=NSEW)
        self.tabControl = ttk.Notebook(self.workWindow)
        self.tab1 = Tab1(self.tabControl, self.program)
        self.tab2 = Tab2(self.tabControl, self.parent, self.program)
        self.tabControl.add(self.tab1, text='szyfrowanie')
        self.tabControl.add(self.tab2, text='zadania')
        self.tabControl.pack(expand=1, fill='both')
        pass


class Tab1(tk.Frame):

    def __init__(self, parent, program):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.program = program
        self.cipher = tk.StringVar()
        self.enOrPl = tk.StringVar()
        self.removeSpaces = tk.BooleanVar()
        self.removerOtherCh = tk.BooleanVar()
        self.key = tk.StringVar()
        self.shiftEn = self.createShifts(26)
        self.shiftPl = self.createShifts(35)
        self.plainText = tk.StringVar()
        self.cryptogram = tk.StringVar()
        self.createWorkingWindow()

    def createWorkingWindow(self):
        label1 = tk.Label(self, text="Szyfr:")
        label1.grid(row=0, column=0, sticky='w')
        self.entry1 = ttk.Combobox(self, textvariable=self.cipher, width=15, state='readonly')
        self.entry1.grid(row=1, column=0, sticky='w')
        self.entry1['values'] = ('cezara', 'atbasz', 'monoalfabetyczny')
        self.entry1.bind("<<ComboboxSelected>>", self.showSetting)

        label2 = tk.Label(self, text="Alfabet:")
        label2.grid(row=0, column=1, sticky='w', columnspan=2)
        self.entry2 = Radiobutton(self, text="ABCDEFGHIJKLMNOPQRSTUVWXYZ", variable=self.enOrPl, value='en',
                                  command = self.setShift)
        self.entry2.grid(row=1, column=1, sticky='w', columnspan=2)
        self.entry3 = Radiobutton(self, text="AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŻŹ", variable=self.enOrPl, value='pl',
                                  command = self.setShift)
        self.entry3.grid(row=2, column=1, sticky='w', columnspan=2)

        label3 = tk.Label(self, text="Pozostałe znaki:")
        label3.grid(row=0, column=3, sticky='w')
        self.entry4 = Checkbutton(self, text="usuń spacje", variable=self.removeSpaces, onvalue=1, offvalue=0)
        self.entry4.grid(row=1, column=3, sticky='w')
        self.entry5 = Checkbutton(self, text="usuń znaki spoza alfabetu", variable=self.removerOtherCh, onvalue=1,
                                  offvalue=0)
        self.entry5.grid(row=2, column=3, sticky='w')

        self.label4 = tk.Label(self, text="klucz:")
        self.label4.grid(row=3, column=0, sticky='e')
        self.entry6 = tk.Entry(self, width=25)
        self.entry6.grid(row=3, column=1, sticky='w')
        self.label4.grid_remove()
        self.entry6.grid_remove()

        self.label5 = tk.Label(self, text="przesunięcie:")
        self.label5.grid(row=3, column=0, sticky='e')
        self.entry7 = ttk.Combobox(self, textvariable=self.key, width=15, state='readonly')
        self.entry7.grid(row=3, column=1, sticky='w')
        self.entry7['values'] = self.shiftEn
        self.label5.grid_remove()
        self.entry7.grid_remove()

        label8 = tk.Label(self, text="Text jawny:")
        label8.grid(row=4, column=0, sticky='w')
        self.text1 = st.ScrolledText(self, width=44, height=20)
        self.text1.grid(row=5, column=0, rowspan=7, columnspan=2)

        label9 = tk.Label(self, text="Szyfrogram:")
        label9.grid(row=4, column=3, sticky='w')
        self.text2 = st.ScrolledText(self, width=44, height=20)
        self.text2.grid(row=5, column=3, rowspan=7, columnspan=2)

        buttonEncrypt = tk.Button(self, text="->", command=self.encrypt, width=4, height=2)
        buttonEncrypt.grid(row=7, column=2, padx=8)
        buttonDecrypt = tk.Button(self, text="<-", command=self.decrypt, width=4, height=2)
        buttonDecrypt.grid(row=9, column=2, padx=8)

    def createShifts(self, x):
        list = []
        for i in range(x):
            list.append(str(i+1))
        return list

    def setShift(self):
        match self.enOrPl.get():
            case 'en':
                self.entry7['values'] = self.shiftEn
                if int(self.key.get()) > 26:
                    self.key.set('3')
            case 'pl':
                self.entry7['values'] = self.shiftPl

    def showSetting(self, event=None):
        match self.cipher.get():
            case 'cezara':
                self.label5.grid()
                self.entry7.grid()
                self.label4.grid_remove()
                self.entry6.grid_remove()
            case 'atbasz':
                self.label5.grid_remove()
                self.entry7.grid_remove()
                self.label4.grid_remove()
                self.entry6.grid_remove()
            case 'monoalfabetyczny':
                self.entry6.delete(0, END)
                self.label5.grid_remove()
                self.entry7.grid_remove()
                self.label4.grid()
                self.entry6.grid()

    def deafaultSettings(self):
        self.cipher.set('cezara')
        self.showSetting()
        self.label5.grid()
        self.entry7.grid()
        self.enOrPl.set('en')
        self.removeSpaces.set(True)
        self.removerOtherCh.set(True)
        self.key.set('3')
        self.text1.delete("1.0", END)
        self.text2.delete("1.0", END)

    def encrypt(self):
        if self.text1.get("1.0", END) != '':
            match self.cipher.get():
                case 'cezara':
                    tmp = self.program.ciphers.prepareText(self.text1.get("1.0", END), self.enOrPl.get(),
                                                           self.removerOtherCh.get(), self.removeSpaces.get())
                    self.text1.delete("1.0", END)
                    self.text1.insert(INSERT, tmp)
                    tmp = self.program.ciphers.encrypt(self.text1.get("1.0", END), 'caesar', self.enOrPl.get(),
                                                       keyNumber=self.key.get())
                    self.text2.delete("1.0", END)
                    self.text2.insert(INSERT, tmp)
                case 'atbasz':
                    tmp = self.program.ciphers.prepareText(self.text1.get("1.0", END), self.enOrPl.get(),
                                                           self.removerOtherCh.get(), self.removeSpaces.get())
                    self.text1.delete("1.0", END)
                    self.text1.insert(INSERT, tmp)
                    tmp = self.program.ciphers.encrypt(self.text1.get("1.0", END), 'atbasz', self.enOrPl.get())
                    self.text2.delete("1.0", END)
                    self.text2.insert(INSERT, tmp)
                case 'monoalfabetyczny':
                    tmp = self.program.ciphers.prepareText(self.entry6.get(), self.enOrPl.get())
                    self.entry6.delete(0, END)
                    self.entry6.insert(INSERT, tmp)
                    tmp = self.program.ciphers.prepareText(self.text1.get("1.0", END), self.enOrPl.get(),
                                                           self.removerOtherCh.get(), self.removeSpaces.get())
                    self.text1.delete("1.0", END)
                    self.text1.insert(INSERT, tmp)
                    tmp = self.program.ciphers.encrypt(self.text1.get("1.0", END), 'monoalphabetic',
                                                       self.enOrPl.get(), self.entry6.get())
                    self.text2.delete("1.0", END)
                    self.text2.insert(INSERT, tmp)

    def decrypt(self):
        if self.text2.get("1.0", END) != '':
            match self.cipher.get():
                case 'cezara':
                    tmp = self.program.ciphers.prepareText(self.text2.get("1.0", END), self.enOrPl.get(),
                                                           self.removerOtherCh.get(), self.removeSpaces.get())
                    self.text2.delete("1.0", END)
                    self.text2.insert(INSERT, tmp)
                    tmp = self.program.ciphers.decrypt(self.text2.get("1.0", END), 'caesar',
                                                       self.enOrPl.get(), keyNumber=self.key.get())
                    self.text1.delete("1.0", END)
                    self.text1.insert(INSERT, tmp)
                case 'atbasz':
                    tmp = self.program.ciphers.prepareText(self.text2.get("1.0", END), self.enOrPl.get(),
                                                           self.removerOtherCh.get(), self.removeSpaces.get())
                    self.text2.delete("1.0", END)
                    self.text2.insert(INSERT, tmp)
                    tmp = self.program.ciphers.decrypt(self.text2.get("1.0", END), 'atbasz', self.enOrPl.get())
                    self.text1.delete("1.0", END)
                    self.text1.insert(INSERT, tmp)
                case 'monoalfabetyczny':
                    tmp = self.program.ciphers.prepareText(self.entry6.get(), self.enOrPl.get())
                    self.entry6.delete(0, END)
                    self.entry6.insert(INSERT, tmp)
                    tmp = self.program.ciphers.prepareText(self.text2.get("1.0", END), self.enOrPl.get(),
                                                           self.removerOtherCh.get(), self.removeSpaces.get())
                    self.text2.delete("1.0", END)
                    self.text2.insert(INSERT, tmp)
                    tmp = self.program.ciphers.decrypt(self.text2.get("1.0", END), 'monoalphabetic',
                                                       self.enOrPl.get(), self.entry6.get())
                    self.text1.delete("1.0", END)
                    self.text1.insert(INSERT, tmp)


class Tab2(tk.Frame):

    def __init__(self, parent, master, program):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.master = master
        self.program = program
        self.frames = {}
        for F in (TaskList, SolveTask, AddTask):
            page_name = F.__name__
            frame = F(parent=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("TaskList")

    def show_frame(self, pageName):  # Show a frame for the given page name
        frame = self.frames[pageName]
        frame.refresh()
        frame.tkraise()

    def changeTask(self, task):
        frame = self.frames["SolveTask"]
        frame.task = task
