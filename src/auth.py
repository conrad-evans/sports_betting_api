import os
import secrets
from datetime import datetime, timedelta
import jwt


def encodeToken(uid: str = secrets.token_hex(4)):
    """
    Generates a json web token

    Args:
        `uid: (str)` -> user id to be encoded in the token

    Returns:
        `token: (str)` -> decoded token if successful else `None`
    """
    try:
        payload = {
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(days=1),
            'uid': uid
        }
        return jwt.encode(payload=payload, key=os.getenv('tokenKey', 'testkey'), algorithm='HS256')

    except Exception as e:
        print(e)
        return None
