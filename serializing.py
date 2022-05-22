from marshmallow import Schema, fields

class MyShema(Schema):
    title = fields.Str()
    author = fields.Str()
