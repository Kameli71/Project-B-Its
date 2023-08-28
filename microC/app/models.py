from flask_sqlalchemy import SQLAlchemy

order = SQLAlchemy()

class Order(order.Model):
    id = order.Column(order.Integer, primary_key=True)
    product_id = order.Column(order.Integer, nullable=False)
    quantity = order.Column(order.Integer, nullable=False)
# ... ajoutez d'autres champs si nécessaire
