import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn=None
    try:
        conn=sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn
def update_task(conn,task):
    sql="""update tasks
            set
            priority=?,
            end_date=?
            where id=?"""
    cur=conn.cursor()
    cur.execute(sql,task)
    conn.commit()  #to save the changes

def main():
    database='test.db'
    conn=create_connection(database)
    with conn:
        update_task(conn,(2,'2018-02-19',2))
if __name__=='__main__':
    main()

