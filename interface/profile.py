import os
import tkinter as tk


class Profile(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.acc = self.parent.program.account

        self.frame1 = tk.Frame(self)
        self.frame1.pack(fill='x')
        self.createToolbar(self.frame1)

        label = tk.Label(self, text="Moje konto", font=parent.title_font)
        label.pack()

        self.frame2 = tk.Frame(self)
        self.frame2.pack()

        label1 = tk.Label(self.frame2, text="login:")
        label1.grid(row=1, column=1, sticky='e')
        self.label2 = tk.Label(self.frame2, text=self.acc.login)
        self.label2.grid(row=1, column=2, sticky='w')
        button1 = tk.Button(self.frame2, text="zmień login", command=lambda: self.parent.show_frame("ChangeLogin"))
        button1.grid(row=1, column=3)

        label3 = tk.Label(self.frame2, text="hasło:")
        label3.grid(row=2, column=1, sticky='e')
        h = len(self.acc.password) * '*'
        self.label4 = tk.Label(self.frame2, text=h)
        self.label4.grid(row=2, column=2, sticky='w')
        button2 = tk.Button(self.frame2, text="zmień hasło", command=lambda: self.parent.show_frame("ChangePassword"))
        button2.grid(row=2, column=3)

        label5 = tk.Label(self.frame2, text="punkty:")
        label5.grid(row=3, column=1, sticky='e')
        self.label6 = tk.Label(self.frame2, text=self.acc.points)
        self.label6.grid(row=3, column=2, sticky='w')

    def refresh(self):
        self.acc = self.parent.program.account
        self.label2.configure(text=self.acc.login)
        h = len(self.acc.password) * '*'
        self.label4.configure(text=h)
        self.label6.configure(text=self.acc.points)

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
        self.parent.show_frame("MainPage")
        pass
