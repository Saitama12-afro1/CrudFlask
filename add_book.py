from models import Author, db, Books
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError


def get_or_create(db,Table, author):
    instance = Table.query.filter_by(author = author).first()
    if instance:
        return instance
    instance = Table(author)
    db.session.add(instance)
    db.session.commit()
    return instance


def add_book(author, title):
    book = Books(title=title)
    auth = get_or_create(db, Author, author)
    db.session.add(book)
    auth.books.append(book)
    db.session.commit()
    db.session.rollback()
    
    # try:
    #     auth = Author(author=author)
    #     db.session.add(auth)         
    #     db.session.add(book)
    #     db.session.commit()
    #     db.session.rollback()

    # except UniqueViolation:
    #     auth = Author.query.filter_by(author = author).first()
    #     auth.books.append(book)
    #     db.session.add(book)
    #     db.session.commit()
        
    # except IntegrityError:
    #     auth = Author.query.filter_by(author = author).first()
    #     auth.books.append(book)
    #     db.session.add(book)
    #     db.session.commit()


