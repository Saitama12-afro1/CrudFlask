from models import db, Book


def add_book(author, title):
    book = Book(title=title, author=author)
    db.session.add(book)
    db.session.commit()
    db.session.rollback()