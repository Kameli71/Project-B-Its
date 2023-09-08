from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv


# Charge les variables d'environnement
load_dotenv()
# Affiche le répertoire de travail actuel (utile pour le débogage)
print(os.getcwd())
# Initialise l'application Flask
app = Flask(__name__)

# Importe la classe Config ici
try:
    from config import Config, DevelopmentConfig, ProductionConfig
except ImportError:
    from .config import Config, DevelopmentConfig, ProductionConfig

# Mise à jour de la configuration de l'application en fonction de l'environnement
if os.environ.get('FLASK_ENV') == 'development':
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

# Ceci définira SQLALCHEMY_DATABASE_URI à 'sqlite:///auth.db' si elle n'est pas définie dans les variables d'environnement
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///auth.db')

# Vérifie que toutes les variables d'environnement nécessaires sont définies
required_env_vars = ['SECRET_KEY', 'SQLALCHEMY_DATABASE_URI', 'JWT_SECRET_KEY']
for var in required_env_vars:
    if not os.environ.get(var):
        raise EnvironmentError(f"La variable d'environnement {var} n'est pas définie")

# Initialise SQLAlchemy pour la gestion de la base de données
db = SQLAlchemy(app)

# Initialise JWT pour l'authentification
jwt = JWTManager(app)

try:
    from routes import init_routes
except ImportError:
    from .routes import init_routes

# Initialisation des routes
init_routes()

if __name__ == '__main__':
    with app.app_context():  # Crée un contexte d'application
        db.create_all()  # Crée la base de données si elle n'existe pas
        app.run(host='localhost', port=5010, debug=True)  # Démarre l'application avec l'adresse d'écoute spécifiée
