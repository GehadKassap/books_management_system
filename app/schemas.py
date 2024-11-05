from marshmallow import Schema, fields, validate
from .models.user import User
from .models.book import Book
from .extensions import db


class UserInputSchema(Schema):
    username = fields.String(required=True, validate=validate.Length(min=1))
    password = fields.String(required=True, validate=validate.Length(min=6))


class UserOutputSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class BookSchema(Schema):
    class Meta:
        model = Book
        load_instance = True

    title = fields.String(required=True, validate=validate.Length(min=1))
    author = fields.String(required=True, validate=validate.Length(min=1))
    description = fields.String(required=False)


user_input_schema = UserInputSchema()
user_output_schema = UserOutputSchema()

book_schema = BookSchema()
books_schema = BookSchema(many=True)
