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

def create_table(conn,create_table_sql):
    try:
        cn=conn.cursor()
        cn.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database=r"test.db"

    sql_create_projects_table="""create table if not exists projects(
    id integer primary key autoincrement,
    name text not null,
    begin_date text,
    end_date text
    );"""
    sql_create_tasks_table="""create table if not exists tasks(
    id integer primary key,
    name text not null,
    priority integer,
    status_id integer not null,
    projects_id integer not null,
    begin_date text  not null,
    end_date text not null,
    foreign key(projects_id) references projects(id)
    );"""


    conn=create_connection(database)

    if conn is not  None:
        create_table(conn,sql_create_projects_table)
        create_table(conn,sql_create_tasks_table)
    else:
        print("Error! cannot create a database connection")

if __name__=='__main__':
    main()




