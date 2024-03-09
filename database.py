import json
import sqlite3
import os

def init_db():
    """Initialize database and create tables"""
    # Create directory for database if it doesn't exist
    os.makedirs('instance', exist_ok=True)
    
    # Connect to SQLite database (will create if it doesn't exist)
    conn = sqlite3.connect('instance/nobel.db')
    cursor = conn.cursor()
    
    # Create Nobel Prize winners table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS nobel_winners (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        year INTEGER,
        category TEXT,
        country TEXT,
        born_in TEXT,
        link TEXT
    )
    ''')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
def populate_db():
    """Populate database with Nobel Prize data from JSON file"""
    conn = sqlite3.connect('instance/nobel.db')
    cursor = conn.cursor()
    
    # Check if data already exists
    cursor.execute("SELECT COUNT(*) FROM nobel_winners")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return  # Database already populated
    
    # Load data from JSON file
    with open('winners.json', 'r') as f:
        winners_data = json.load(f)
    
    # Insert data into the database
    for winner in winners_data:
        cursor.execute(
            "INSERT INTO nobel_winners (name, year, category, country, born_in, link) VALUES (?, ?, ?, ?, ?, ?)",
            (winner.get('name', ''), 
             winner.get('year', 0), 
             winner.get('category', ''), 
             winner.get('country', ''), 
             winner.get('born_in', ''), 
             winner.get('link', ''))
        )
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

def get_winners_by_country():
    """Get count of Nobel Prize winners grouped by country"""
    conn = sqlite3.connect('instance/nobel.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Query to count winners by country, excluding empty countries
    cursor.execute("""
    SELECT country, COUNT(*) as count 
    FROM nobel_winners 
    WHERE country != '' 
    GROUP BY country 
    ORDER BY count DESC
    """)
    
    result = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return result

def get_random_winners(limit=5):
    """Get a random selection of Nobel Prize winners"""
    conn = sqlite3.connect('instance/nobel.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT id, name, year, category, country, born_in 
    FROM nobel_winners 
    ORDER BY RANDOM() 
    LIMIT ?
    """, (limit,))
    
    result = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return result
