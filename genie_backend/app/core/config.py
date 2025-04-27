# app/core/config.py

from dotenv import load_dotenv
import os

load_dotenv()  # This must be called BEFORE reading the variables

class Settings:
    MONGO_URI: str = os.getenv("MONGO_URI")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    EXA_API_KEY: str = os.getenv("EXA_API_KEY")
    JWT_SECRET: str = os.getenv("JWT_SECRET")

settings = Settings()
