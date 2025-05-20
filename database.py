import sqlite3

def init_db():
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            encrypted TEXT,
            nonce TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_message(ciphered, nonce):
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages (encrypted, nonce) VALUES (?, ?)", (ciphered, nonce))
    conn.commit()
    conn.close()

def get_all_messages():
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute("SELECT id, encrypted, nonce FROM messages")
    data = c.fetchall()
    conn.close()
    return data
