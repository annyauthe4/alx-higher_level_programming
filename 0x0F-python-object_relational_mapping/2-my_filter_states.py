#!/usr/bin/python3
"""
Takes in an arg and displays all values in the states table of
hbtn_0e_0_usa where name matches the arg.
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Unpack command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create cursor object to execute queries
    cursor = db.cursor()

    # Use format for the SQL query
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
        ORDER BY id ASC".format(state_name_searched)
    cursor.execute(query)

    # Fetch and display result
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database
    cursor.close()
    db.close()
