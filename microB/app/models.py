import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

basedir = os.path.dirname(os.path.abspath(__file__))

db_dir = (basedir, 'database.db')

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    stock_availables = db.Column(db.Integer, nullable=False)
    
    def __init__(self, product_id , quantity, stock_availables):
        self.product_id  = product_id 
        self.quantity = quantity
        self.stock_availables = stock_availables

with app.app_context():
    db.create_all()