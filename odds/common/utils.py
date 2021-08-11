import secrets
import time


class Utils:
    _instance = None

    def __init__(self) -> None:
        pass

    @staticmethod
    def generateRandomId():
        """
        Generates a random hexicdecimal string

        Returns:
            `str`: string with hexidecimal values

        >>>
        """
        token = secrets.token_hex()
        now = time.time()
        id = now + token
        return id

    @staticmethod
    def getInstance(re_init=False):
        if Utils._instance is None or re_init:
            Utils._instance = Utils()
        return Utils._instance
