#!/usr/bin/python3
"""
Lists all cities using state name as an argument.
"""


import MySQLdb
import sys


# Ensure code not executed when imported
if __name__ == "__main__":
    # Unpack command-line argument
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor to execute queries
    cursor = db.cursor()

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
    cursor.execute(query, (state_name,))

    # Fetch and process results
    cities = cursor.fetchall()
    city_names = [city[0] for city in cities]

    # Print cities with comma separating them
    print(", ".join(city_names))

    # Close cursor and database
    cursor.close()
    db.close()
