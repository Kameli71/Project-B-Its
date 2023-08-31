from flask import request, jsonify  # Importation des fonctions nécessaires de Flask
from flask_jwt_extended import create_access_token, jwt_required  # Outils JWT pour la gestion des tokens
from app import app, db  # Importation de l'application et de la base de données
from models import User  # Importation du modèle utilisateur

@app.route('/')
def index():
    return "Service d'authentification en cours d'exécution"

# Route d'enregistrement
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # Récupération des données envoyées
    user = User(username=data['username'])  # Création d'un nouvel utilisateur
    user.set_password(data['password'])  # Définition du mot de passe
    db.session.add(user)  # Ajout de l'utilisateur à la session
    db.session.commit()  # Enregistrement des modifications
    return jsonify({"message": "User registered successfully!"}), 201  # Retourne un message de succès

# Route de connexion
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Récupération des données envoyées
    user = User.query.filter_by(username=data['username']).first()  # Recherche de l'utilisateur par nom d'utilisateur
    # Vérification du mot de passe et création du token
    if user and user.check_password(data['password']):
        token = create_access_token(identity=user.username)  # Création d'un token d'accès
        return jsonify({"access_token": token}), 200  # Retourne le token
    return jsonify({"message": "Invalid credentials!"}), 401  # Retourne un message d'erreur en cas d'échec

# Route de profil
@app.route('/profile', methods=['GET'])
@jwt_required()  # Nécessite un token valide
def profile():
    current_user = get_jwt_identity()  # Récupère l'identité de l'utilisateur actuel
    user = User.query.filter_by(username=current_user).first()  # Recherche de l'utilisateur par nom d'utilisateur
    return jsonify({"username": user.username}), 200  # Retourne le nom d'utilisateur

