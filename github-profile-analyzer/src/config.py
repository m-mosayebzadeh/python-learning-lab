from dotenv import load_dotenv
import os

load_dotenv()

ACCEPT_HEADER = "application/vnd.github+json"
API_VERSION = "2026-03-10"

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")