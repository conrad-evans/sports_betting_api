import json
from typing import Dict


def jsonResponse(status_code: int = 200, data: Dict = None, error: Dict = None) -> Dict:
    res = {"status_code": status_code}
    if data:
        return json.dumps({**res, **{"data": data}})
    return json.dumps({**res, **{"error": error}})
