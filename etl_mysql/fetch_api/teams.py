import requests
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

from config import API_BASE_URL_V2, HEADERS
from etl_mysql.fetch_api.get_leagues import get_league_data

# Fetch Team Data using League ID
def get_team_data():
    team_list = []
    
    # Fetch unique league IDs
    league_df = get_league_data()
    league_ids = league_df['id'].unique()

    for league_id in league_ids:
        url = f"{API_BASE_URL_V2}/teams/league/{league_id}"
        response = requests.get(url, headers=HEADERS)

        if response.status_code == 200:
            data = response.json().get("teams", [])
            team_list.extend(data)

            team_names = [team.get("name", "Unknown") for team in data]
            print(f"Fetched teams from League ID {league_id}: {', '.join(team_names)}")
        else:
            print(f"Error fetching teams for League ID {league_id}: {response.status_code}")
    
    return pd.DataFrame(team_list)