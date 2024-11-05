from ..models.book import Book
from ..extensions import db
from ..schemas import book_schema, books_schema
from flask_jwt_extended import jwt_required
from flask import jsonify, request


class BookController:
    @staticmethod
    @jwt_required()
    def all():
        books = Book.query.all()
        return jsonify(books=books_schema.dump(books), message='Books retrieved successfully!'), 200

    @staticmethod
    @jwt_required()
    def show(book_id):
        book = Book.query.get_or_404(book_id)
        return jsonify(book=book_schema.dump(book), message='Book retrieved successfully!'), 200

    @staticmethod
    @jwt_required()
    def create():
        data = request.get_json()
        errors = book_schema.validate(data)
        if errors:
            return jsonify(errors), 400

        book = Book(**data)
        db.session.add(book)
        db.session.commit()

        return jsonify(book=book_schema.dump(book), message='Book created successfully!'), 201

    @staticmethod
    @jwt_required()
    def update(book_id):
        data = request.get_json()
        book = Book.query.get_or_404(book_id)
        book.title = data['title']
        book.author = data['author']
        book.description = data.get('description')
        db.session.commit()
        return jsonify(book=book_schema.dump(book), message='Book updated successfully!')

    @staticmethod
    @jwt_required()
    def delete(book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'}), 204
