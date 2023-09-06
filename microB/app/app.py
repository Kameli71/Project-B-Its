from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
from prestashop1 import fetch_product
from models import Order, db, app
           
@app.route('/')
def hello():
    return "<h1>HELLO</h1>"

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity')
    stock_availables = request.json.get('stock_availables')
    
    product_data = fetch_product(product_id)
    if not product_data:
        return jsonify({"error": "Failed to fetch product info from PrestaShop"}), 500
    product_data = fetch_product(product_id)
    
    if not product_data:
        return jsonify({"error": "Failed to fetch product info from PrestaShop"}), 500

    available_quantity = product_data.get('stock_availables', {}).get('quantity', {}).get('product_id', {"1"})
    available_quantity = int()
    if quantity > available_quantity:
        return jsonify({"error": "Requested quantity not available"}), 400
    
    order = Order(product_id=product_id, quantity=quantity, stock_availables=stock_availables)
    db.session.add(order)
    db.session.commit()

    return jsonify({"message": "Added to cart successfully", "order_id": order.id}), 201

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500

app.run()