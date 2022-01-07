from src import SportsBetting


def getWebApp():
    web_app = SportsBetting.getInstance()

    return web_app.flask_app
