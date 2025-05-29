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
            (title, author, price, stock),
        )
        conn.commit()
        return cls(cursor.lastrowid, title, author, price, stock)
