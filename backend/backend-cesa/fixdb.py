import sqlite3

# Use the file that actually has data (36KB)
db_name = 'gov_tech.db' 

try:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Add the missing column
    cursor.execute("ALTER TABLE applications ADD COLUMN district TEXT;")
    conn.commit()
    
    print(f"✅ Successfully added 'district' column to {db_name}")
except sqlite3.OperationalError as e:
    print(f"ℹ️ {e}")
finally:
    if conn:
        conn.close()
