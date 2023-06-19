#!/usr/bin/python3

"""Conect DataBase and query"""

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
    cur.execute("SELECT cities.id, cities.name, states.name \
                    FROM cities JOIN states ON cities.state_id \
                    = states.id ORDER BY cities.id ASC")
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
