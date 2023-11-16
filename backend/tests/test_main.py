def test_root(client):
    res = client.get('/')
    assert res.status_code == 200
    assert res.json() == {
        'version': '1.0.0',
        'documentation v1': 'http://localhost:8000/docs',
        'documentation v2': 'http://localhost:8000/redoc',
        'status': 'online',
    }
