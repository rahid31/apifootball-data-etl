from etl_mysql.database.db_utils import DatabaseManager
from etl_mysql.fetch_api.get_leagues import get_league_data
from etl_mysql.fetch_api.teams import get_team_data
from etl_mysql.fetch_api.fixtures import get_fixtures_data

import logging
import time

# Set up logging
logging.basicConfig(
    filename="logs.txt", 
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Starting ETL process for leagues...")
    start_time = time.time()

    # Initialize database connection
    db_manager = DatabaseManager()

    # Fetch all data
    dataframes = {
        "leagues": get_league_data(),
        # "teams": get_team_data(),
        "fixtures": get_fixtures_data()
    }

    # Loop through data and insert into MySQL
    for table_name, df in dataframes.items():
        if not df.empty:
            db_manager.insert_data(df, table_name)
            logging.info(f"Inserted {len(df)} rows into {table_name} table.")
        else:
            logging.warning(f"No data fetched for {table_name}. Skipping insert.")

    logging.info(f"ETL process completed in {time.time() - start_time:.3f} seconds")

if __name__ == "__main__":
    main()