from src.queries import CREATE_ODDS, READ_ALL_ODDS
from src.database import DataBase
from src.sqlite_db import SqlDatabase

test_config = {'db_name': ":memory:", "schema": "./tests/test.sql"}
sqlite = SqlDatabase.getInstance(test_config, re_init=True)

db = DataBase.getInstance(sqlite, re_init=True)


class Test_DataBase:
    def test_query(self):
        # prepare
        data = ['la liga', 'madrid', 'barcelona', 2.30, 2.50, 3, '2021-0703']

        # before data inserted
        result_one = db.query(READ_ALL_ODDS)

        # insert data into db
        db.query(CREATE_ODDS, data)

        # query db
        result_two = db.query(READ_ALL_ODDS)

        # assertions
        assert len(list(result_one)) == 0
        assert len(list(result_two)) == 1
        assert list(db.query(READ_ALL_ODDS)) == [tuple([1, 'la liga', 'madrid', 'barcelona', 2.30, 2.50, 3.0, '2021-0703'])]
