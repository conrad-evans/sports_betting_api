CREATE_ODDS = """INSERT INTO odds (league, home_team, away_team, home_team_win_odds, away_team_win_odds, draw_odds, game_date) VALUES (?, ?, ?, ?, ?, ?, ?)"""
READ_ALL_ODDS = """SELECT * FROM odds"""
UPDATE_ODDS = """UPATE odds SET league = ?, home_team = ?, away_team = ?, home_team_win_odds = ?, away_team_win_odds = ?, draw_odds = ?, game_date = ? WHERE league = ?, home_team = ?, away_team = ? AND game_date = ?"""
DELETE_ODDS = """DELETE FROM odds WHERE league = ?, home_team = ?, away_team = ? AND game_date = ?"""
