from lib.models.customer import Customer
from lib.models.book import Book
from lib.models.purchase import Purchase
from datetime import datetime

def main_menu():
    print("\n=== Bookstore Management System ===")
    print("1. Add Customer")
    print("2. Add Book")
    print("3. Record Purchase")
    print("4. List All Customers")
    print("5. List All Books")
    print("6. List Purchases by Customer")
    print("7. Exit")

def add_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    customer = Customer.create(name, email)
    print(f"Customer added with ID {customer.id}")

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    price = float(input("Enter book price: "))
    stock = int(input("Enter stock quantity: "))
    book = Book.create(title, author, price, stock)
    print(f"Book added with ID {book.id}")

def record_purchase():
    customer_name = input("Enter customer name: ")
    customer = Customer.find_by_name(customer_name)
    if not customer:
        print("Customer not found. Please add the customer first.")
        return
    
    book_title = input("Enter book title: ")
    book = Book.find_by_title(book_title)
    if not book:
        print("Book not found. Please add the book first.")
        return
    
    quantity = int(input("Enter quantity to purchase: "))
    if quantity > book.stock:
        print(f"Not enough stock! Available: {book.stock}")
        return
    
    
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Purchase.create(customer.id, book.id, quantity, date)

    
    update_book_stock(book, quantity)

    print(f"Purchase recorded for {quantity} copies of '{book.title}' by {customer.name}.")

def update_book_stock(book, quantity_purchased):
    
    new_stock = book.stock - quantity_purchased
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET stock = ? WHERE id = ?", (new_stock, book.id))
    conn.commit()
    conn.close()

def list_customers():
    customers = Customer.all()
    print("\nCustomers:")
    for c in customers:
        print(f"ID: {c.id} | Name: {c.name} | Email: {c.email}")

def list_books():
    books = Book.all()
    print("\nBooks:")
    for b in books:
        print(f"ID: {b.id} | Title: {b.title} | Author: {b.author} | Price: ${b.price:.2f} | Stock: {b.stock}")

def list_purchases_by_customer():
    customer_name = input("Enter customer name: ")
    customer = Customer.find_by_name(customer_name)
    if not customer:
        print("Customer not found.")
        return
    
    purchases = Purchase.find_by_customer(customer.id)
    if not purchases:
        print(f"No purchases found for {customer.name}.")
        return

    print(f"\nPurchases by {customer.name}:")
    for p in purchases:
        book = Book.find_by_title(p.book_id)
        print(f"Purchase ID: {p.id} | Book ID: {p.book_id} | Quantity: {p.quantity} | Date: {p.date}")

def main():
    while True:
        main_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_customer()
        elif choice == "2":
            add_book()
        elif choice == "3":
            record_purchase()
        elif choice == "4":
            list_customers()
        elif choice == "5":
            list_books()
        elif choice == "6":
            list_purchases_by_customer()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
