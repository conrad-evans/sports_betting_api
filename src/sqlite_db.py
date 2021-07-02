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
            print('first')
            self.conn = sqlite3.connect(config['db_name'])
            print('second')
            self.conn.cursor().executescript(schema)

    def readAll(self, db_name):
        try:
            data = self.conn.execute("""SELECT * FROM {}""".format(db_name))
            self.conn.commit()
            return list(data)
        except Exception as e:
            print(e)
            return None

    def query(self, sql_statement, params=None):
        try:
            if params is None:
                data = self.conn.cursor().execute(sql_statement)
            else:
                params = tuple(params)
                data = self.conn.cursor().execute(sql_statement, params)
            return data
        except Exception as e:
            print(e)
            return None

    def getInstance(config: dict = None, re_init=False):
        global instance
        if instance is None or re_init is True:
            return SqlDatabase(config)
        return instance
