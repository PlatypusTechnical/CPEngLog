import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from cpenglog import dbSQLite

class Application(tk.Tk):
    """The instance of the application.

    Specifically, used to manage application based UI processes (e.g. starting window properties) and is what the main Tkinter event loop runs on.
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('CPEngLog')
        self.geometry('500x100+300+150')
        self.mainFrame = MainFrame(self)
        self.mainMenu = MainMenu(self)
        self['menu'] = self.mainMenu #MainMenu(self)
        self.mainFrame.pack(fill=tk.BOTH, expand=True)

        self.openDBpath = None
        self.dbConnection = None
        self.protocol("WM_DELETE_WINDOW", self.quitCleanup())

    def quitCleanup(self):
        if self.dbConnection:
            self.dbConnection.close()

class MainFrame(tk.Frame):
    """The instance of the application's main frame.

    Specifically, draws the contents of the main window.
    """
    def __init__(self, master):
        tk.Frame.__init__(self, bg='green')

class MainMenu(tk.Menu):
    """The instance of the application's main menu.

    Specifically, manages the deisgn and contents of the main windows menu system.
    """
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
        """Called by the 'New' item in the 'File' menu and manages the process of creating a new CPD database.  Does not itself do any work, but calls functions from other modules.
     
        Arguments:
            Nil.
        """
        if self.master.dbConnection != None:
            self.closeDatabase()
        newDBpath = tk.filedialog.asksaveasfilename()
        if len(newDBpath) > 0:
            if newDBpath[-4:] != ".cpd":
                newDBpath = newDBpath + ".cpd"
            print('Creating a new database: ', newDBpath, len(newDBpath))
            newConnection = dbSQLite.connectToSQLite(newDBpath)
            if newConnection:
                self.master.openDBpath = newDBpath
                self.master.dbConnection = newConnection
                dbSQLite.setupNewDB(self.master.dbConnection)

    def openDatabase(self):
        """Called by the 'Open' item in the 'File' menu and manages the process of loading and exisitng database into the application.  Does not itself do any work, but calls functions from other modules.
     
        Arguments:
            Nil.
        """
        if self.master.dbConnection != None:
            self.closeDatabase()
        openDBpath = tk.filedialog.askopenfilename()
        if len(openDBpath) > 0:
#            if openDBpath[-4:] != ".cpd":
#                openDBpath = openDBpath + ".cpd"
            print('Opening:', openDBpath)
            newConnection = dbSQLite.connectToSQLite(openDBpath)
            if newConnection:
                self.master.openDBpath = openDBpath
                self.master.dbConnection = newConnection
#        self.master.openDBpath = tk.filedialog.askopenfilename()
#        print('Opening:', self.master.openDBpath)


    def closeDatabase(self):
        """Called by the 'Close' item in the 'File' menu and manages the process of closing the database that is currently open.  Does not itself do any work, but calls functions from other modules.
     
        Arguments:
            Nil.
        """
#        print('Closing this databse')
        if self.master.dbConnection:
            self.master.dbConnection.close()

        self.master.dbConnection = None
        self.master.openDBpath = None

    def importData(self):
        """Called by the 'Import' item in the 'File' menu and manages the process of importing data from another source into the current database.  Does not itself do any work, but calls functions from other modules.
     
        Arguments:
            Nil.
        """
        print('Importing data')
        if self.master.dbConnection == None:
            print('No DB available')
            tk.messagebox.showerror("Error: No database connection", "You need to be connected to a database to import data.\n\nPlease open an exisitng database or create a new one, then try to import again.")


Application().mainloop()