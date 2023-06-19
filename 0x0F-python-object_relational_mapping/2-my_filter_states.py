#!/usr/bin/python3

"""
A script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.

"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[2],
                         passwd=sys.argv[1],
                         db=sys.argv[3])
    cur = db.cursor()

    # Execute the query
    cur.execute("SELECT * FROM states \
                WHERE name LIKE BINARY '{}' \
                ORDER BY states.id ASC".format(argv[4]))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
