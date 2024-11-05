from flask import Blueprint
from ..controllers.user_controller import UserController

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    return UserController.register()


@bp.route('/login', methods=['POST'])
def login():
    return UserController.login()


@bp.route('/logout', methods=['POST'])
def logout():
    return UserController.logout()


@bp.route('/me', methods=['GET'])
def get_current_user():
    return UserController.get_current_user()
