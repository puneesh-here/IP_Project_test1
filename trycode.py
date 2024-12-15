import sqlite3
import csv
import matplotlib.pyplot as plt

# Create the database and table
def create_database():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            genre TEXT,
            rating REAL
        )
    ''')
    conn.commit()
    conn.close()

# Add sample books to the database
def add_sample_books():
    sample_books = [
        ('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 4.5),
        ('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 4.8),
        ('1984', 'George Orwell', 'Dystopian', 4.7),
        ('Brave New World', 'Aldous Huxley', 'Dystopian', 4.6),
        ('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 4.0),
        ('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 4.8),
        ('Harry Potter and the Sorcerer\'s Stone', 'J.K. Rowling', 'Fantasy', 4.9),
        ('The Da Vinci Code', 'Dan Brown', 'Mystery', 4.2),
        ('Gone Girl', 'Gillian Flynn', 'Mystery', 4.1),
        ('The Alchemist', 'Paulo Coelho', 'Adventure', 4.5),
        ('Life of Pi', 'Yann Martel', 'Adventure', 4.6),
        ('The Road', 'Cormac McCarthy', 'Post-Apocalyptic', 4.3),
        ('Fahrenheit 451', 'Ray Bradbury', 'Dystopian', 4.4),
        ('The Fault in Our Stars', 'John Green', 'Romance', 4.5),
        ('Pride and Prejudice', 'Jane Austen', 'Romance', 4.7),
        ('The Shining', 'Stephen King', 'Horror', 4.5),
        ('It', 'Stephen King', 'Horror', 4.4),
        ('The Picture of Dorian Gray', 'Oscar Wilde', 'Classic', 4.3),
        ('Moby Dick', 'Herman Melville', 'Classic', 4.2),
        ('War and Peace', 'Leo Tolstoy', 'Classic', 4.5),
        ('The Brothers Karamazov', 'Fyodor Dostoevsky', 'Classic', 4.6)
    ]

    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO books (title, author, genre, rating) VALUES (?, ?, ?, ?)', sample_books)
    conn.commit()
    conn.close()

# CRUD Functions
def add_book(title, author, genre, rating):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author, genre, rating) VALUES (?, ?, ?, ?)', 
                   (title, author, genre, rating))
    conn.commit()
    conn.close()
    print(f'Book "{title}" added successfully!')

def get_books():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

def update_book(book_id, title, author, genre, rating):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE books SET title=?, author=?, genre=?, rating=? WHERE id=?', 
                   (title, author, genre, rating, book_id))
    conn.commit()
    conn.close()
    print(f'Book ID {book_id} updated successfully!')

def delete_book(book_id):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id=?', (book_id,))
    conn.commit()
    conn.close()
    print(f'Book ID {book_id} deleted successfully!')

def recommend_books(genre):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books WHERE genre = ?', (genre,))
    recommendations = cursor.fetchall()
    conn.close()
    return recommendations

def visualize_books(books):
    genres = {}
    for book in books:
        genre = book[3]
        if genre in genres:
            genres[genre] += 1
        
