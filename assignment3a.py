import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # delete table if it exists
    c.execute("DROP TABLE IF EXISTS integers")

    # create integers table
    c.execute("CREATE TABLE integers(number INT)")

    # add 100 random integers to the table
    for i in xrange(100):
        c.execute("INSERT INTO integers VALUES(?)", (random.randint(0,100),))