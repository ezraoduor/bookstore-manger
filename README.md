# Bookstore Management System (CLI + SQLAlchemy ORM)

A command-line application for managing a bookstore. This system allows you to manage customers, books, and purchases using SQLAlchemy ORM and a SQLite database. Built as a Phase 3 project for Moringa School's Software Development curriculum.

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

## 🛠 Technologies Used

- Python 3
- SQLAlchemy ORM
- SQLite3
- Pipenv for environment and dependency management
- Command-line interface (CLI)

---

## 📁 Project Structure

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

## How to Run

### 1. Clone the repository

git clone https://github.com/ezraoduor/bookstore-manger.git
cd bookstore-manger

### 2. Set up the environment with Pipenv

pipenv install
pipenv shell

### 3. Seed the database

python seed.py

### 4. Run the CLI application

python cli.py

---

## Author

Ezra Oduor
