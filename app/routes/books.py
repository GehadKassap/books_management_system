from flask import Blueprint, request, jsonify
from ..models.book import Book, db
from ..schemas import book_schema

bp = Blueprint('book', __name__, url_prefix='/books')


@bp.route('/', methods=['GET'])
def get_books():
    books = Book.query.all()
    return book_schema.jsonify(books), 200


@bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict())


@bp.route('/', methods=['POST'])
def add_book():
    data = request.get_json()
    errors = book_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    book = Book(**data)
    db.session.add(book)
    db.session.commit()

    return book_schema.jsonify(book), 201


@bp.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = Book.query.get_or_404(book_id)
    book.title = data['title']
    book.author = data['author']
    book.description = data.get('description')
    db.session.commit()
    return jsonify(book.to_dict())


@bp.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify(message="Book deleted"), 204
