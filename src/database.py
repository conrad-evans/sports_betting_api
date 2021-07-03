instance = None


class DataBase:

    def __init__(self, provider) -> None:
        self.provider = provider

    def create(self, data):
        return self.provider.create(data)

    def read(self):
        return self.provider.read()

    def update(self, old_data, new_data):
        return self.provider.update(old_data, new_data)

    def delete(self, data):
        return self.provider.delete(data)

    def query(self, query, params=None):
        return self.provider.query(query, params)

    @staticmethod
    def getInstance(provider=None, re_init=False):
        global instance
        if instance is None and re_init:
            return DataBase(provider)
        return instance
