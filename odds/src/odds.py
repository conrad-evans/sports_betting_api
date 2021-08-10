from flask import Flask


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
            "/odds/read", methods=["GET"], view_func=self.readOdds
        )

    def createOdds(self):
        return "Create Odds"

    def readOdds(self):
        return "Read Odds"

    @staticmethod
    def getInstance(re_init=False):
        if Odds._instance is None or re_init:
            Odds._instance = Odds()
        return Odds._instance
