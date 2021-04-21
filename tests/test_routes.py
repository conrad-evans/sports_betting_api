from src.routes import *

base_url = "/api/sportsbetting"


def test_createOdds(client):
    res = client.post('{}/create'.format(base_url))
    print(res.data)
    assert res.data == b'create odds'


def test_readOdds(client):
    res = client.get('{}/read'.format(base_url))
    print(res.data)
    assert res.data == b'read odds'


def test_updateOdds(client):
    res = client.put('{}/update'.format(base_url))
    print(res.data)
    assert res.data == b'update odds'


def test_deleteOdds(client):
    res = client.delete('{}/delete'.format(base_url))
    print(res.data)
    assert res.data == b'delete odds'
