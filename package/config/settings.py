from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env into environment variables

class Settings(BaseSettings):
    DATABASE_URL: str
    DEBUG: bool = False

    class Config:
        env_file = ".env"
        case_sensitive = True

# Singleton pattern — reuse this instance
settings = Settings()
# settings = os.getenv("DEBUG")
