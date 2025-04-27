from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # Loads .env file

uri = os.getenv("MONGO_URI")

try:
    client = MongoClient(uri)
    print("✅ Connected to MongoDB")
    print("Databases:", client.list_database_names())
except Exception as e:
    print("❌ Connection failed:", e)
