from flask import Blueprint

sports = Blueprint('sports', __name__, url_prefix="/api/sportsbetting")


@sports.route('/create', methods=['POST'])
def createOdds():
    return "create odds"


@sports.route('/read', methods=['GET'])
def readOdds():
    return "read odds"


@sports.route('/update', methods=['PUT'])
def updateOdds():
    return "update odds"


@sports.route('/delete', methods=['DELETE'])
def deleteOdds():
    return "delete odds"
