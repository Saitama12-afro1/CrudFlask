from models import Book
print(Book)
print(Book.query.get(1))
# a = Book.query.order_by(Book.id_book)
# print(a.title)