import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn=None
    try:
        conn=sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_project(conn,project):
    sql="""insert into projects(name,begin_date,end_date) values(?,?,?)"""
    cur=conn.cursor()
    cur.execute(sql,project)
    return cur.lastrowid

def create_task(conn,task):
    sql="""insert into tasks(name,priority,status_id,projects_id,begin_date,end_date
    ) Values(?,?,?,?,?,?)"""
    cur=conn.cursor()
    cur.execute(sql,task)
    return cur.lastrowid


def main():
    database='test.db'
    conn=create_connection(database)
    with conn:
        project=('school management system','2018-01-01','2018-03-31');
        project_id=create_project(conn,project)

        task1=('Team members selection',1,1,project_id,'2018-01-02','2018-01-05')
        task2=('Project ER diagram',2,2,project_id,'2018-01-31','2018-02-04')
        create_task(conn,task1)
        create_task(conn,task2)


if __name__=='__main__':
    main()




