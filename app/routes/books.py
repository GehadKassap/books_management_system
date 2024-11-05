from flask import Blueprint
from ..controllers.book_controller import BookController


bp = Blueprint('book', __name__, url_prefix='/books')


@bp.route('/', methods=['GET'])
def all():
    return BookController.all()


@bp.route('/<int:book_id>', methods=['GET'])
def show(book_id):
    return BookController.show(book_id)


@bp.route('/', methods=['POST'])
def create():
    return BookController.create()


@bp.route('/<int:book_id>', methods=['PUT'])
def update(book_id):
    return BookController.update(book_id)


@bp.route('/<int:book_id>', methods=['DELETE'])
def delete(book_id):
    return BookController.delete(book_id)
