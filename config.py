from dotenv import load_dotenv
import os

load_dotenv()

# MYSQL Credentials
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASS = os.getenv("MYSQL_PASS")
MYSQL_DB = os.getenv("MYSQL_DB")

# API Credentials
API_BASE_URL_V3 = os.getenv("API_BASE_URL_V3")
API_BASE_URL_V2 = os.getenv("API_BASE_URL_V2")
API_KEY = os.getenv("API_KEY")
API_HOST = os.getenv("API_HOST")

HEADERS = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": API_HOST
}
