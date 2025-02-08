import os
import requests
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

from config import API_BASE_URL, HEADERS

# League Lists
leagues = ['Premier League', 'Championship', 'La Liga', 'Segunda División', 'Bundesliga', '2. Bundesliga', 'Ligue 1', 'Ligue 2', 'Serie A', 'Serie B'
           ]

# Fetch League Data API
def get_league_data():
    leagues_list =[]

    for league in leagues:
        url = f"{API_BASE_URL}/leagues"
        params = {"name": league}

        response = requests.get(url, headers=HEADERS, params=params)

        if response.status_code == 200:
            response = response.json()
            data = response.get("response", [])

            if data:
                league_data = data[0]

                league = league_data.get("league", {})
                country = league_data.get("country", {})
                league_name = league_data.get("league", {}).get("name")

                leagues_list.append({
                    "id": league.get("id"),
                    "name": league.get("name"),
                    "type": league.get("type"),
                    "logo": league.get("logo"),
                    "country_name": country.get("name"),
                    "country_code": country.get("code"),
                    "country_flag": country.get("flag"),
                })

                print(f"Fetched: {league_name} data successfully.")
            else:
                print(f"No data found for: {league_name}")
        else:
            print(f"Failed to fetch {league_name} data. Status code: {response.status_code}")

    return pd.DataFrame(leagues_list)