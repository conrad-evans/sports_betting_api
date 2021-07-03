import os
import sqlite3
import sys
instance = None


class SqlDatabase:
    def __init__(self, config: dict = None) -> None:
        self.config = config
        self.setUp()

    def setUp(self):
        if type(self.config) != dict:
            sys.exit(1)
        if self.config.get('db_name'):
            if self.config['db_name'] == ':memory:':
                self._initializeDatabase(self.config)
            elif os.path.exists(self.config['db_name']):
                self.conn = sqlite3.connect(self.config['db_name'])
            else:
                self._initializeDatabase(self.config)

    def _readFile(self, file):
        try:
            with open(file) as f:
                return f.read()
        except Exception as e:
            print(e)
            return None

    def _initializeDatabase(self, config):
        if config.get('schema') is None or not os.path.exists(config['schema']):
            print("schema missing")
            sys.exit(1)
        schema = self._readFile(config['schema'])
        if schema:
            try:
                self.conn = sqlite3.connect(config['db_name'])
                self.conn.cursor().executescript(schema)
            except Exception as e:
                print(e)
                sys.exit(1)

    def query(self, sql_statement, params=None):
        try:
            if params is None:
                data = self.conn.cursor().execute(sql_statement)
            else:
                params = tuple(params)
                print(params)
                data = self.conn.cursor().execute(sql_statement, params)
            return data
        except Exception as e:
            print(e)
            return e

    def getInstance(config: dict = None, re_init=False):
        global instance
        if instance is None or re_init is True:
            return SqlDatabase(config)
        return instance


if __name__ == '__main__':
    test_config = {'db_name': ':memory:', 'schema': './tests/test.sql'}
    sql = SqlDatabase.getInstance(config=test_config, re_init=True)
    data = ["la liga", "madrid", "atletico", 1.95, 2.80, 4.00, "7/3/2021"]
    sql.query("INSERT INTO odds (league, home_team, away_team, home_team_win_odds, away_team_win_odds, draw_odds, game_date) VALUES (?, ?, ?, ?, ?, ?, ?)", params=data)
    print(list(sql.query("SELECT * FROM odds")))

