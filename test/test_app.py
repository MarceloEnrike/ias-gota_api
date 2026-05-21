
import sys
import os

# Agregar raíz del proyecto al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_get_marcas():
    client = app.test_client()
    response = client.get("/marcas")
    assert response.status_code == 200


