from flask import Flask, jsonify, request
from common import Validation, Database, SqliteDatabse

sqlite_database = SqliteDatabse.getInstance(database_name)
database = Database.getInstance(sqlite_database)


class Odds:
    _instance = None

    def __init__(self) -> None:
        self.web_app = Flask(__name__)
        self.setEndpoints()

    def setEndpoints(self):
        self.web_app.add_url_rule(
            "/odds/create", methods=["GET"], view_func=self.createOdds
        )
        self.web_app.add_url_rule(
            "/odds/read", methods=["POST"], view_func=self.readOdds
        )

    def createOdds(self):
        data = request.get_json()
        validation = Validation(data)
        expected_data = ["league", "home_team"]
        validation.checkAll(expected_data)
        if validation.errors():
            return jsonify({"data": validation.errors()})

        if len(data) != len(expected_data):
            # do some sort of mapping to data
            pass


        return jsonify({"data": data})

    def readOdds(self):
        data = request.get_json()
        validation = Validation(data)
        expected_data = ["league", "home_team"]
        validation.checkAll(expected_data)
        if validation.errors():
            return jsonify({"data": validation.errors()})

        if len(data) != len(expected_data):
            # do some sort of mapping to data
            pass


        return jsonify({"data": data})

    @staticmethod
    def getInstance(re_init=False):
        if Odds._instance is None or re_init:
            Odds._instance = Odds()
        return Odds._instance
