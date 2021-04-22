import jwt
from src.auth import encodeToken


def test_encodeToken():
    uid = "testuser"
    token = encodeToken(uid)
    decoded_token = jwt.decode(token, 'testkey', algorithms='HS256')
    assert decoded_token['uid'] == uid
    assert isinstance(token, str)

