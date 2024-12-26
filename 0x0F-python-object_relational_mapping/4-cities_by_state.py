#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa using id
Execute should be used only once. It should take 3 args
"""


import MySQLdb
import sys


# Ensure code not executed when imported
if __name__ == "__main__":
    # Unpack command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Retrieve all cities with their corresponding states
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC;
        """
    cursor.execute(query)

    # Fetch all the results and print
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cursor.close()
    db.close()
