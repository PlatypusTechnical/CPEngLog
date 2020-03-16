import sqlite3
from sqlite3 import Error

def createNewSQLite(newDBPath):
    print('Creating a new SQLite database')
    connection = None
    try:
        connection = sqlite3.connect(newDBPath)
    except Error as e:
        print(e)
        return None
    finally:
        return connection