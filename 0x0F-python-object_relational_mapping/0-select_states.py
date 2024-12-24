#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Unpack command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch result and display
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database
    cursor.close()
    db.close()
