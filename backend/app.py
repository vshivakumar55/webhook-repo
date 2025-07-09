from dotenv import load_dotenv
import os

load_dotenv()  # Loads the .env file

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
