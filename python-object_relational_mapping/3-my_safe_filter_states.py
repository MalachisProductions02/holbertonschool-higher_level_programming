#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
where name matches the argument safely (no SQL injection).
Usage: ./3-my_safe_filter_states.py username password database_name state_name
"""

import MySQLdb
import sys


def safe_filter_states(username, password, db_name, state_name):
    """
    Connects to MySQL DB and lists states where name matches the argument safely
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py holberton 123456 hbtn_0e_0_usa 'Arizona'")
        sys.exit(1)

    safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
