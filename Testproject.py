import sqlite3
from matplotlib import pyplot as plt

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


def add_book(title, author, genre, rating):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author, genre, rating) VALUES (?, ?, ?, ?)', 
                   (title, author, genre, rating))
    conn.commit()
    conn.close()

def get_books():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return books


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
        else:
            genres[genre] = 1

    plt.bar(genres.keys(), genres.values())
    plt.xlabel('Genres')
    plt.ylabel('Number of Books')
    plt.title('Books by Genre')
    plt.xticks(rotation=45)
    plt.show()

import csv

def export_to_csv(filename):
    books = get_books()
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Title', 'Author', 'Genre', 'Rating'])
        writer.writerows(books)



if __name__ == "__main__":
    create_database()
    while True:
        print("1. Add Book")
        print("2. View Books")
        print("3. Recommend Books by Genre")






