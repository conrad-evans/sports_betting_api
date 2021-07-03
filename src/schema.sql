DROP TABLE IF EXISTS odds;

CREATE TABLE odds
(
    id INTEGER PRIMARY KEY NOT NULL,
    league TEXT NOT NULL,
    home_team TEXT NOT NULL,
    away_team TEXT NOT NULL,
    home_team_win_odds REAL NOT NULL,
    away_team_win_odds REAL NOT NULL,
    draw_odds REAL NOT NULL,
    game_date TEXT NOT NULL
);