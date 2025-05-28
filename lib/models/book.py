from lib.db.connection import get_connection

class Book:
    def __init__(self, id, title, author, price, stock):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    @classmethod
    def create(cls, title, author, price, stock):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO books (title, author, price, stock) VALUES (?, ?, ?, ?)",
            (title, author, price, stock)
        )
        conn.commit()
        return cls(cursor.lastrowid, title, author, price, stock)

    @classmethod
    def find_by_title(cls, title):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
        row = cursor.fetchone()
        if row:
            return cls(row["id"], row["title"], row["author"], row["price"], row["stock"])
        return None

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        return [cls(row["id"], row["title"], row["author"], row["price"], row["stock"]) for row in rows]
