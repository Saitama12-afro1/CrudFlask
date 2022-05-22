from models import db, Book

def upg_book(book:Book, title, author):
    book.author = author
    book.title = title
    db.session.coomit()