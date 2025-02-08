from etl_mysql.database.db_utils import DatabaseManager
from etl_mysql.fetch_api.get_leagues import get_league_data
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

    # Fetch league data
    league_df = get_league_data()

    if league_df.empty:
        logging.warning("No league data fetched. Skipping database insert.")
    else:
        # Insert into MySQL
        db_manager.insert_data(league_df, "leagues")
        end_time = time.time()
        logging.info(f"Inserted {len(league_df)} rows into leagues table. Total time taken: {end_time - start_time:.3f} seconds")

if __name__ == "__main__":
    main()