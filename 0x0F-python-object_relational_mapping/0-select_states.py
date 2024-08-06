#!/usr/bin/python3
import MySQLdb
import sys 

user= sys.argv[1]
password= sys.argv[2]
database= sys.argv[3]

def list_states(user,password,database):
    database = MySQLdb.connect(host="localhost",user=user,passwd=password,db=database, port =3306)
    cur = database.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)


if __name__ =='__main__':
    if len(sys.argv) != 4:
        print("Usage: select_states.py username password database_name")
    else:
        list_states(sys.argv[1],sys.argv[2],sys.argv[3])

