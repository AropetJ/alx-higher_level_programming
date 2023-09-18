#!/usr/bin/python3

import MySQLdb
import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 5:
    print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
    sys.exit(1)

# Get command-line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

try:
    # Connect to the MySQL server
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Create a parameterized SQL query to select states by name
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"

    # Execute the SQL query with the user-provided state_name
    cursor.execute(query, (state_name,))

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    connection.close()

except MySQLdb.Error as e:
    print("MySQL Error:", e)
    sys.exit(1)
