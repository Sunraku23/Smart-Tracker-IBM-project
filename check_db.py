import sqlite3

conn = sqlite3.connect('tracker.db')
c = conn.cursor()

# Check what tables exist
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables in DB:", c.fetchall())

# Check the columns in 'items'
c.execute("PRAGMA table_info(items);")
print("Columns in items:", c.fetchall())

conn.close()
