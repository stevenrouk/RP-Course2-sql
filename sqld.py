# SELECT statement, (optional remove unicode characters)

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # unicode characters in
    """# use a for loop to iterate through the db, printing results line by line
    for row in c.execute("SELECT city, state FROM population"):
        print row"""

    # remove unicode characters
    c.execute("SELECT city, state FROM population")

    # fetchall() retrieves all records from the query as a list of tuples
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print r[0], r[1]