from dotenv import load_dotenv
import os

load_dotenv()

GECKO_BASE_URL = "https://api.coingecko.com/api/v3/simple/"
GECKO_TOKEN = os.getenv("GECKO_TOKEN")
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_EXPIRE_MINUTES = 30
JWT_ALGORITHM = "HS256"
JWT_TOKEN_TYPE = "Bearer"