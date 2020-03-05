import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('CPEngLog')
        self.geometry('500x100+300+150')
        self.mainFrame = MainFrame(self)
        self['menu'] = MainMenu(self)
        self.mainFrame.pack(fill=tk.BOTH, expand=True)

class MainFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, bg='green')

class MainMenu(tk.Menu):
    def __init__(self, master=None):
        tk.Menu.__init__(self, master=None)
        fileMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label='New', command=self.newDatabase)
        fileMenu.add_command(label='Open', command=self.openDatabase)
        fileMenu.add_command(label='Close', command=self.closeDatabase)
        fileMenu.add_separator()
        fileMenu.add_command(label='Import', command=self.importData)
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=self.quit)

    def newDatabase(self):
        print('Creating a new database')

    def openDatabase(self):
        print('Opening an exisiting database')

    def closeDatabase(self):
        print('Closing this databse')

    def importData(self):
        print('Importing data')

Application().mainloop()