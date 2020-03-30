import sqlite3
from sqlite3 import Error
from pkg_resources import get_distribution

from cpenglog import readData
from pandas import DataFrame as validDataFrame

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

def dbIsCompatible(connection: sqlite3.Connection) -> bool:
    """Checks if a sqlite3.Connection is to a compatible CPEngLog database.
    
    Carries out the checks needed to determine if the database is a CPEngLog database AND that it is a compatible version.
     
    Arguments:
        connection: An open connection to an sqlite3 database.

    Returns:
        True if the connected database is compatible with the running version of CPEngLog, otherwise False.
    """
    return True

def dbIsMigratable(connection: sqlite3.Connection) -> bool:
    """Checks if a sqlite3.Connection is to a CPEngLog database that can be automatically migrated to the current version.
    
    Carries out the checks needed to determine if the database is a CPEngLog database AND that it is a version that can be migrated to the current version by CPEngLog.
     
    Arguments:
        connection: An open connection to an sqlite3 database.

    Returns:
        True if the connected database can be migrated using Migrate in the CPEngLog File menu, otherwise False.
    """
    return False

def insertEAData(EAFilePath) -> bool:
    """Inserts database rows from an Engineers Australia myCPD export file.
    
    Does basic checks on the file name before passing to path to a reader function that returns a pandas.DataFrame.  The dataframe is then written to the database.
    
    Arguments:
        EAFilePath: A file path to an Excel file containing cpd data in the Engineers Australia myCPD format (e.g. exported from myCPD to Excel).

    Returns:
        True if successful, otherwise False.
    """
    if EAFilePath[-4:] == ".xls" or EAFilePath[-5:] == ".xlsx":
        newDataframe = readData.readEAExcel(EAFilePath)
        if isinstance(newDataframe, validDataFrame):
            print('New data!')
            return True
        else:
            return False
