#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa
SQL injection safe.
Usage: ./5-filter_cities.py username password database_name state_name
"""

import MySQLdb
import sys


def filter_cities(username, password, db_name, state_name):
    """
    Connects to MySQL DB and lists cities of a specific state,
    sorted by cities.id ascending.
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
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    print(", ".join(row[0] for row in rows))
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py holberton 123456 hbtn_0e_0_usa 'Arizona'")
        sys.exit(1)

    filter_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
