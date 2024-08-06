#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all cities
from the `hbtn_0e_4_usa` database, sorted by city.id in ascending order.
"""
import MySQLdb
import sys


def list_cities(user, password, database):
    """
    Connect to the MySQL database and list all cities.

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
    # Single execute() call to retrieve cities and their state names
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


usage = (
    "Usage: ./4-cities_by_state.py <user> <password> <database>"
)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(usage)
    else:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
