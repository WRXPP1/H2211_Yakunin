import sqlite3

connection = sqlite3.connect("itstep_DB", 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (enam) VALUES ('Nick')")
cur.execute("INSERT INTO first_table (enam) VALUES ('Liz')")
connection.commit()
connection.close()