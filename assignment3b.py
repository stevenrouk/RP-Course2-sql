import sqlite3

prompt = """***
What kind of aggregation would you like?
\t(AVG, MAX, MIN, SUM)
\t(QUIT or Q to quit)
--> """

while True:
    while True:
        user_agg = raw_input(prompt).upper()
        if user_agg in ['AVG', 'MAX', 'MIN', 'SUM', 'QUIT', 'Q']:
            break
        print "Sorry, that's not an accepted aggregation."

    if user_agg in ['QUIT', 'Q']:
        break

    with sqlite3.connect("newnum.db") as connection:
        c = connection.cursor()

        aggregations = {
            'AVG': "SELECT avg(number) FROM integers",
            'MAX': "SELECT max(number) FROM integers",
            'MIN': "SELECT min(number) FROM integers",
            'SUM': "SELECT sum(number) FROM integers"
        }

        for r in c.execute(aggregations[user_agg]):
            print r[0]