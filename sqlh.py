# joining data from multiple tables - cleanup

import sqlite3


with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # retrieve data
    c.execute("""SELECT population.city, population.population, regions.region
            FROM population, regions
            WHERE population.city = regions.city
            ORDER BY population.city ASC""")

    rows = c.fetchall()

    for r in rows:
        print "City:{} - Population:{} - Region:{}".format(r[0], r[1], r[2])