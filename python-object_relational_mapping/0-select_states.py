#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It uses MySQLdb to connect to a MySQL server running on localhost at port 3306.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys


def list_states(username, password, db_name):
    """
    Connects to the database and lists all states ordered by id ascending.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
