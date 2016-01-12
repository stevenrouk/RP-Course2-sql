# INSERT Command with Error Handler

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("DELETE FROM population")
    c.execute("VACUUM")
    try:
        c.execute("INSERT INTO population VALUES('New York City', \
            'NY', 8200000)")
        c.execute("INSERT INTO population VALUES('San Francisco', \
            'CA', 800000)")
        connection.commit()
    except sqlite3.OperationalError as e:
        print "** Error ** {}".format(e)