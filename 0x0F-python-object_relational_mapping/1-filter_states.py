#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all states
from the `hbtn_0e_0_usa` database.
"""
import MySQLdb
import sys


def list_states(user, password, database):
    """
    Connect to the MySQL database and list all states.
    Args:
        user (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database to connect to.
    """
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=database,
        port=3306
    )
    cur = db.cursor()
    cur.execute(
        "SELECT id, name FROM states WHERE name LIKE 'N% ORDER BY id ASC"
        )
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./select_states.py <user> <password> <database>")
    else:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
