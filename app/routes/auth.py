from flask import Blueprint, request, jsonify
# from ..models import User, db
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="User registered successfully"), 201


@bp.route('/login', methods=['POST'])
def login():
    # Implement login logic here
    pass


@bp.route('/logout', methods=['POST'])
def logout():
    # Implement login logic here
    pass
