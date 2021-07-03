# sports_betting_api

A basic micro service CRUD API for a sports betting API

# Endpoints

## Post data

```
/api/sportsbetting/create
```

This endpoints takes a json object and makes an entry in the database

```
data = {
    "league": "premier league",
    "home_team": "arsenal",
    "away_team": "liverpool",
    "home_team_win_odds": 3.50,
    "away_team_win_odds": 2.00,
    "draw_odds": 4.25,
    "game_date": "2020-04-21"
}
```

## Read all data

```
/api/sportsbetting/read
```

This endpoint returns all entries in the database. It doesn't take any parameters

## Update all data

```
/api/sportsbetting/update
```

This endpoint takes an entry with the old data and new data that needs to be updated. Returning the new data

```
data = {
    old_data: {
        "league": "premier league",
        "home_team": "arsenal",
        "away_team": "liverpool",
        "game_date": "2020-04-21"
    }
    new_data: {
        "league": "la liga",
        "home_team": "real madrid",
        "away_team": "barcelona",
        "home_team_win_odds": 3.50,
        "away_team_win_odds": 2.00,
        "draw_odds": 4.25,
        "game_date": "2020-04-21"
    }
}
```

## Delete an entry from the database

```
/api/sportsbetting/delete
```

This endpoint takes a json object with the keys as seen below and deletes the entry from the database

```
data = {
    "league": "premier league",
    "home_team": "arsenal",
    "away_team": "liverpool",
    "game_date": "2020-04-21"
}
```
