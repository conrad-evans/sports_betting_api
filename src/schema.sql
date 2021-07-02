-- CREATE TABLE IF NOT EXISTS sportsbetting (
-- id  INTEGER PRIMARY KEY NOT NULL,
-- league BLOB NOT NULL,
-- home_team BLOB NOT NULL,
-- away_team BLOB NOT NULL,
-- home_team_win_odds REAL NOT NULL,
-- away_team_win_odds REAL NOT NULL,
-- draw_odds REAL NOT NULL,
-- game_date TEXT NOT NULL)

CREATE TABLE IF NOT EXISTS sportsbetting (
    id INTEGER PRIMARY KEY NOT NULL,
    league TEXT NOT NULL,
    home_team TEXT NOT NULL,
    away_team TEXT NOT NULL,
    home_team_win_odds TEXT NOT NULL,
    away_team_win_odds TEXT NOT NULL,
    draw_odds TEXT NOT NULL,
    game_date TEXT NOT NULL
)