from dotenv import load_dotenv
import os

load_dotenv()

GECKO_BASE_URL = "https://api.coingecko.com/api/v3/simple/"
GECKO_TOKEN = os.getenv("GECKO_TOKEN")