import secrets


class InMemoryDatabase:
    _instance = None

    def __init__(self) -> None:
        self.database = None

    def setUp(self):
        self.database = dict()

    def create(self, location: str, data: dict):
        id = secrets.token_hex(4)
        data = {**data, **{'id': id}}
        if self.database.get(location) is None:
            self.database[location] = dict()
        self.database[location][id] = data
        return True, None, data

    def read(self):
        pass

    def update(self):
        pass

    def batchCreate(self):
        pass

    def delete(self):
        pass

    def readAll(self):
        pass

    def filterData(self):
        pass

    def readAllKeys(self):
        pass

    def closeConnection(self):
        pass

    @staticmethod
    def getInstance(re_init=False):
        if InMemoryDatabase._instance is None or re_init:
            InMemoryDatabase._instance = InMemoryDatabase()
        return InMemoryDatabase._instance