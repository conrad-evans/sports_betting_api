from common import InMemoryDatabase


class Database:
    _instance = None

    def __init__(self, provider) -> None:
        self.provider = provider or InMemoryDatabase.getInstance()
        self.provider.setUp()

    def create(self, location: str, data: dict):
        return self.provider.create(location, data)

    def read(self, location: str):
        return self.provider.read(location)

    def update(self, location: str, data: dict):
        return self.provider.update(location, data)

    def delete(self, location: str):
        return self.provider.delete(location)

    def closeConnection(self):
        self.provider.closeConnection()

    @staticmethod
    def getInstance(provider=None, re_init: bool = False):
        if Database._instance is None or re_init:
            Database._instance = Database(provider)
        return Database._instance
