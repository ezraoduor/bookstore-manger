from lib.db.connection import get_connection

class Customer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    @classmethod
    def create(cls, name, email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        return cls(cursor.lastrowid, name, email)

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE name = ?", (name,))
        row = cursor.fetchone()
        return cls(row["id"], row["name"], row["email"]) if row else None
