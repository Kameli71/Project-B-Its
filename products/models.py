from .app import db  # Importation de l'objet db depuis app
from datetime import datetime


# Modèle produit
class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)  # ID unique pour chaque produit
    name = db.Column(db.String(80), nullable=False)  # Nom du produit
    price = db.Column(db.Float, nullable=False)  # Prix du produit
    description = db.Column(db.String(200))  # Description du produit
    stock = db.Column(db.Integer, default=0)  # Stock du produit
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'stock': self.stock,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
