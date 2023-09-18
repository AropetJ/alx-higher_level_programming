#!/usr/bin/python3

import MySQLdb
import sys

if len(sys.argv) != 5:
    print("Usage: {} <username> <password> <database> <state_name>"
          .format(sys.argv[0]))
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

try:
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = connection.cursor()

    query = """
    SELECT GROUP_CONCAT(cities.name ORDER BY cities.id SEPARATOR ', ')
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    """

    cursor.execute(query, (state_name,))

    result = cursor.fetchone()
    if result[0]:
        print(result[0])
    else:
        print("")

    cursor.close()
    connection.close()

except MySQLdb.Error as e:
    print("MySQL Error:", e)
    sys.exit(1)
