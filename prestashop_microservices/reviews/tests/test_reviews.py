import pytest
from reviews.app import app
from reviews.models import Review, db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_review_creation(client):
    response = client.post('/reviews', json={'product_id': 1, 'user_id': 1, 'rating': 5, 'content': 'Great product!'})
    assert response.status_code == 201
    review = Review.query.filter_by(content='Great product!').first()
    assert review is not None
    assert review.rating == 5
