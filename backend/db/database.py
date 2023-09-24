from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the MongoDB URL and other configs from environment variables
MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME", "tech-job-market-insights")

if MONGO_URL is None:
    raise EnvironmentError("MONGO_URL is not set in the environment variables")

# Create a MongoDB client and connect to the database
client = MongoClient(MONGO_URL)

# Explicitly specify the database name
db = client[DB_NAME]
