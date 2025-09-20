# Import sqlite function to make a mini database
import sqlite3
from datetime import datetime

# Database name
DB_NAME = "tracker.db"

# Function to get conn from databae
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# function for make an table in database
def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    category TEXT NOT NULL,
                    genre TEXT,
                    rating REAL,
                    status TEXT,
                    added_date TEXT
                )''')
    conn.commit()
    conn.close()

# function for adding an item from user
def add_item(title, category, genre, rating, status):
    added_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # convert rating safely to float, or None if blank
    rating_value = float(rating) if rating.strip() != "" else None

    conn = get_connection()
    c = conn.cursor()
    c.execute(
        "INSERT INTO items (title, category, genre, rating, status, added_date) VALUES (?, ?, ?, ?, ?, ?)",
        (title, category, genre, rating_value, status, added_date)
    )
    conn.commit()
    conn.close()



#  Getting all items data from database
def get_all_items(sort_by=None, filter_category=None, filter_genre=None):
    conn = get_connection()
    c = conn.cursor()
    
    query = "SELECT * FROM items WHERE 1=1"
    params = []

    if filter_category:
        query += " AND category = ?"
        params.append(filter_category)

    if filter_genre:
        query += " AND genre = ?"
        params.append(filter_genre)

    if sort_by in ["title", "rating", "status", "category", "genre"]:
        query += f" ORDER BY {sort_by}"

    c.execute(query, params)
    rows = c.fetchall()
    conn.close()

    items = []
    for row in rows:
        items.append({
            "id": row[0],
            "title": row[1],
            "category": row[2],
            "genre": row[3],
            "rating": row[4],
            "status": row[5]
        })
    return items


    
# Get item from their unic id
def get_item_by_id(item_id):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM items WHERE id = ?" , (item_id,))
    item = c.fetchone()
    conn.close()
    return item


# for updating item if user get a typo
def update_item(item_id, title, category, genre, rating, status):
    conn = get_connection()
    c = conn.cursor()
    c.execute(""" 
        UPDATE items 
        SET title = ?, category = ?, genre = ?, rating = ?, status = ?
        WHERE id = ? """, (title, category, genre, rating, status, item_id))

    conn.commit()
    conn.close()

# Deleting a items by choosing their id
def delete_item(item_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()