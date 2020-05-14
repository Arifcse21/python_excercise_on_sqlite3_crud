import sqlite3
from sqlite3 import  Error

def create_connection(db_file):
    conn=None
    try:
        conn=sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn
def delete_task(conn,id):
    sql="""delete from tasks where id=?"""
    cur=conn.cursor()
    cur.execute(sql,(id,))
    conn.commit()

def delete_all_tasks(conn):
    sql="""delete from tasks"""
    cur=conn.cursor()
    cur.execute(sql)
    conn.commit()

def main():
    database=r'test.db'
    conn=create_connection(database)
    with conn:
        delete_task(conn,2);
        #delete_all_tasks(conn)

if __name__=='__main__':
    main()





