#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all states
from the `hbtn_0e_0_usa` database where the state name matches
the given argument.
"""
import MySQLdb
import sys


def list_states(user, password, database, state_name):
    """
    Connect to the MySQL database and list all states with a name matching state_name.
    
    Args:
        user (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database to connect to.
        state_name (str): The name of the state to filter by.
    """
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=database,
        port=3306
    )
    cur = db.cursor()
    # Use format method to insert the state name into the query
    query = "SELECT id, name FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <user> <password> <database> <state_name>")
    else:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
