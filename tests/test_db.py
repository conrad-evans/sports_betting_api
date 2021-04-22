import sqlite3
from tests.test_factory import test_config

from werkzeug import test
from src.db import DataBase

test_db = ":memory:"
test_data = {"league": "premier league",
             "home_team": "arsenal", "away_team": "liverpool", "home_team_win_odds": 3.50, "away_team_win_odds": 2.00, "draw_odds": 4.25, "game_date": "2020-21-04"}

test_data_two = {"league": "la liga",
                 "home_team": "real madrid", "away_team": "barcelona", "home_team_win_odds": 3.50, "away_team_win_odds": 2.00, "draw_odds": 4.25, "game_date": "2020-21-04"}


class Test_DataBase:
    def test_init(self):
        db = DataBase(test_db)
        assert isinstance(db.cursor, sqlite3.Cursor)
        assert len(list(db.cursor.execute(
            """SELECT * FROM sportsbetting"""))) == 0

    def test_createOdds(self):
        db = DataBase(test_db)
        db.create(test_data)
        assert len(list(db.cursor.execute(
            """SELECT * FROM sportsbetting"""))) == 1
        assert list(db.cursor.execute("""SELECT * FROM sportsbetting"""))[0] == (
            1, "premier league", "arsenal", "liverpool", 3.5, 2.0, 4.25, "2020-21-04")

    def test_readOdds(self):
        db = DataBase(test_db)
        db.create(test_data)
        db.create(test_data_two)
        result = db.read()
        assert isinstance(result, list)
        assert len(result) == 2
        assert result[1] == (
            2, "la liga", "real madrid", "barcelona", 3.5, 2.0, 4.25, "2020-21-04")

    def test_updateOdds(self):
        pass

    def test_deleteOdds(self):
        # test data
        data_to_delete = {
            "league": "la liga",
            "home_team": "real madrid",
            "away_team": "barcelona",
            "game_date": "2020-21-04"
        }

        db = DataBase(test_db)
        db.create(test_data)
        db.create(test_data_two)
        db.delete(data_to_delete)

        # assertion
        assert len(db.read()) == 1
        # assert len(list(db.cursor.execute(
            # """SELECT * FROM sportsbetting"""))) == 1
        assert list(db.cursor.execute("""SELECT * FROM sportsbetting"""))[0] == (
            1, "premier league", "arsenal", "liverpool", 3.5, 2.0, 4.25, "2020-21-04")
