# Library Management System

## Overview

This is a Library Management System that allows users to view, borrow, and review books. Users can create accounts, log in, deposit money, borrow and return books, and view their borrowing history.

## Features

### Books

- Each book has:
  - Title
  - Description
  - Image
  - Borrowing price
  - User reviews
- Books can be filtered based on categories.

### User

- Users can:
  - Create an account
  - Log in and log out
  - Deposit money to their account
  - Borrow and return books
  - Receive email notifications for successful deposit and book borrowing
  - Review books after borrowing
  - View borrowing history, including borrowing date and amount

### Deployment

The project is deployed on [Render](https://render.com/) or your preferred platform.

## Implementation

The implementation can use either function-based views or class-based views. The choice is yours.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/library-management-system.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```bash
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Open your web browser and go to [http://localhost:8000/](http://localhost:8000/) to access the Library Management System.

## Usage

1. Create a user account.
2. Log in to your account.
3. Deposit money to your account.
4. Browse and borrow books.
5. Return books to receive the borrowed amount.
6. Write reviews for the books you've borrowed.
7. View your borrowing history in your profile.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).
