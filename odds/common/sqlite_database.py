import os
import sys
import sqlite3


class SqliteDatabse:
    """Sqlite Database Class"""
    _instance = None

    def __init__(self, database_file: str) -> None:
        """
        Sqlite Database Class initialization.

        Params:
            database_file (str)

        Returns:
            None

        >>> SqliteDatabase(":memory:")
        """
        self.database_file = database_file

    def _initializeDatabase(self, sql_file: str, database_name: str):
        """
        Initializes a database to be used.

        Params:
            sql_file (`str`): sql file having database setup statements
            database_name (`str`): name of the database to be created

        Returns:
            `True` if successful else `False`

        Exits:
            sys.exit(1): if sql_file path does not exist.

        >>> _initializeDatabase("./schema.sql", ":memory:")
        """
        if not self._filePathExists(sql_file):
            print("Failed to initiate database...")
            sys.exit(1)
        try:
            sql_statement = self._readFile(sql_file)
            conn = sqlite3.connect(database_name)
            cursor = conn.cursor()
            cursor.executescript(sql_statement)
            print("Database initiated...")
            return True
        except Exception as err:
            print("Error: something went wrong")
            print(err)
            return False

    def create(self, location: str, data: dict):
        """
        creates a record in an sqlite3 database.

        Params:
            location(str): table and row id separated by '/'
            data (dict)  : data to be put into the database

        Returns:
            `bool`, `str|None`, `str|None`: Returns `True`, `None`, `str` if successful
            else `False`, `str`, `None` 

        >>> create("Persons/123", {"name":"John","age":30})
        """
        succeeded, reason, nests = self._checkIfTableAndIdProvided(location)
        if not succeeded:
            return succeeded, reason, nests

        col_headers = "id, " + ", ".join(data.keys())
        values = [nests[1], *data.values()]
        value_holders = ("?, " * len(data)) + "?"
        sql = f"INSERT INTO {nests[0]} ({col_headers}) VALUES ({value_holders})"
        try:
            self.database.execute(sql, values)
            return True, None, nests[1]
        except Exception as err:
            return False, err, None

    def read(self, location: str):
        """
        Reads data from an Sqlite3 database

        Params:
            location(`str`): is a "/" separated string containing the table name and id

        Return:
            `bool`, `str|None`, `data: dict|None` -> `True`, `None`, `dict` if data successful
            else `False`, `str`, `None` when unsuccessful

        Exception:
            Exception: Raises an error if the location format is not met.
            Exception: Raises SQL Error if operation is not successful.

        >>> read("users/user_id")
        >>> read("users/8343424")
        """
        nests = location.split('/')
        if len(nests) != 2:
            return Exception("Error: location string should be in the form of 'table_name/id'")

        sql = f"SELECT * FROM {nests[0]} WHERE id = ?"
        data = self.database.execute(sql, [nests[1]])
        try:
            return True, None, list(data)
        except Exception as err:
            return False, str(err)

    def update(self, location: str, data: dict):
        """
        Update data in sqlite3 database

        Returns:
            `bool`, `str|None`, `str|None`: Returns `True`, `None`, `str` if successful
            else returns `bool`, `str`, `None` if unsuccessful

            >>> succeeded, reason, data

        Example:
            >>> update("Persons/123", {"name":"John","age":30})
        """
        succeeded, reason, nests = self._checkIfTableAndIdProvided(location)
        if not succeeded:
            return succeeded, reason, nests

        set_values = self._extractUpdateData(data)

        values = [*data.values(), nests[1]]
        sql = f"UPDATE {nests[0]} SET {set_values} WHERE id = ?"

        try:
            self.database.execute(sql, values)
            return True, None, nests[1]
        except Exception as err:
            return False, err, None

    def delete(self, location: str):
        """
        Deletes row of given ID in Sqlite3

        Returns:
            `bool`, `str|None`, `str|None`: Returns `True`, `None`, `str` if successful
            else returns `False`, `str`, `None`
            
        Examples:
            >>> delete("Persons/123")
        """
        succeeded, reason, nests = self._checkIfTableAndIdProvided(location)
        if not succeeded:
            return succeeded, reason, nests

        values = [nests[1]]
        sql = f"DELETE FROM {nests[0]} WHERE id = ?"

        try:
            self.database.execute(sql, values)
            return True, None, nests[1]
        except Exception as err:
            return False, err, None

    def setUp(self):
        try:
            self.database = sqlite3.connect(self.database_file)
            print('connected to database')
        except Exception as err:
            print('failed to connect to database')
            print(err)

    @staticmethod
    def _extractUpdateData(data: dict):
        string = (" = ?, ").join(data.keys()) + " = ?"
        return string

    @staticmethod
    def _checkIfTableAndIdProvided(location):
        nests = location.split('/')
        if len(nests) != 2:
            return False, Exception("Error: location string should be in the form of 'table_name/id'"), None
        return True, None, nests

    @ staticmethod
    def _filePathExists(file_path: str):
        return os.path.exists(file_path)

    @ staticmethod
    def _readFile(file_path: str):
        try:
            with open(file_path) as f:
                return f.read()
        except Exception as err:
            print(err)
            return None

    @ staticmethod
    def getInstance(database_file: str, re_init=False):
        if SqliteDatabse._instance is None or re_init:
            SqliteDatabse._instance = SqliteDatabse(database_file)
        return SqliteDatabse._instance