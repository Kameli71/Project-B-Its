import os
from dotenv import load_dotenv
import logging

# Configuration des logs
logging.basicConfig(filename='app.log', level=logging.INFO)

# Chargez les variables d'environnement du fichier .env
load_dotenv()

class Config:
    """Configuration de base - contient les configurations communes à tous les environnements."""
    
    try:
        SECRET_KEY = os.environ['SECRET_KEY']
        SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
        if SQLALCHEMY_DATABASE_URI is None:
            raise RuntimeError("SQLALCHEMY_DATABASE_URI n'est pas défini. Veuillez le définir dans votre fichier .env ou dans les variables d'environnement de votre système.")
        JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']
    except KeyError as e:
        logging.error(f"Variable d'environnement manquante : {str(e)}")
        raise RuntimeError(f"Variable d'environnement manquante : {str(e)}")
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False  

class DevelopmentConfig(Config):
    """Configuration pour le développement."""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Configuration pour la production."""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Configuration pour les tests."""
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
