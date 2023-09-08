from flask import request, jsonify, current_app as app
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from wtforms import Form, StringField, PasswordField, validators
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging

from .app import app
from .app import db
from .models import User  

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=20)])
    password = PasswordField('Password', [validators.DataRequired()])

logging.basicConfig(level=logging.INFO)

limiter = Limiter(app=app, key_func=get_remote_address)

def log_event(event_message):
    logging.info(event_message)

def init_routes():
    @app.route('/reset_password', methods=['POST'])
    def reset_password():
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user:
            token = create_access_token(identity=user.username)
            return jsonify({"access_token": token}), 200
        return jsonify({"message": "Invalid credentials!"}), 401

    @app.route('/login', methods=['POST'])
    @limiter.limit("5 per minute")
    def login():
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            token = create_access_token(identity=user.username)
            return jsonify({"access_token": token}), 200
        return jsonify({"message": "Invalid credentials!"}), 401

    @app.route('/')
    def index():
        return "Service d'authentification en cours d'exécution"

    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        user = User(username=data['username'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User registered successfully!"}), 201

    @app.route('/profile', methods=['GET'])
    @jwt_required()
    def profile():
        current_user = get_jwt_identity()
        user = User.query.filter_by(username=current_user).first()
        return jsonify({"username": user.username}), 200
