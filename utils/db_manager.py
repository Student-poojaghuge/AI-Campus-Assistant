import sqlite3

DATABASE_NAME = "database/users.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'student'
        )
    """)

    conn.commit()
    conn.close()


# Insert New User
def add_user(full_name, email, password, role="student"):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users(full_name, email, password, role)
        VALUES (?, ?, ?, ?)
    """, (full_name, email, password, role))

    conn.commit()
    conn.close()


# Check Email Exists
def email_exists(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email=?", (email,))

    user = cursor.fetchone()

    conn.close()

    return user