from flask import jsonify, request
from ..models.user import User
from ..extensions import db
from ..schemas import user_output_schema, user_input_schema
from flask_login import logout_user, current_user
from flask_jwt_extended import create_access_token, jwt_required


class UserController:
    @staticmethod
    def register():
        data = request.get_json()
        username = data['username']
        password = data['password']

        errors = user_input_schema.validate(data)
        if errors:
            return jsonify(errors), 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'message': 'Username already exists!'}), 400

        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        access_token = create_access_token(identity=user.id)
        result = user_output_schema.dump(user)
        return jsonify(user=result, access_token=access_token, message='Register successful!'), 201

    @staticmethod
    def login():
        data = request.get_json()
        username = data['username']
        password = data['password']

        errors = user_input_schema.validate(data)
        if errors:
            return jsonify(errors), 400

        user = User.query.filter_by(username=username).first()
        result = user_output_schema.dump(user)
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id)
            return jsonify(user=result, access_token=access_token, message='Login successful!'), 200

        return jsonify({'message': 'Invalid username or password!'}), 400

    @ staticmethod
    @ jwt_required
    def logout():
        logout_user()
        return jsonify({'message': 'Logged out successfully!'}), 200
