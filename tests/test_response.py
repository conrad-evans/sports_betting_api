import json
from src.response import jsonResponse


def test_jsonResponse():
    # test data
    data = {"token": "testtokencreated"}

    error = {"token": "token required"}
    status_code = 401

    # Assertions
    assert json.dumps({"status_code": 200, "data": data}
                      ) == jsonResponse(data=data)
    assert json.dumps({"status_code": 401, "error": error}
                      ) == jsonResponse(status_code=status_code, error=error)
