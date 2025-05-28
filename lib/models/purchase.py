from lib.db.connection import get_connection

class Purchase:
    def __init__(self, id, customer_id, book_id, quantity, date):
        self.id = id
        self.customer_id = customer_id
        self.book_id = book_id
        self.quantity = quantity
        self.date = date

    @classmethod
    def create(cls, customer_id, book_id, quantity, date):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO purchases (customer_id, book_id, quantity, date)
            VALUES (?, ?, ?, ?)
        """, (customer_id, book_id, quantity, date))
        conn.commit()
        return cls(cursor.lastrowid, customer_id, book_id, quantity, date)

    @classmethod
    def find_by_customer(cls, customer_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM purchases WHERE customer_id = ?", (customer_id,))
        rows = cursor.fetchall()
        return [cls(row["id"], row["customer_id"], row["book_id"], row["quantity"], row["date"]) for row in rows]

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM purchases")
        rows = cursor.fetchall()
        return [cls(row["id"], row["customer_id"], row["book_id"], row["quantity"], row["date"]) for row in rows]

    def __repr__(self):
        return f"<Purchase id={self.id}, customer_id={self.customer_id}, book_id={self.book_id}, quantity={self.quantity}, date={self.date}>"
