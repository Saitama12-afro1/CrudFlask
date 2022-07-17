from marshmallow import Schema, fields

class MyShema(Schema):
    book = fields.Str()
    author = fields.Str()
