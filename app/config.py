from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    DEBUG = os.getenv("DEBUG") == "True"

    GITHUB_WEBHOOK_SECRET = os.getenv("GITHUB_WEBHOOK_SECRET")
    GITHUB_APP_ID = os.getenv("GITHUB_APP_ID")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

settings = Settings()