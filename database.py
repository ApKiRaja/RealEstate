import psycopg2
from config import DATABASE_URL

def create_tables():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        chat_id BIGINT UNIQUE,
        name VARCHAR(100),
        phone VARCHAR(20),
        role VARCHAR(10) CHECK (role IN ('lister', 'viewer')),
        language VARCHAR(5) DEFAULT 'en',
        balance DECIMAL(10,2) DEFAULT 0
    );
    """)
    
    conn.commit()
    cur.close()
    conn.close()

create_tables()  # Runs on startup
