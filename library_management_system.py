import sqlite3
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox

def create_database():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        isbn TEXT NOT NULL,
        available INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS BorrowedBooks (
        borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        book_id INTEGER,
        borrow_date TEXT,
        return_date TEXT,
        returned INTEGER,
        FOREIGN KEY (user_id) REFERENCES Users(user_id),
        FOREIGN KEY (book_id) REFERENCES Books(book_id)
    )
    ''')
    
    conn.commit()
    conn.close()

def insert_sample_data():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    
    books = [
        ("To Kill a Mockingbird", "Harper Lee", "978-0061120084", 1),
        ("1984", "George Orwell", "978-0451524935", 1),
        ("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565", 1),
        ("The Catcher in the Rye", "J.D. Salinger", "978-0316769488", 1),
        ("Pride and Prejudice", "Jane Austen", "978-1503290563", 1)
    ]

    cursor.executemany('''
        INSERT INTO Books (title, author, isbn, available)
        VALUES (?, ?, ?, ?)
    ''', books)

    conn.commit()
    conn.close()


create_database()
insert_sample_data()

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f8ff")  

       
        self.main_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.main_frame.pack(pady=20)

        self.user_frame = tk.Frame(self.main_frame, bg="#f0f8ff")

        self.show_main_menu()

    def show_main_menu(self):
        self.clear_frame(self.main_frame)
        tk.Label(self.main_frame, text="Library Management System", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#4b0082").pack(pady=10)

        tk.Button(self.main_frame, text="Register", command=self.show_register_menu, bg="#add8e6", fg="#000080", font=("Helvetica", 12)).pack(pady=10, fill='x')
        tk.Button(self.main_frame, text="Login", command=self.show_login_menu, bg="#add8e6", fg="#000080", font=("Helvetica", 12)).pack(pady=10, fill='x')
        tk.Button(self.main_frame, text="Exit", command=self.root.quit, bg="#ff7f50", fg="#ffffff", font=("Helvetica", 12)).pack(pady=10, fill='x')

    def show_register_menu(self):
        self.clear_frame(self.main_frame)
        tk.Label(self.main_frame, text="Register", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#4b0082").pack(pady=10)

        tk.Label(self.main_frame, text="Username", bg="#f0f8ff").pack(pady=5)
        self.reg_username = tk.Entry(self.main_frame)
        self.reg_username.pack(pady=5)

        tk.Label(self.main_frame, text="Password", bg="#f0f8ff").pack(pady=5)
        self.reg_password = tk.Entry(self.main_frame, show="*")
        self.reg_password.pack(pady=5)

        tk.Button(self.main_frame, text="Register", command=self.register_user, bg="#90ee90", font=("Helvetica", 12)).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.show_main_menu, bg="#ff7f50", fg="#ffffff", font=("Helvetica", 12)).pack(pady=5)

    def show_login_menu(self):
        self.clear_frame(self.main_frame)
        tk.Label(self.main_frame, text="Login", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#4b0082").pack(pady=10)

        tk.Label(self.main_frame, text="Username", bg="#f0f8ff").pack(pady=5)
        self.login_username = tk.Entry(self.main_frame)
        self.login_username.pack(pady=5)

        tk.Label(self.main_frame, text="Password", bg="#f0f8ff").pack(pady=5)
        self.login_password = tk.Entry(self.main_frame, show="*")
        self.login_password.pack(pady=5)

        tk.Button(self.main_frame, text="Login", command=self.login_user, bg="#90ee90", font=("Helvetica", 12)).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.show_main_menu, bg="#ff7f50", fg="#ffffff", font=("Helvetica", 12)).pack(pady=5)

    def show_user_menu(self, user_id):
        self.clear_frame(self.user_frame)
        self.user_id = user_id
        tk.Label(self.user_frame, text="User Menu", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#4b0082").pack(pady=10)

        tk.Button(self.user_frame, text="Display Available Books", command=self.display_books, bg="#add8e6", fg="#000080", font=("Helvetica", 12)).pack(pady=5, fill='x')
        tk.Button(self.user_frame, text="Borrow a Book", command=self.borrow_book, bg="#add8e6", fg="#000080", font=("Helvetica", 12)).pack(pady=5, fill='x')
        tk.Button(self.user_frame, text="Return a Book", command=self.return_book, bg="#add8e6", fg="#000080", font=("Helvetica", 12)).pack(pady=5, fill='x')
        tk.Button(self.user_frame, text="Check Borrowed Books", command=self.check_borrowed_books, bg="#add8e6", fg="#000080", font=("Helvetica", 12)).pack(pady=5, fill='x')
        tk.Button(self.user_frame, text="Logout", command=self.show_main_menu, bg="#ff7f50", fg="#ffffff", font=("Helvetica", 12)).pack(pady=10, fill='x')

        self.user_frame.pack(pady=20)

    def clear_frame(self, frame):
        for widget in self.main_frame.winfo_children():
            widget.pack_forget()
        frame.pack()

    def register_user(self):
        username = self.reg_username.get()
        password = self.reg_password.get()

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful!")
            self.show_main_menu()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")
        finally:
            conn.close()

    def login_user(self):
        username = self.login_username.get()
        password = self.login_password.get()

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM Users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Success", f"Welcome, {username}!")
            self.show_user_menu(user[0])
        else:
            messagebox.showerror("Error", "Invalid username or password.")
        
        conn.close()

    def display_books(self):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books WHERE available = 1")
        available_books = cursor.fetchall()
        
        book_list = "\n".join([f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}" for book in available_books])
        
        if book_list:
            messagebox.showinfo("Available Books", book_list)
        else:
            messagebox.showinfo("Available Books", "No books available at the moment.")
        
        conn.close()

    def borrow_book(self):
        self.clear_frame(self.user_frame)
        tk.Label(self.user_frame, text="Borrow a Book", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#4b0082").pack(pady=10)

        tk.Label(self.user_frame, text="Enter Book ID", bg="#f0f8ff").pack(pady=5)
        self.book_id_entry = tk.Entry(self.user_frame)
        self.book_id_entry.pack(pady=5)

        tk.Button(self.user_frame, text="Borrow", command=self.borrow_book_action, bg="#90ee90", font=("Helvetica", 12)).pack(pady=10)
        tk.Button(self.user_frame, text="Back", command=lambda: self.show_user_menu(self.user_id), bg="#ff7f50", fg="#ffffff", font=("Helvetica", 12)).pack(pady=5)

        self.user_frame.pack(pady=20)

    def borrow_book_action(self):
        book_id = self.book_id_entry.get()
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()

        cursor.execute("SELECT available FROM Books WHERE book_id = ?", (book_id,))
        book = cursor.fetchone()

        if book and book[0] == 1:
            borrow_date = datetime.now().strftime("%Y-%m-%d")
            return_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
            cursor.execute("INSERT INTO BorrowedBooks (user_id, book_id, borrow_date, return_date, returned) VALUES (?, ?, ?, ?, 0)", 
                           (self.user_id, book_id, borrow_date, return_date))
            cursor.execute("UPDATE Books SET available = 0 WHERE book_id = ?", (book_id,))
            conn.commit()
            messagebox.showinfo("Success", f"You have borrowed the book with ID {book_id}. Please return it by {return_date}.")
        else:
            messagebox.showerror("Error", "This book is not available.")

        conn.close()
        self.show_user_menu(self.user_id)

    def return_book(self):
        self.clear_frame(self.user_frame)
        tk.Label(self.user_frame, text="Return a Book", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#4b0082").pack(pady=10)

        tk.Label(self.user_frame, text="Enter Book ID", bg="#f0f8ff").pack(pady=5)
        self.return_book_entry = tk.Entry(self.user_frame)
        self.return_book_entry.pack(pady=5)

        tk.Button(self.user_frame, text="Return", command=self.return_book_action, bg="#90ee90", font=("Helvetica", 12)).pack(pady=10)
        tk.Button(self.user_frame, text="Back", command=lambda: self.show_user_menu(self.user_id), bg="#ff7f50", fg="#ffffff", font=("Helvetica", 12)).pack(pady=5)

        self.user_frame.pack(pady=20)

    def check_borrowed_books(self):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute("SELECT bb.book_id, b.title FROM BorrowedBooks bb JOIN Books b ON bb.book_id = b.book_id WHERE bb.user_id = ? AND bb.returned = 0", (self.user_id,))
        borrowed_books = cursor.fetchall()
        
        if borrowed_books:
            book_list = "\n".join([f"Book ID: {book[0]}, Title: {book[1]}" for book in borrowed_books])
            messagebox.showinfo("Your Borrowed Books", book_list)
        else:
            messagebox.showinfo("Your Borrowed Books", "You have no borrowed books.")

        conn.close()

    def return_book_action(self):
        book_id = self.return_book_entry.get()
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT book_id FROM BorrowedBooks WHERE user_id = ? AND book_id = ? AND returned = 0", (self.user_id, book_id))
        book = cursor.fetchone()

        if book:
            cursor.execute("UPDATE BorrowedBooks SET returned = 1 WHERE book_id = ? AND user_id = ?", (book_id, self.user_id))
            cursor.execute("UPDATE Books SET available = 1 WHERE book_id = ?", (book_id,))
            conn.commit()
            messagebox.showinfo("Success", f"You have successfully returned the book with ID {book_id}.")
        else:
            messagebox.showerror("Error", "You haven't borrowed this book or it has already been returned.")

        conn.close()
        self.show_user_menu(self.user_id)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
