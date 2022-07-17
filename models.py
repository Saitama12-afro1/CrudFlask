from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
    
association_book_author = db.Table('association_book_author', db.Model.metadata,
                                   db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
                                   db.Column('author_id', db.Integer, db.ForeignKey('author.id'))
                                   )

class Books(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    
    
    def __init__(self,title):
        self.title = title
    
    def __repr__(self) -> str:
        return f" {self.title}" 

class Author(db.Model):
    __tablename__ ='author'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False, unique = True)
    books = db.relationship("Books", secondary=association_book_author, backref='authors')
    
    def __init__(self,author):
        self.author = author
    def __repr__(self) -> str:
        return f" {self.author}" 