#!#!/usr/bin/python3
"""Lists the states"""

import MySQLdb
from sys import argv


if__name__ == "__main__":
    conn = MySQL.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1].startswitch("N"):
            print(row)
    cur.close()
    conn.close()
