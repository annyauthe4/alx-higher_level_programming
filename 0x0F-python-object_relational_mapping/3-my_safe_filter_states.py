#!/usr/bin/python3
"""
Displays all values of states table from hbtn_0e_0_usa database
where name match argument and is safe from MySQL injection.
"""


import MySQLdb
import sys


# Ensure code is not executed when imported
if __name__ == "__main":
    # Unpack command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

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

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))

    # Display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database
    cursor.close()
    db.close()
