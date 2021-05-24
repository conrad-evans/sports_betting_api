instance = None


class DataBase:
    def __init__(self, provider) -> None:
        self.provider = provider

    def create(self, provider, data):
        self.provider.create(data)

    def read(self, provider):
        self.provider.read()

    def update(self, provider, old_data, new_data):
        self.provider.update(old_data, new_data)

    def delete(self, provider, data):
        self.provider.delete(data)

    @staticmethod
    def getInstance(provider=None, re_init=False):
        global instance
        if instance is None and re_init is True:
            return DataBase(provider)
        return instance
