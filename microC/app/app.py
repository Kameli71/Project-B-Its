from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS

from models import Order, order
import prestashop

# CORS(app)
app = Flask(__name__)
app.config.from_object('config')
order = SQLAlchemy(app)
cache = Cache(app)

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500

@app.route('/')
def hello():
    return "<h1>HELLO</h1>"

@app.route('/add_to_cart', methods=['POST'])
# @limiter.limit("5 per minute") # Adaptez selon vos besoins
def add_to_cart():
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity')
    
    product_data = prestashop.fetch_product(product_id)
    if not product_data:
        return jsonify({"error": "Failed to fetch product info from PrestaShop"}), 500
    
    # available_quantity = product_data['stock_availables']['1']['quantity']
    print(product_data)
    
    if quantity > available_quantity:
        return jsonify({"error": "Requested quantity not available"}), 400
    
    order.session.add(Order(product_id=product_id, quantity=quantity))
    order.session.commit()

    return jsonify({"message": "Added to cart successfully", "order_id": order.id}), 201

app.run()