import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()

co = cur.execute(
    """
SELECT * FROM daily WHERE ticker = 'JNJ' AND ts > 1629090000000;
"""
)

rows = cur.fetchall()
for row in rows:
    print(row)
