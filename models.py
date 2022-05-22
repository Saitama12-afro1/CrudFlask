from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):# Разбить на два класса автор и книга
    __tablename__ = 'book'
    
    id_book  = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    
    
    def __init__(self,title,author) :
        self.title = title
        self.author = author
    
    
    def __repr__(self) -> str:
        return f" {self.title}  {self.author}" 

