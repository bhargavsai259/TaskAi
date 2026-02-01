from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME", "Ai Assistant")
    DATABASE_URL = os.getenv("DATABASE_URL")
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

settings = Settings()
