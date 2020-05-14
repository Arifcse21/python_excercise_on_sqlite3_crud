import sqlite3
from sqlite3 import Error
def create_connection():
    """create a database connection to a database that resides in athe memory"""
    conn=None
    try:
        conn=sqlite3.connect(':memory:')  #It will create a db in RAM
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

create_connection()
