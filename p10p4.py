import sqlite3

connection = sqlite3.connect("itstep_DB", 5)
cur = connection.cursor()
cur.execute("SELECT rowid, enam FROM first_table;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()