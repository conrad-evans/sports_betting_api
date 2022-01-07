from flask import Flask, jsonify, request
from common import Validation, Database, SqliteDatabse, Utils


database_name = "odds.db"
sqlite_database = SqliteDatabse.getInstance(database_name)
database = Database.getInstance(sqlite_database)

utils = Utils.getInstance()


class Odds:
    _instance = None
    api = "/odds"
    table = "Odds"

    def __init__(self) -> None:
        self.web_app = Flask(__name__)
        self.setEndpoints()

    def setEndpoints(self):
        self.web_app.add_url_rule(
            f"{Odds.api}/create", methods=["POST"], view_func=self.createOdds
        )
        self.web_app.add_url_rule(
            f"{Odds.api}/read", methods=["GET"], view_func=self.readOdds
        )
        self.web_app.add_url_rule(
            f"{Odds.api}/update", methods=["PUT"], view_func=self.updateOdds
        )
        self.web_app.add_url_rule(
            f"{Odds.api}/delete", methods=["DELETE"], view_func=self.deleteOdds
        )

    def createOdds(self):
        data = request.get_json()
        validation = Validation(data)
        expected_data = [
            "league",
            "home_team",
            "away_team",
            "home_team_win_odds",
            "away_team_win_odds",
            "draw_odds",
            "game_date",
        ]
        validation.checkAll(expected_data)
        if validation.errors():
            return jsonify({"data": validation.errors()})

        if len(data) != len(expected_data):

            def mapData(array: list) -> dict:
                """
                map data of an array to a new dictionary object

                Returns:
                    `dict`: mapped Data

                >>> mapData(["name", "age"], {"name": "doe", "city":"new york", "age": 30})
                >>> {"name": "doe", "age": 30}
                """
                mappedData = dict()
                for item in array:
                    mappedData[item] = data[item]
                return mappedData

            data = mapData(expected_data)

        uid = utils.generateRandomId()
        path = Odds.table + "/" + uid
        succeeded, _, data = database.create(path, data)

        return jsonify({"data": data, "succeeded": succeeded})

    def readOdds(self):
        data = request.get_json()
        validation = Validation(data)
        expected_data = ["id"]
        validation.checkAll(expected_data)
        if validation.errors():
            return jsonify({"data": validation.errors()})

        uid = data[expected_data[0]]
        path = Odds.table + "/" + uid

        succeeded, _, data = database.read(path)

        return jsonify({"data": data, "succeeded": succeeded})

    def updateOdds(self):
        data = request.get_json()
        validation = Validation(data)
        expected_data = [
            "id" "league",
            "home_team",
            "away_team",
            "home_team_win_odds",
            "away_team_win_odds",
            "draw_odds",
            "game_date",
        ]
        validation.checkAll(expected_data)
        if validation.errors():
            return jsonify({"data": validation.errors()})

        uid = data["id"]
        path = Odds.table + "/" + uid
        succeeded, _, data = database.update(path, data)

        return jsonify({"data": data, "succeeded": succeeded})
        pass

    def deleteOdds(self):
        data = request.get_json()
        validation = Validation(data)
        expected_data = ["league", "home_team", "away_team", "game_date"]
        validation.checkAll(expected_data)
        if validation.errors():
            return jsonify({"data": validation.errors()})

        uid = data["id"]
        path = Odds.table + "/" + uid
        succeeded, _, data = database.delete(path)

        return jsonify({"data": data, "succeeded": succeeded})

    @staticmethod
    def getInstance(re_init=False):
        if Odds._instance is None or re_init:
            Odds._instance = Odds()
        return Odds._instance
