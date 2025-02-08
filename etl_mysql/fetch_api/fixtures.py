import requests
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

from config import API_BASE_URL_V3, HEADERS
from etl_mysql.fetch_api.get_leagues import get_league_data

# Fetch Team Data using League ID
def get_fixtures_data():
    fixtures_data = []
    
    # Fetch unique league IDs
    league_df = get_league_data()
    league_ids = league_df['id'].unique()

    for league_id in league_ids:
        url = f"{API_BASE_URL_V3}/fixtures"
        params = {"league": league_id, "season": "2024", "status": "FT"}
        response = requests.get(url, headers=HEADERS, params=params)

        if response.status_code == 200:
            response = response.json()
            data = response.get("response", [])

            if data:
                fixture_data = data[0]
                round_name = fixture_data.get("league", {}).get("round")

                fixtures = fixture_data.get("fixture", {})
                league = fixture_data.get("league", {})
                status = fixture_data.get("status", {})
                venue = fixture_data.get("venue", {})
                home_team = fixture_data.get("teams", {}).get("home", {})
                away_team = fixture_data.get("teams", {}).get("away", {})
                goals = fixture_data.get("goals", {})
                halftime = fixture_data.get("score", {}).get("halftime", {})
                penalty = fixture_data.get("score", {}).get("penalty", {})

                # For print purpose (optional)
                home_id = home_team.get("name")
                away_id = away_team.get("name")

                fixtures_data.append({
                    "id": fixtures.get("id"),
                    "referee": fixtures.get("referee"),
                    "date": fixtures.get("date"),
                    "venue_name": venue.get("name"),
                    "status": status.get("short"),
                    "elapsed": status.get("elapsed"),
                    "league_id": league.get("id"),
                    "season": league.get("season"),
                    "round": fixtures.get("round"),
                    "home_id": home_team.get("id"),
                    "away_id": away_team.get("id"),
                    "goals_home": goals.get("home"),
                    "goals_away": goals.get("away"),
                    "ht_goals_home": halftime.get("home"),
                    "ht_goals_away": halftime.get("away"),
                    "penalty_home": penalty.get("home"),
                    "penalty_away": penalty.get("away")
                })

                print(f"Fetched: {round_name}: {home_id} vs {away_id} data successfully.")
            else:
                print(f"No data found for: {round_name}: {home_id} vs {away_id}")
        else:
            print(f"Failed to fetch {round_name}: {home_id} vs {away_id} data. Status code: {response.status_code}")

    return pd.DataFrame(fixtures_data)