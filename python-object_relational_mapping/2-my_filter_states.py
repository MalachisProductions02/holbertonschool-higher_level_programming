#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
where name matches the argument exactly.
Usage: ./2-my_filter_states.py username password database_name state_name
"""

import MySQLdb
import sys


def filter_states_by_name(username, password, db_name, state_name):
    """
    Connects to MySQL DB and lists states where name matches the argument
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()
    # WARNING: Using format() as instructed (this is prone to SQL injection)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py holberton 123456 hbtn_0e_0_usa 'Arizona'")
        sys.exit(1)

    filter_states_by_name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
