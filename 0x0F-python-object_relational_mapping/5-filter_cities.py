#!/usr/bin/python3

"""
A script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa

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
    cur.execute("""
        SELECT
            cities.id, cities.name
        FROM
            cities
        JOIN
            states
        ON
            cities.state_id = states.id
        WHERE
            states.name LIKE BINARY %(state_name)s
        ORDER BY
            cities.id ASC
        """, {
            'state_name': argv[4]
        })

    row_selected = cur.fetchall()

    if row_selected is not None:
        print(", ".join([row[1] for row in row_selected]))
