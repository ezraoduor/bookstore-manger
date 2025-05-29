# Bookstore Management System (CLI + SQLAlchemy ORM)

A command-line application for managing a bookstore. This system allows you to manage customers, books, and purchases using SQLAlchemy ORM and a SQLite database. Built as a Phase 3 project for Moringa School's Software Development curriculum.

---

### Instalation

## 1. Clone the repository

git clone https://github.com/ezraoduor/bookstore-manger.git
cd bookstore-manger

### 2. Set up the environment with Pipenv
```bash
pipenv install
pipenv shell

```
---
### 3. Seed the database
```
python seed.py
```
### 4. Run the CLI application
```
python cli.py
```
---

## Features

- Add, view, and manage customers
- Add, view, and manage books
- Record purchases of books by customers
- View purchase history per customer or book
- View most popular books and active customers
- Clean and interactive CLI interface
- Uses SQLAlchemy ORM to interact with the database

---

## Technologies Used

- Python 3
- SQLAlchemy ORM
- SQLite3
- Pipenv for environment and dependency management
- Command-line interface (CLI)

---

##  Project Structure

    bookstore/
    │
    ├── cli.py               # Main CLI application
    ├── seed.py              # Populates the database with sample data
    ├── helpers.py           # Helper functions (e.g. printing tables)
    │
    ├── lib/
    │   ├── __init__.py
    │   ├── db/
    │   │   ├── __init__.py
    │   │   └── connection.py   # Database connection setup
    │   ├── models/
    │   │   ├── __init__.py
    │   │   ├── customer.py     # Customer model
    │   │   ├── book.py         # Book model
    │   │   └── purchase.py     # Purchase model

---

### How the Code Works
The Bookstore Management System is a command-line interface (CLI) application that uses SQLAlchemy ORM to interact with a SQLite database. The application consists of three main models:

-Customer: Represents customers who can purchase books.

-Book: Represents books available for sale.

-Purchase: Records purchases linking customers to books with quantities and timestamps.

The program workflow is as follows:

# 1.Database Setup
The seed.py script initializes the database and populates it with sample customers, books, and purchase records.

# 2.CLI Interface
Running cli.py launches an interactive menu-driven CLI. Users can add/view customers and books, record new purchases, and view reports such as purchase history or popular books.

# 3.Data Management with SQLAlchemy
Each model class (Customer, Book, Purchase) uses SQLAlchemy ORM to map Python objects to database tables. CRUD operations are handled via SQLAlchemy’s session management, ensuring database integrity.

# 4.Helper Functions
Helper functions support tasks like nicely printing tables and validating user input to provide a smooth user experience.

# 5.Virtual Environment
Pipenv manages the project’s dependencies and virtual environment, isolating package installations and simplifying setup.



## Author

Ezra Oduor
