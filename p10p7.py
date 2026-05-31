import sqlite3

connection = sqlite3.connect("itstep_DB", 5)
cur = connection.cursor()
cur.execute("UPDATE first_table SET enam='Kate' WHERE rowid=3;")
connection.commit()
connection.close()