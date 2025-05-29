from lib.models.customer import Customer
from lib.models.book import Book
from lib.models.purchase import Purchase
from lib.db.schema import create_tables
from datetime import datetime

def seed_customers():
    print("Seeding customers...")
    customers = [
        ("Alice Johnson", "alice@example.com"),
        ("Bob Smith", "bob@example.com"),
        ("Charlie Brown", "charlie@example.com"),
    ]
    created = []
    for name, email in customers:
        c = Customer.create(name, email)
        created.append(c)
        print(f"Created customer: {c.name} (ID: {c.id})")
    return created

def seed_books():
    print("Seeding books...")
    books = [
        ("1984", "George Orwell", 9.99, 15),
        ("To Kill a Mockingbird", "Harper Lee", 12.50, 10),
        ("The Great Gatsby", "F. Scott Fitzgerald", 8.75, 7),
    ]
    created = []
    for title, author, price, stock in books:
        b = Book.create(title, author, price, stock)
        created.append(b)
        print(f"Created book: {b.title} by {b.author} (ID: {b.id})")
    return created

def seed_purchases(customers, books):
    print("Seeding purchases...")
    purchases = [
        (customers[0].id, books[0].id, 2),
        (customers[1].id, books[1].id, 1),
        (customers[2].id, books[2].id, 3),
    ]
    for customer_id, book_id, qty in purchases:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        p = Purchase.create(customer_id, book_id, qty, date)
        print(f"Recorded purchase ID {p.id} for customer {customer_id} of book {book_id}, quantity {qty}")

def main():
    create_tables()
    customers = seed_customers()
    books = seed_books()
    seed_purchases(customers, books)
    print("Seeding complete!")

if __name__ == "__main__":
    main()
