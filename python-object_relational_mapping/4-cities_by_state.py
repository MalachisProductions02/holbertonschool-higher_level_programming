#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
with their corresponding state name.
Usage: ./4-cities_by_state.py username password database_name
"""

import MySQLdb
import sys


def list_cities(username, password, db_name):
    """
    Connects to MySQL DB and lists all cities with their state names
    ordered by cities.id ascending.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py holberton 123456 hbtn_0e_0_usa")
        sys.exit(1)

    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
