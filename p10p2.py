import sqlite3

connection = sqlite3.connect("itstep_DB", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE first_table (enam TEXT);")
connection.commit()
connection.close()