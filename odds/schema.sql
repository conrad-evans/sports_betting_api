DROP TABLE IF EXISTS Odds;
CREATE TABLE Odds
(
    id TEXT UNIQUE,
    league TEXT,
    home_team TEXT,
    away_team TEXT,
    home_team_win_odds INTEGER,
    away_team_win_odds INTEGER,
    draw_odds INTEGER,
    game_date TEXT
)