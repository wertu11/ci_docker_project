import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    """Тест 1: Главная страница возвращает 200"""
    response = client.get('/')
    assert response.status_code == 200

def test_home_content(client):
    """Тест 2: Главная страница содержит ожидаемую строку"""
    response = client.get('/')
    assert response.data == b'Hello, Docker CI/CD!'

def test_health_endpoint(client):
    """Тест 3: Эндпоинт /health возвращает JSON со статусом ok"""
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'ok'
