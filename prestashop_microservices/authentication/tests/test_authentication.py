import pytest
from authentication.models import User, db
from authentication.app import app
from authentication import routes



@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_user_creation(client):
    response = client.post('/register', json={'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 201
    user = User.query.filter_by(username='testuser').first()
    assert user is not None
    assert user.check_password('testpassword')

def test_user_login(client):
    client.post('/register', json={'username': 'testuser', 'password': 'testpassword'})
    response = client.post('/login', json={'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 200
    assert 'access_token' in response.get_json()
