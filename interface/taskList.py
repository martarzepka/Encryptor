import tkinter as tk


class TaskList(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.program = self.parent.program

        self.frame1 = tk.Frame(self)
        self.frame1.pack(fill="both")

        self.addButton = tk.Button(self, text="Dodaj zadanie", command=lambda: self.parent.show_frame("AddTask"))
        self.addButton.pack()

    def refresh(self):
        for widget in self.frame1.winfo_children():
            widget.destroy()
        solvedTasks = self.program.account.completedTasks
        col = 0
        for T in self.program.data.tasks.values():
            task = []
            nr = T.number
            rowNr = (nr-1) % 10
            colNr = 3 * col
            task.append(tk.Label(self.frame1, text="zadanie " + str(nr)))
            task[0].grid(row=rowNr, column=colNr, pady=5, padx=5)
            task.append(tk.Button(self.frame1, text="zobacz", command=(lambda x=nr: self.solve(x))))
            task[1].grid(row=rowNr, column=1 + colNr, pady=5, padx=2)
            task.append(tk.Label(self.frame1, text="rozwiązane", fg="green"))

            if nr in solvedTasks:
                task[2].grid(row=rowNr, column=2 + colNr, pady=5, padx=2)

            if nr % 10 == 0:
                col += 1

    def solve(self, taskNr):
        self.parent.changeTask(self.program.data.tasks[taskNr])
        self.parent.show_frame("SolveTask")
        pass
