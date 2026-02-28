import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "AI App")
    ENV: str = os.getenv("ENV", "development")

settings = Settings()