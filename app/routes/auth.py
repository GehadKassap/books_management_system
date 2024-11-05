from flask import Blueprint, request, jsonify
from ..models.user import User, db
from flask_login import login_user, logout_user, login_required, current_user
from ..schemas import user_schema

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists!'}), 400

    new_user = User(username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user), 201


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        login_user(user)
        return jsonify({'message': 'Login successful!'}), 200

    return jsonify({'message': 'Invalid username or password!'}), 401


@bp.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully!'}), 200


@bp.route('s/me', methods=['GET'])
@login_required
def get_current_user():
    return jsonify({
        'id': current_user.id,
        'username': current_user.username
    }), 200
