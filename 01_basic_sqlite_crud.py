import sqlite3
from sqlite3 import Error

def create_connection(db_name):
    conn=None
    try:
        conn=sqlite3.connect(db_name)
    except Error as e:
        print(e)
    return conn

#def create_table(conn,table_create_sql):
#    try:
#        cn=conn.cursor()
#        cn.execute(table_create_sql)
#    except Error as e:
#        print(e)
#

#def insert_data(conn,data):
#    data_ins="""insert into author(userrname,author_name) values(?,?)"""
#    cur=conn.cursor()
#    cur.execute(data_ins,data)
#

def read_data(conn,sql):
    cur=conn.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    return data


def  main():

#   table="""create table if not exists author(
#              id integer primary key autoincrement,
#              userrname text not null,
#              author_name text not null
#              )"""
    conn=create_connection(r'01_author.sqlite')
#
    with conn:
       # create_table(conn,table)
#       data1=('almasud','Abdullah Al Masud')
#       data2=('rimon','Rimol Ali')
#       data3=('niloy','Niloy Roy')
#       data4=('sourov','Sourov Deb Sharma')
#       data5=('sathi','Sathi Rani Roy')
#       insert_data(conn,data1)
#       insert_data(conn,data2)
#       insert_data(conn,data3)
#       insert_data(conn,data4)
#       insert_data(conn,data5)
#
        select="""select id,author_name from author"""
        data_lists=list(read_data(conn,select))

        for  lst in data_lists:
           print(lst[0],'-',lst[1])
           #print(lst)

if __name__=='__main__':
    main()



