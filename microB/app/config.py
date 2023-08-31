import os
from flask import Flask
from decouple import config

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

PRESTASHOP_API_URL = config('API_URL')
PRESTASHOP_API_KEY = config('API_KEY')