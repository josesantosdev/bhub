import pytest

from app import create_app

import json


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app
    
@pytest.fixture()
def client(app):
    return app.test_client()

def test_create_costumer(client):
    payload = json.dumps({
        "razao_social": "jose santos",
        "telefone": 31991458907,
        "endereco": "bandolin 13",
        "faturamento_declarado": 10000
    })
    
    
    header = {"Content-Type": "application/json"}
    response = client.post(
        "http://127.0.0.1:5000/api/v1/clientes/cadastrar",
        data=payload,
        headers=header)

    assert response.status_code == 201


def test_get_costumer(client):
    response = client.get('http://127.0.0.1:5000/api/v1/clientes/consultar')
    data = json.loads(response.data.decode('utf-8'))
    assert type(data) == list
    assert response.status_code == 200

def test_get_costumer_by_id(client):
    response = client.get('http://127.0.0.1:5000/api/v1/clientes/consultar/1')
    data = json.loads(response.data.decode('utf-8'))
    assert type(data) == dict
    assert response.status_code == 200

def test_update_costumer(client):
    payload = json.dumps({
        "razao_social": "jose carlos santos",
        "telefone": 31991458907,
        "endereco": "bandolin 13",
        "faturamento_declarado": 10000
    })

    header = {"Content-Type": "application/json"}
    response = client.put(
        "http://127.0.0.1:5000/api/v1/clientes/atualizar/1",
        data=payload,
        headers=header)

    assert response.status_code == 201

def test_delete_costumer(client):
    response = client.delete('http://127.0.0.1:5000/api/v1/clientes/deletar/1')
    assert response.status_code == 201