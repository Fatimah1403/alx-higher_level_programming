#!/usr/bin/python3
""" Connect Database and query """

import sys
import MYSQLdb

# db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)

if __name__ == '__main__':
    db = MYSQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")

    row_selected = cur.fetchall()

    for row in row_selected:
        print(row)
