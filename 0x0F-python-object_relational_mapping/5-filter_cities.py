#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all cities
from the `hbtn_0e_4_usa` database where the state name matches
the given argument, sorted by city.id in ascending order.
"""
import MySQLdb
import sys


def list_cities(user, password, database, state_name):
    """
    Connect to the MySQL database and list all cities with names
    matching the provided state name.

    Args:
        user (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database to connect to.
        state_name (str): The name of the state to filter cities by.
    """
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=database,
        port=3306
    )
    cur = db.cursor()
    # Use parameterized query to avoid SQL injection
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    # Extract city names and join them with a comma
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cur.close()
    db.close()


usage = "Usage: ./5-filter_cities.py <user> <password> <database> <state_name>"

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print(usage)
    else:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
