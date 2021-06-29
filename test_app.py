import pytest

from app import app as flask_app
from app import db

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def init_db():
    return db

@pytest.fixture
def client(app):
    return app.test_client()

def test_add(app, client, init_db):
    del app
    init_db.create_all()
    payload = {'num1': 4, 'num2': 7}
    res = client.post('/new', data=payload)
    assert res.status_code == 302
    # expected = '8'
    # assert expected == res.get_data(as_text=True)

def test_main(app, client):
    del app
    res = client.get('/')
    assert res.status_code == 200
    data = res.get_data(as_text=True)
    lines = data.split('\n')
    lines = [line for line in lines if line != '']
    print(lines)
    expected = '4 7 11'
    assert expected == lines[-1]



