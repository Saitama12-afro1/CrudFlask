from email import message
from traceback import print_tb
from flask_migrate import  Migrate
from flask import Flask
from instance.config import Config
from models import db
from flask import render_template, request, redirect, abort, jsonify
from models import Book
from add_book import add_book
from validation_data import validation_data
from serializing import MyShema


app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.before_first_request
def create_table():
    db.create_all()    

@app.route('/')
def index():
    books = Book.query.order_by(Book.author).all()
    a = Book.query.order_by(Book.id_book).all()
    shema = MyShema()
    return render_template("index.html",books=books, shema = shema)


@app.route('/getAuthor', methods=["POST","GET"])
def get_author():
    all_author_books = []
    shema = MyShema()
    if request.method == "POST":
        author = request.form['author']
        a = validation_data(author, None)
        if a == False:
            abort(500, description = ["getAuthor_error"])
        all_author_books =  Book.query.filter_by(author = author).all()
    return render_template('get_author.html', all_author_books = all_author_books, shema= shema)


@app.route('/getBook', methods=["POST","GET"])
def get_book():
    book = []
    shema = MyShema()
    if request.method == "POST":
        title = request.form['title']
        a = validation_data(title, None)    
        if a == False:
            abort(500, description = ["getBook_error"])
        book =  Book.query.filter_by(title = title).all()

    return render_template('get_book.html', book = book, shema= shema)


@app.route('/create/', methods=['post', 'get'])
def create():
    if request.method == "POST":
        author = request.form['author']
        title = request.form['title'] 
        a = validation_data(author, title)
        if a == False:
            abort(500, description = ["create_error"])
        add_book(author=author, title=title)

              
    return render_template("create.html")


@app.route('/upg/<int:id>', methods = ["POST", "GET"])
def upg(id):
    book = Book.query.get(id)
    if request.method == "POST":
        title = request.form['title']
        author = request.form['author']
        if validation_data(author, title) == False:
            abort(500, description = ["upd_error",id])
        book.title = title
        book.author = author
        db.session.commit()
    return render_template("book_upd.html", book=book)


@app.route('/del/<int:id>')
def delite(id):
    book = Book.query.get_or_404(id)
    try:
        db.session.delete(book)
        db.session.commit()
        return redirect("/")
    except:
        db.session.rollback()
        abort(404)
 

@app.errorhandler(500)
def iternal_error(error):
    db.session.rollback()
    return render_template("500er.html", props = error.description), 500


@app.errorhandler(404)
def iternal_error(error):
    db.session.rollback()
    return render_template("404er.html"), 404

    
if __name__ == "__main__":
    app.run(debug=True)