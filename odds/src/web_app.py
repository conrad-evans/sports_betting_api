from src import Odds


def getWebApp():
    app = Odds.getInstance()

    return app.web_app
