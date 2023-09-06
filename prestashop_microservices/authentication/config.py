import os

# Classe de configuration
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')  # Clé secrète pour Flask
    SQLALCHEMY_DATABASE_URI = 'sqlite:///auth.db'  # URI de la base de données
    #JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')  # Clé secrète pour JWT
    JWT_SECRET_KEY = 'your_jwt_secret_key'

    
    #app.Config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
