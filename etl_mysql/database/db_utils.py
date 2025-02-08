import os
from dotenv import load_dotenv
load_dotenv()

from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASS, MYSQL_DB

from sqlalchemy import create_engine,text

class DatabaseManager:
    def __init__(self):
        """Initialize database connection using SQLAlchemy."""
        self.db_url = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}/{MYSQL_DB}"
        self.engine = create_engine(self.db_url, pool_recycle=3600)
        self.create_tables()

    def create_tables(self):
        """Create all tables by reading from schema.sql."""
        SCHEMA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "database", "schema.sql")

        try:
            with open(SCHEMA_FILE, "r") as sql_file:
                queries = sql_file.read().split(";")

            with self.engine.connect() as conn:
                for query in queries:
                    query = query.strip()
                    if query:
                        conn.execute(text(query))  
                        conn.commit()

            print("All tables checked/created.")
        except Exception as e:
            print(f"Error creating tables: {e}")

    def insert_data(self, df, table_name):
        """Insert DataFrame into MySQL table."""
        if df.empty:
            print(f"No data to insert into {table_name}.")
            return

        try:
            df.to_sql(table_name, self.engine, if_exists="append", index=False, method="multi")
            print(f"Inserted {len(df)} rows into {table_name}.")
        except Exception as e:
            print(f"Error inserting data into {table_name}: {e}")