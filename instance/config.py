from flask_sqlalchemy import SQLAlchemy

class Config(object):
    Debug = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:danila2001@localhost:5432/crud'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'True'
    