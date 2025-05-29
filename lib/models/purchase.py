from lib.db.connection import get_connection

class Purchase:
    def __init__(self, id, customer_id, book_id, quantity, purchase_date):
        self.id = id
        self.customer_id = customer_id
        self.book_id = book_id
        self.quantity = quantity
        self.purchase_date = purchase_date

    @classmethod
    def create(cls, customer_id, book_id, quantity, purchase_date):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO purchases (customer_id, book_id, quantity, purchase_date) VALUES (?, ?, ?, ?)",
            (customer_id, book_id, quantity, purchase_date),
        )
        conn.commit()
        return cls(cursor.lastrowid, customer_id, book_id, quantity, purchase_date)
