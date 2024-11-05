# Book Management System

The Book Management System is a web application built with Python and Flask, designed to manage a collection of books. The application supports essential features like user registration, login, and logout, as well as CRUD (Create, Read, Update, Delete) operations for managing book records.

## Features

- **User Authentication**: Register, log in, and log out users securely.
- **Book Management**: Add, edit, view, and delete books in the database.
- **Database Integration**: Uses MySQL for data persistence.
- **Schema Validation**: Validates request and response data with defined schemas.
- **Environment-Based Configuration**: Uses `.env` file for managing sensitive information.
- **Modular Code Structure**: Organized into distinct modules for models, routes, utilities, and more.

## Quick Note

The project contains postman collection with example for response.

## Folder Structure

The project is organized as follows:

```plaintext
book_management_system/
├── app/
│   ├── __init__.py           # Initialize the Flask app and configurations
│   ├── models/             # Define User and Book models
│   │   ├── auth.py           # Define user model
│   │   └── books.py          # Define book model
│   ├── routes/
│   │   ├── __init__.py       # Register routes
│   │   ├── auth.py           # User registration, login, logout
│   │   └── books.py          # Book CRUD operations
│   │   └── public.py          # Main route
│   ├── schemas.py            # Define request and response schemas
│   ├── utils.py              # Helper functions like authentication and password hashing
│   └── config.py             # Configuration settings for Flask
├── migrations/               # Database migration files 
├── tests/                    # Tests for endpoints and models
├── requirements.txt          # List of dependencies
├── .env                      # Environment variables for sensitive information
└── app.py                    # Main app entry point
└── postman collection        #Example for api's
```

## Getting Started 

### Prerequisites

- **Python 3.x**.
- **MySQL**.
- **Flask and other dependencies listed in `requirements.txt`**.


## Installation 

1. Clone the repository:
   1. git clone `https://github.com/GehadKassap/books_management_system.git`.
   2. cd `books_management_system`.

2. Install dependencies:
   - **pip install -r requirements.txt**

3. Set up the database:
   1. Create a MySQL database named `book_management`.
   2. Update the `.env` file with your MySQL credentials.

4. Run migrations:
   - **flask db upgrade**

5. flask run
   - **flask run**

