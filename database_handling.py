import sqlite3


DB_NAME = "wedding.db"
conn = sqlite3.connect(DB_NAME)



def init_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS guests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            second_name TEXT NOT NULL,
            first_name TEXT NOT NULL,
            guests INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_guest(second_name, first_name, guests):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO guests (second_name, first_name, guests) VALUES (?, ?, ?)",
        (second_name, first_name, guests)
    )
    conn.commit()
    conn.close()


def get_all_guests():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, second_name, first_name, guests FROM guests")
    rows = cursor.fetchall()
    conn.close()
    return rows


if __name__ == '__main__':
    init_db()