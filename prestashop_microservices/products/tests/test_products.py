import pytest
from products.app import app
from products.models import Product, db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_product_creation(client):
    response = client.post('/products', json={'name': 'Test Product', 'price': 100.0})
    assert response.status_code == 201
    product = Product.query.filter_by(name='Test Product').first()
    assert product is not None
    assert product.price == 100.0
