from src.routes import *


def test_createOdds(client):
    res = client.post('{}/create'.format(api_url))
    print(res.data)
    assert res.data == b'create odds'


def test_readOdds(client):
    res = client.get('{}/read'.format(api_url))
    print(res.data)
    assert res.data == b'read odds'


def test_updateOdds(client):
    res = client.put('{}/update'.format(api_url))
    print(res.data)
    assert res.data == b'update odds'


def test_deleteOdds(client):
    res = client.delete('{}/delete'.format(api_url))
    print(res.data)
    assert res.data == b'delete odds'
