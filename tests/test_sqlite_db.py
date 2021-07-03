from src.queries import CREATE_ODDS, READ_ALL_ODDS
from src.database import DataBase
from src.sqlite_db import SqlDatabase

test_config = {'db_name': ':memory:', 'schema': './tests/test.sql'}
sql = SqlDatabase.getInstance(config=test_config, re_init=True)
db = DataBase.getInstance(provider=sql, re_init=True)


class Test_SqlDatabase:
    def test_query(self):
        # prepare
        data = ['la liga', 'madrid', 'barcelona', 2.30, 2.50, 3, '2021-07-03']
        data_two = ['premier league', 'chelsea',
                    'arsenal', 1.5, 2.95, 4, '2021-05-03']

        # before data inserted
        result_one = db.query(READ_ALL_ODDS)

        # insert data into db
        db.query(CREATE_ODDS, data)
        db.query(CREATE_ODDS, data_two)

        # query db
        result_two = db.query(READ_ALL_ODDS)

        # assertions
        assert len(list(result_one)) == 0
        assert len(list(result_two)) == 2
        results = list(result_two)
        assert list(db.query(READ_ALL_ODDS))[0] == tuple(
            [1, 'la liga', 'madrid', 'barcelona', 2.30, 2.50, 3.0, '2021-07-03'])
