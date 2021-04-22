from src.db import DataBase

test_db = ":memory:"


class Test_DataBase:
    def test_init(self):
        pass

    def test_createOdds(self):
        data = {"league": "premier league",
                "home_team": "arsenal", "away_team": "liverpool", "home_team_win_odds": 3.50, "away_team_win_odds": 2.00, "draw_odds": 4.25, "game_date": "2020-21-04"}

        db = DataBase(test_db)
        db.create(data)
        assert len(list(db.cursor.execute(
            """SELECT * FROM sportsbetting"""))) == 1
        assert list(db.cursor.execute("""SELECT * FROM sportsbetting"""))[0] == (
            1, "premier league", "arsenal", "liverpool", 3.5, 2.0, 4.25, "2020-21-04")

    def test_readOdds(self):
        pass

    def test_updateOdds(self):
        pass

    def test_deleteOdds(self):
        pass
