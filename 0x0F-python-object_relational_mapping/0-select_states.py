#!/usr/bin/python3
"""Lists all states."""
import MySQLdb

options = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "passwd": "taco",
    "db": "hbtn_0e_0_usa",
    "charset": "utf8"
}
conn = MySQLdb.connect(**options)
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
