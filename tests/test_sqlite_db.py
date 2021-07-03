import datetime
from src.database import DataBase
from src.sqlite_db import SqlDatabase

test_config = {'db_name': ':memory:', 'schema': './tests/test.sql'}
sql = SqlDatabase.getInstance(config=test_config, re_init=True)
db = DataBase.getInstance(provider=sql, re_init=True)


class Test_SqlDatabase:
    def test_query(self):
        # test data has no odds
        data = ["la liga", "madrid", "atletico", 1.8, 2.8, 4.00, "07/03/2021"]
        result_one = db.query("SELECT * FROM odds")

        new = db.query("""
        INSERT INTO odds
        (league, home_team, away_team, home_team_win_odds, away_team_win_odds, draw_odds, game_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)""", params=data)
        db.query("""
        INSERT INTO odds
        (league, home_team, away_team, home_team_win_odds, away_team_win_odds, draw_odds, game_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)""", params=data)

        result_two = db.query("SELECT * FROM odds")
        print(new)
        print(list(result_two))
        print(result_two)
        assert len(list(result_one)) == 0
        assert(list(result_two)) == [('la liga', 'madrid', 'atletico', 1.8, 2.8, 4.00,
                                      '07/03/2021'), ('la liga', 'madrid', 'atletico', 1.8, 2.8, 4.00, '07/03/2021')]
