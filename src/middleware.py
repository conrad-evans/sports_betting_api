import os
from functools import wraps
import jwt
from flask import request
from src.response import jsonResponse


def tokenRequired(func):
    """
    checks for token and decodes it

    Args:
        `func: (function)` -> function which needs token validated before access

    Returns:
        `function`
    """
    @wraps(func)
    def decoratedFunc(*args, **kwargs):
        token = request.headers.get("x-auth-token", None)
        if token is None:
            return jsonResponse(status_code=401, error={"message": "token required"})

        try:
            decoded_token = jwt.decode(
                jwt=token, key=os.getenv("tokenKey"), algorithms='HS256')
            uid = decoded_token["uid"]
        except Exception as e:
            print(e)
            return jsonResponse(status_code=500, error={"message": "something went wrong try again"})

        return func(*args, **kwargs, uid=uid)
    return decoratedFunc
