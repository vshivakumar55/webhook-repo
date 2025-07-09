from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

db = client.webhook_data
collection = db.events
