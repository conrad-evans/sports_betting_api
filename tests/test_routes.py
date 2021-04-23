from src.routes import *
import json


def test_createOdds(client):
    res = client.post('{}/create'.format(api_url), data=dict())
    data = json.loads(res.data)
    assert data['status_code'] == 400
    assert data['error']['league'] == "league is required"


def test_readOdds(client):
    res = client.get('{}/read'.format(api_url))
    data = json.loads(res.data)
    assert data['status_code'] == 200
    assert data["data"] == []


def test_updateOdds(client):
    res = client.put('{}/update'.format(api_url))
    print(res.data)
    assert res.data == b'update odds'


def test_deleteOdds(client):
    # test data
    data = {
        "league": "la liga",
        "home_team": "real madrid",
        "away_team": "barcelona",
        "game_date": "2020-03-28"
    }
    missing_data = {"league": "premier league"}
    res = client.delete('{}/delete'.format(api_url), data=missing_data)
    data = json.loads(res.data)
    assert data['status_code'] == 400
