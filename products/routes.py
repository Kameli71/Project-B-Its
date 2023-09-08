from flask import request, jsonify  # Importation des fonctions nécessaires de Flask
from app import app, db  # Importation de l'application et de la base de données
from models import Product  # Importation du modèle produit
import requests  # Module pour faire des requêtes HTTP

# Fonction pour récupérer les données depuis l'API PrestaShop
def fetch_from_prestashop(endpoint):
    headers = {
        'Authorization': f'Bearer {app.config["PRESTASHOP_API_KEY"]}'  # Authentification avec la clé API
    }
    response = requests.get(f'{app.config["PRESTASHOP_API_URL"]}/{endpoint}', headers=headers)  # Requête GET
    response.raise_for_status()  # Vérification de la réponse
    return response.json()  # Retourne les données au format JSON

# Route pour synchroniser les produits
@app.route('/sync_products', methods=['GET'])
def sync_products():
    products_data = fetch_from_prestashop('products')  # Récupération des produits depuis PrestaShop
    for product_data in products_data:
        product = Product(
            name=product_data['name'],
            price=product_data['price'],
            description=product_data.get('description', ''),
            stock=product_data.get('stock', 0)
        )
        db.session.add(product)  # Ajout du produit à la session
    db.session.commit()  # Enregistrement des modifications
    return jsonify({"message": "Products synced successfully!"}), 200  # Retourne un message de succès


# Create a product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        price=data['price'],
        description=data.get('description', ''),
        stock=data.get('stock', 0)
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created successfully!", "product": new_product.to_dict()}), 201


#Read a product
@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict()), 200


#Update a product
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = Product.query.get_or_404(id)
    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.description = data.get('description', product.description)
    product.stock = data.get('stock', product.stock)
    db.session.commit()
    return jsonify({"message": "Product updated successfully!", "product": product.to_dict()}), 200

#Delete a product
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully!"}), 200



