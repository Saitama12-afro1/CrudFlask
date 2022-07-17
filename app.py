from flask_migrate import  Migrate
from flask import Flask
from instance.config import Config
from models import db
from flask import render_template, request, redirect, abort
from models import  Books, Author, association_book_author
from add_book import add_book
from validation_data import validation_data
from serializing import MyShema
from BookAuthor import BookAuthor, ListAuthorBook

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.before_first_request
def create_table():
    db.create_all()    

@app.route('/')
def index():
    author = Author.query.all()
    list_author_book = ListAuthorBook()
    a = list_author_book.all_list_add(author)
    shema = MyShema()
    return render_template("index.html",books=a, shema = shema)


@app.route('/getAuthor', methods=["POST","GET"])
def get_author():
    all_author_books = []
    shema = MyShema()
    if request.method == "POST":
        author = request.form['author']
        a = validation_data(author, None)
        if a == False:
            abort(500, description = ["getAuthor_error"])
        all_author_books =  Author.query.filter_by(author = author).all()
        list_author_book = ListAuthorBook()
        all_author_books = list_author_book.all_list_add(all_author_books)
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
        book =  Books.query.filter_by(title = title).all()
        list_author_book = ListAuthorBook()
        book = list_author_book.all_list_add_book(book)

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


@app.route('/upg/<int:id>/<int:id_a>', methods = ["POST", "GET"])
def upg(id, id_a):
    book = Books.query.get(id)
    auth = Author.query.get(id_a)
    if request.method == "POST":
        title = request.form['title']
        author = request.form['author']
        if validation_data(author, title) == False:
            abort(500, description = ["upd_error",id])
        book.title = title
        auth.author = author
        db.session.commit()
    return render_template("book_upd.html", book=book, author=auth)


@app.route('/del/<int:id>/<int:id_a>')
def delite(id, id_a):
    book = Books.query.get_or_404(id)
    author = Author.query.get(id_a)
    print(len(author.books))
    try:
        print(11111111)
        db.session.delete(book)
        if len(author.books) == 1:
            db.session.delete(author)
        db.session.commit()
        return redirect("/")
    except:
        print(22222222)
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