from src.database import DataBase
from src.sqlite_db import SqlDatabase

test_config = {'db_name': ":memory", "schema": "./tests/test.sql"}
sqlite = SqlDatabase.getInstance(test_config)

db = DataBase.getInstance(sqlite)


class Test_DataBase:
    def test_query(self):
        assert 1 == 2

    def test_readAll(self):
        result = db.readAll('odds')
        assert len(result) == 0
