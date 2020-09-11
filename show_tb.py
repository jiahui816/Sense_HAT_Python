import sqlite3

connection = sqlite3.connect('sensehat.db')
cursor = connection.cursor()
cursor.execute("select * from temp_humid;")
print(cursor.fetchall())