import sys

from requests import request
sys.path.append('C:/Users/User/Desktop/Programm/CrudFlask')

from models import Book, db
from validation_data import validation_data
from app import app



def test_db():
    book = Book("Фауст","Гете")
    
    assert book.title == "Фауст"
    assert book.author == "Гете"
    assert book.title != "Гет"

def test_validation():
    assert validation_data("test", None) == True
    assert validation_data("", None) == False
    assert validation_data("test", "test") == True


class TestResponce():
    def test_home_page_get(self):
        app.testing = True
        with app.test_client() as test_client:
            responce = test_client.get('/')
            assert responce.status_code == 200
            

    def test_home_page_post(self):
        app.testing = True
        with app.test_client() as test_client:
            responce = test_client.post('/')
            assert responce.status_code == 405

    def test_create_page_get(self):
        app.testing = True
        with app.test_client() as test_client:
            responce = test_client.get('/create/')
            assert responce.status_code == 200

    def test_create_page_post(self):
        app.testing = True
        with app.test_client() as test_client:
            responce = test_client.post('/create/')
            assert responce.status_code == 400                          