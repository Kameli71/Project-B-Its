import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'votre_clé_secrète_ici'  # Clé secrète pour les sessions
    SQLALCHEMY_DATABASE_URI = 'sqlite:///products.db'  # URI de la base de données SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Désactivez le suivi des modifications pour éviter les avertissements
    SQLALCHEMY_ECHO = False  # Désactivez l'affichage des requêtes SQL pour améliorer les performances
    # PRESTASHOP_API_URL = os.environ.get('PRESTASHOP_API_URL')  # URL de l'API PrestaShop (commenté car non utilisé pour le moment)
    # PRESTASHOP_API_KEY = os.environ.get('PRESTASHOP_API_KEY')  # Clé API de PrestaShop (commenté car non utilisé pour le moment)
