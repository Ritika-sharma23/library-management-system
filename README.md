# library-management-system
library management system using python and sql (minor project)

PROJECT REPORT
ON

LIBRARY MANAGEMENT SYSTEM


Submitted By:	
 Ritika Sharma	


University Institute of Computing Chandigarh University, Gharuan, Mohali


 1. Introduction

The Library Management System is a simple, user-friendly software designed to manage library operations. The system allows users to register, log in, borrow, and return books. It also provides an interface to view available books and track borrowed books. This project was built using “Python” and “SQLite” to provide a lightweight, efficient, and portable solution. With a focus on maintaining simplicity, the system operates via the command line, simulating a real-world library with essential functions.

 2. Objective

The primary objectives of  Library Management System are:
- To simplify library operations, such as managing book inventories and tracking users' borrowing and returning activities.
- To offer a basic user management system that allows for secure registration and login for library members.
- To enable library users to borrow books and ensure that the system keeps track of their borrowing status.
- To maintain an accurate book availability status, ensuring that only available books can be borrowed and returned books are updated in the system.
- To provide a foundation for further expansion, including advanced features such as overdue tracking, fines, and more sophisticated search functionalities.

 3. System Requirements
Here are the system requirements:
3.1 Software Requirements:
- Programming Language: Python 3.x
- Database Management System: SQLite3 (comes as part of the Python standard library)
- Python Libraries: 
  -tkinter modify the existing GUI to better organize the components
  - sqlite3 for database operations.
  - datetime for managing borrowing and return dates.

3.2 Hardware Requirements:
- Any machine capable of running Python 3.x (Windows, macOS, or Linux)
- Minimum 512 MB RAM
- Minimum 1 GB disk space for database storage (though SQLite databases typically use far less space)


 4. System Design

The system is built with a clear and modular design, making it easy to maintain and expand. At the core of the system are three database tables: Users, Books, and BorrowedBooks. Each table serves a distinct role, and their interactions drive the functionality of the system.
4.1 Database Structure

The system's database schema consists of the following tables:

1. Users Table
   - The `Users` table contains the information of registered users. Each user is uniquely identified by a `user_id`. 
   - Fields:
     - `user_id`: Unique identifier for each user (Auto-incremented primary key).
     - `username`: Unique username for each user (Indexed and required for login).
     - `password`: User’s password stored as plain text (Note: future improvements can include password hashing for enhanced security).

2. Books Table
   - The `Books` table stores information about the books in the library. Each book is uniquely identified by a `book_id`. The availability of each book is managed by the `available` column.
   - Fields:
     - `book_id`: Unique identifier for each book (Auto-incremented primary key).
     - `title`: Title of the book.
     - `author`: Author of the book.
     - `isbn`: International Standard Book Number for identifying the book.
     - `available`: Indicates whether the book is available for borrowing (1 for available, 0 for borrowed).

3. BorrowedBooks Table
   - The `BorrowedBooks` table tracks the borrowing and return activity for each user. It logs the user who borrowed the book, the date of borrowing, the return date, and whether the book has been returned.
   - Fields:
     - `borrow_id`: Unique identifier for each borrow transaction (Auto-incremented primary key).
     - `user_id`: Foreign key reference to the `Users` table (Links to the user who borrowed the book).
     - `book_id`: Foreign key reference to the `Books` table (Links to the borrowed book).
     - `borrow_date`: Date when the book was borrowed.
     - `return_date`: Due date for the book to be returned (Two weeks after the borrow date).
     - `returned`: Indicates whether the book has been returned (1 for returned, 0 for not returned).

4.2 Functional Components

The Library Management System offers a range of functionalities, including user registration, book management, and borrowing/returning books. These functions are organized into separate modules to ensure clean and maintainable code.

5. Features & Functionalities

5.1 User Management

1. User Registration:
   - A user can register by providing a unique `username` and a `password`. The system stores these credentials in the `Users` table.
   - If the chosen username already exists, the system prompts the user to select a different username.
  
2. User Login:
   - Registered users can log in by entering their username and password. The system validates these credentials by querying the `Users` table.
   - Upon successful login, the system returns the user’s `user_id`, which is used to track their borrowing and returning activities.

5.2 Book Management
1. Displaying Available Books:
   - Users can view all the books that are currently available for borrowing. The system queries the `Books` table for all books where `available = 1`.
   - The available books are displayed with details such as book ID, title, author, and ISBN.

2. Borrowing a Book:
 - Users can borrow books by providing the book ID of the available book. The system updates the `Books` table to mark the book as unavailable (`available = 0`), and a new entry is created in the `BorrowedBooks` table.
   - The system also calculates a due date (two weeks from the borrowing date) and informs the user.

3. Returning a Book:-
 Users can return a book by providing the book ID. The system verifies whether the user has borrowed that book and updates the `BorrowedBooks` and `Books` tables accordingly- Once returned, the book becomes available for other users.
6.CODE FOR THE PROJECT:

 7.Result

8. Potential Enhancements
Password Security: Implement password hashing using libraries like bcrypt to improve security.
Overdue Tracking: Introduce a feature to check for overdue books and alert users when the return date is exceeded.
Fine Calculation: Integrate a system to calculate and manage late fees for overdue books.
Search Functionality: Allow users to search for books by title, author, or ISBN.

8.FUTURE SCOPE AND NEED
1. Enhanced Security and User Management
2. Book Reservation and Queue System
3. Fines and Penalty System for Overdue Books
4. Advanced Book Search and Filtering
5. Digital Library and E-Book Integration
6. Mobile Application Development
7. Graphical User Interface (GUI)
8. Cloud-Based System and Scalability
9. Reporting and Analytics
10. Artificial Intelligence and Machine Learning Integration
11. Offline Mode and Syncing
12. Collaboration with Other Libraries

9.Learning Outcomes
1.	Understanding Database Design and Management.
2.	Python and SQL Integration.
3.	User Authentication and Management.
4.	Building Functional Logic for a Real-World Application.
5.	Handling Dates and Time Operations.
6.	Error Handling and Input Validation.
7.	Structured and Modular Programming.
8.	Commitment to Best Practices.
9.	Understanding Future Scalability.
10.	Project Management and Development Flow.

10. Conclusion
The Library Management System successfully simulates the core functions of a real-world library. It allows users to borrow and return books while keeping track of the books' availability and borrowing history. With room for future improvements such as enhanced security and overdue management, this project lays the foundation for a full-featured library system.
