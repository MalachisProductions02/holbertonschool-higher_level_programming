#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys


def filter_states(username, password, db_name):
    """
    Connect to the database and list states whose name starts with 'N', ordered by id ascending.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py holberton 123456 hbtn_0e_0_usa")
        sys.exit(1)

    filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
