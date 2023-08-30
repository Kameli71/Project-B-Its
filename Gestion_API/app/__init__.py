from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from .views import *

if __name__ == "__main__":
    app.run()

# print(app.config.SQLALCHEMY_DATABASE_URI)
