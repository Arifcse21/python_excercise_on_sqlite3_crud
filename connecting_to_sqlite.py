import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    '''Create a database connection to a Sqlite database'''
    conn=None
    try:
        conn=sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

create_connection(r"test.db")

