import pickle
from functionality.ciphers import Ciphers

# classes holding information about accounts and tasks
class Account:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.points = 0
        self.completedTasks = []

    def addCompletedTask(self, taskNumber):
        if taskNumber not in self.completedTasks:
            self.points += 3
            self.completedTasks.append(taskNumber)
            return 1    # task was solved first time
        return 0        # task solved once again

class Task:
    def __init__(self, cryptogram, plaintext, number):
        self.number = number
        self.cryptogram = cryptogram
        self.plainText = plaintext

class Data:
    def __init__(self):
        self._accountsFile = "accounts.txt"
        self._tasksFile = "tasks.txt"
        self.accounts = {}
        self.tasks = {}
        self.loadAccounts()
        self.loadTasks()

    def loadAccounts(self):
        with open(self._accountsFile, 'rb') as file:
            self.accounts = pickle.load(file)

    def loadTasks(self):
        with open(self._tasksFile, 'rb') as file:
            self.tasks = pickle.load(file)

    def saveAccounts(self):
        with open(self._accountsFile, 'wb') as file:
            pickle.dump(self.accounts, file, pickle.HIGHEST_PROTOCOL)

    def saveTasks(self):
        with open(self._tasksFile, 'wb') as file:
            pickle.dump(self.tasks, file, pickle.HIGHEST_PROTOCOL)

    def addAccount(self,login, password):
        if login in self.accounts:
            return 2                        #account with this login already exist
        else:
            self.accounts[login] = Account(login, password)
            return 1                        #account correctly created

    def addTask(self,cryptogram, plaintext):
        self.tasks[len(self.tasks)+1] = Task(cryptogram, plaintext, len(self.tasks)+1)

    def changeLogin(self, login, acc):
        if login in self.accounts:
            return 2                        # account with this login already exist
        else:
            del self.accounts[acc.login]
            acc.login = login
            self.accounts[login] = acc
            return 1                        # login changed

    def changePassword(self, password, acc):
        acc.password = password
        self.accounts[acc.login] = acc

# the "Program" class is a relay of application functionality to the user interface
class Program:
    def __init__(self):
        self.data = Data()
        self.account = Account('default', 'default')
        self.ciphers = Ciphers()

    def save(self):
        self.data.saveAccounts()
        self.data.saveTasks()

    def login(self, login, password):
        self.account = self.data.accounts.setdefault(login)
        if self.account == None:
            return 2                           #non-existent login
        elif self.account.password == password:
            return 1                           #valid login and password
        else:
            return 3                           #wrong password
