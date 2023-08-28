import os
from decouple import config

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PRESTASHOP_DB_USER = config('PRESTASHOP_DB_USER')
PRESTASHOP_DB_PASSWD = config('PRESTASHOP_DB_PASSWD')
PRESTASHOP_DB_HOST = config('PRESTASHOP_DB_HOST')
PRESTASHOP_DB_PORT = config('PRESTASHOP_DB_PORT')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + PRESTASHOP_DB_USER + ':' \
    + PRESTASHOP_DB_PASSWD \
    + '@' + PRESTASHOP_DB_HOST + ':' + PRESTASHOP_DB_PORT + '/prestashop'
SQLALCHEMY_TRACK_MODIFICATIONS = False
