from flask import Flask


class SportsBetting:
    _instance = None

    def __init__(self) -> None:
        self.flask_app = Flask(__name__)

    def setEndpoints(self):
        self.flask_app.add_url_rule(
            "/create", methods=["GET"], view_func=self.createOdds
        )
        self.flask_app.add_url_rule("/read", methods=["GET"], view_func=self.readOdds)
        self.flask_app.add_url_rule(
            "/update", methods=["GET"], view_func=self.updateOdds
        )
        self.flask_app.add_url_rule(
            "/delete", methods=["GET"], view_func=self.deleteOdds
        )
        self.flask_app.add_url_rule("/", methods=["GET"], view_func=self.getApp)

    def createOdds(self):
        return "CREATING ODDS"

    def readOdds(self):
        return "READING ODDS"

    def updateOdds(self):
        return "UPDATING ODDS"

    def deleteOdds(self):
        return "DELETING ODDS"

    @staticmethod
    def getInstance(re_init=False):
        if SportsBetting._instance is None or re_init:
            SportsBetting._instance = SportsBetting()
        return SportsBetting._instance
