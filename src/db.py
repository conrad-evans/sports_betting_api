import sqlite3
from src.schema import SCHEMA


class DataBase:
    def __init__(self, db_name: str) -> None:
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(SCHEMA)

    def create(self, data):
        try:
            self.cursor.execute(
                """
                INSERT INTO sportsbetting 
                (league, home_team, away_team, home_team_win_odds, away_team_win_odds, draw_odds, game_date)
                 VALUES (?, ?, ?, ?, ?, ?, ?)
                 """,
                (data['league'], data['home_team'], data['away_team'], data['home_team_win_odds'], data['away_team_win_odds'], data['draw_odds'], data['game_date']))
            self.conn.commit()
            return data
        except Exception as e:
            print(e)
            return None

    def read(self):
        try:
            data = self.conn.execute("""SELECT * FROM sportsbetting""")
            self.conn.commit()
            return list(data)
        except Exception as e:
            print(e)
            return None

    def update(self, data):
        self.conn.commit()

    def delete(self, data):
        self.cursor.execute(
            """DELETE FROM sportsbetting WHERE league = ?, home_team = ?, away_team = ?, game_date = ?""",
            (data["league"], data["home_team"], data["away_team"], data["game_date"]))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
