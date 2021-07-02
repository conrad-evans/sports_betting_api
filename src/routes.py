from flask import Blueprint, request
from src.validator import Validator
from src.response import jsonResponse
from src.database import DataBase
from src.sqlite_db import SqlDatabase

api_url = "/api/sportsbetting"
sports = Blueprint('sports', __name__, url_prefix=api_url)


@sports.route('/create', methods=['POST'])
# @tokenRequired
def createOdds():
    """
    creates an entry in the db
    """
    data = request.get_json()
    validator = Validator(data)
    validator.checkAll(["league", "home_team", "away_team",
                       "home_team_win_odds", "away_team_win_odds", "draw_odds", "game_date"])
    if validator.errors():
        return jsonResponse(status_code=400, error=validator.errors())

    data_created = db.create(data)
    if data_created is None:
        return jsonResponse(status_code=500, error="something went wrong")

    return jsonResponse(status_code=201, data=data_created)


@sports.route('/read', methods=['GET'])
# @tokenRequired
def readOdds():
    """
    Returns all entries in the database
    """
    data = db.read()
    print(data)
    if data is None:
        return jsonResponse(status_code=500, error="something went wrong")

    return jsonResponse(data=data)


@sports.route('/update', methods=['PUT'])
# @tokenRequired
def updateOdds():
    return "update odds"


@sports.route('/delete', methods=['DELETE'])
# @tokenRequired
def deleteOdds():
    data = request.get_json()
    validation = Validation(data)
    [validation.check("league"), validation.check("home_team"), validation.check(
        "away_team"), validation.check("game_date")]
    if validation.errors():
        return jsonResponse(status_code=400, error=validation.errors())

    data = db.delete()
    if data is None:
        return jsonResponse(status_code=500, error="something went wrong")

    return jsonResponse(data=data)
