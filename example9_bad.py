import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM table")  # Такой код может быть подвержен SQL-инъекцией
