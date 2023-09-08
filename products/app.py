import sys
print(sys.path)

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config  # Je suppose que config est dans le même répertoire, ajustez si nécessaire
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Initialiser l'application Flask
app = Flask(__name__)
app.config.from_object(Config)

# Initialiser SQLAlchemy pour la gestion de la base de données
db = SQLAlchemy(app)

# Initialiser Flask-Migrate
migrate = Migrate(app, db)

# Importer les routes après l'initialisation de l'app
from routes import *
 # Je suppose que routes est dans le même répertoire, ajustez si nécessaire

# Ajouter un gestionnaire de route pour la racine
@app.route('/')
def home():
    return render_template('index.html')  # Assurez-vous d'avoir un template index.html

# Ajouter un gestionnaire d'erreur pour les erreurs 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500  # Assurez-vous d'avoir un template 500.html

# Créer les tables au démarrage
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run()
