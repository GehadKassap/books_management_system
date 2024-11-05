from flask import Blueprint, jsonify

bp = Blueprint('public', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def home():
    return jsonify(message="Welcome to main home"), 200
