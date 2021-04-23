import json
from typing import Dict


def jsonResponse(status_code: int = 200, data: Dict = None, error: Dict = None) -> Dict:
    """
    coverts dictionary obj into json
    Args:
        `status_code (int)` -> default is 200
        `data (dict)` -> dictionary obj of the data
        `error (dict)` -> dictionary obj of error being converted
    """
    res = {"status_code": status_code}
    if data is None:
        return json.dumps({**res, **{"error": error}})
    return json.dumps({**res, **{"data": data}})
