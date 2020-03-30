import sqlite3
from sqlite3 import Error
from pkg_resources import get_distribution

def connectToSQLite(DBPath: str):
    """Connects to an CPEngLog (SQLite 3) database at the path provided.
    
    If there is no database at the path provided it will be created.  So this function is used to connection to exisiting databases and to create new ones.  Note that when creating a new database, this function will creat the empty database, but initNewDB() needs to be called to initialise it.
     
    Arguments:
        DBPath: A path to an exisiting CPEngLog database OR the path to where you want one created.
    """
    print('Connecting to an SQLite database')
    connection = None
    try:
        connection = sqlite3.connect(DBPath)
    except Error as e:
        print(e)
        return None
    finally:
        return connection

def initNewDB(connection: sqlite3.Connection):
    """Initialises a newly created CPEngLog (SQLite 3) database at the path provided.
    
    Expected to be called imediately after a call to connectToSQLite() to create a new database.  It initialises a newly created SQLite 3 database into a CPEngLog database.
     
    Arguments:
        connection: An open connection to an empty sqlite3 database.
    """
    connection.execute('CREATE TABLE info (CPEngLogVer textsq)')
    LogVer = (get_distribution('CPEngLog').version,)
    connection.execute('INSERT INTO info VALUES (?)', LogVer)
    connection.commit()
