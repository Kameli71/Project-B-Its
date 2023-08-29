from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import views

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


# print(app.config.SQLALCHEMY_DATABASE_URI)
