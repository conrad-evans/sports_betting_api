from os import stat
from flask import Blueprint, request
from src.validator import Validator
from src.response import jsonResponse
from src.database import DataBase
from src.sqlite_db import SqlDatabase
from src.queries import CREATE_ODDS, READ_ALL_ODDS, UPDATE_ODDS, DELETE_ODDS

api_url = "/api/sportsbetting"
sports = Blueprint('sports', __name__, url_prefix=api_url)

sports_betting_db_config = {
    'db_name': './sportsbetting.db',
    'schema': './src/schema.sql'
}

sql = SqlDatabase.getInstance(config=sports_betting_db_config)
db = DataBase.getInstance(provider=sql)


@sports.route('/create', methods=['POST'])
# @tokenRequired
def createOdds():
    """
    creates an entry in the db
    """
    data = request.get_json()

    fields_checked = ["league", "home_team", "away_team",
                      "home_team_win_odds", "away_team_win_odds", "draw_odds", "game_date"]
    validator = Validator(data)
    validator.checkAll(fields_checked)
    if validator.errors():
        return jsonResponse(status_code=400, error=validator.errors())

    data_created = db.query(CREATE_ODDS, params=fields_checked)
    if data_created is None:
        return jsonResponse(status_code=500, error="something went wrong")

    return jsonResponse(status_code=201, data=list(data_created))


@sports.route('/read', methods=['GET'])
# @tokenRequired
def readOdds():
    """
    Returns all entries in the database
    """
    data = db.query(READ_ALL_ODDS)
    print(data)
    if data is None:
        return jsonResponse(status_code=500, error="something went wrong")

    return jsonResponse(data=data)


@sports.route('/update', methods=['PUT'])
# @tokenRequired
def updateOdds():
    data = request.get_json()
    validator = Validator(data)
    validator.checkAll(["league", "home_team", "away_team", "game_date"])

    if validator.errors():
        return jsonResponse(status_code=400, error=validator.errors())

    validator = Validator(data['new_data'])
    validator.checkAll(["league", "home_team", "away_team",
                        "home_team_win_odds", "away_team_win_odds", "draw_odds", "game_date"])

    if validator.errors():
        return jsonResponse(status_code=400, error=validator.errors())

    data = db.query(UPDATE_ODDS)
    if data is None:
        return jsonResponse(status_code=500, error="something went wrong")

    return jsonResponse(data=data)


@sports.route('/delete', methods=['DELETE'])
# @tokenRequired
def deleteOdds():
    data = request.get_json()

    fields_checked = ["league", "home_team", "away_team", "game_date"]
    validator = Validator(data['old_data'])
    validator.checkAll(fields_checked)

    if validator.errors():
        return jsonResponse(status_code=400, error=validator.errors())

    data = db.query(DELETE_ODDS, params=fields_checked)
    if data is None:
        return jsonResponse(status_code=500, error="something went wrong")

    return jsonResponse(data=data)
