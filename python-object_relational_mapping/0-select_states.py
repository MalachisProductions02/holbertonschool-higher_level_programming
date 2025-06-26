#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It connects to a MySQL server running on localhost at port 3306
and retrieves all rows in the 'states' table, sorted by id in ascending order.

Usage:
    ./0-select_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys


def list_states(username, password, db_name):
    """
    Connects to the MySQL database and prints all states ordered by id.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        db_name (str): The name of the database.
    """
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        db.close()
    except Exception as e:
        print("Error connecting to database:", e)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database_name>")
        sys.exit(1)

    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
