import os
from dotenv import load_dotenv
import logging

# Vérifie si le dossier 'logs' existe, sinon le crée
if not os.path.exists('logs'):
    os.makedirs('logs')


# Configuration de la journalisation : définit le niveau de journalisation et le fichier dans lequel les logs seront enregistrés
logging.basicConfig(filename='logs/app.log', level=logging.INFO)

# Charge les variables d'environnement à partir du fichier .env
load_dotenv()

class Config:
    """Configuration de base - contient les configurations communes à tous les environnements."""
    
    try:
        # Récupération des variables d'environnement nécessaires
        SECRET_KEY = os.environ['SECRET_KEY']
        SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
        
        # Lance une exception si SQLALCHEMY_DATABASE_URI n'est pas défini
        if SQLALCHEMY_DATABASE_URI is None:
            raise RuntimeError("SQLALCHEMY_DATABASE_URI n'est pas défini. Veuillez le définir dans votre fichier .env ou dans les variables d'environnement de votre système.")
        
        JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']
    
    except KeyError as e:
        # Log l'erreur et lance une exception si une variable d'environnement est manquante
        logging.error(f"Variable d'environnement manquante : {str(e)}")
        raise RuntimeError(f"Variable d'environnement manquante : {str(e)}")
    
    # Désactive le suivi des modifications des objets SQLALCHEMY pour économiser la mémoire
    SQLALCHEMY_TRACK_MODIFICATIONS = False  

class DevelopmentConfig(Config):
    """Configuration pour le développement."""
    # Active le mode debug pour le développement
    DEBUG = True
    # Désactive le mode de test
    TESTING = False

class ProductionConfig(Config):
    """Configuration pour la production."""
    # Désactive le mode debug en production
    DEBUG = False
    # Désactive le mode de test en production
    TESTING = False

class TestingConfig(Config):
    """Configuration pour les tests."""
    # Désactive le mode debug pendant les tests
    DEBUG = False
    # Active le mode de test
    TESTING = True
    # Utilise une base de données SQLite en mémoire pour les tests
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
