import sqlite3
from sqlite3 import Error

def connectToSQLite(DBPath):
    print('Connecting to an SQLite database')
    connection = None
    try:
        connection = sqlite3.connect(DBPath)
    except Error as e:
        print(e)
        return None
    finally:
        return connection