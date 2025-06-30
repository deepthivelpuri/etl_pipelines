import configparser
from pymongo import MongoClient # type: ignore
import pandas as pd
import os

def extract_data():
    # Read config.ini
    config = configparser.ConfigParser()
    config.read('config/config.ini')

    # MongoDB connection details
    uri = config["MONGODB"]["URI"]
    database_name = config["MONGODB"]["DATABASE"]
    collection_name = config["MONGODB"]["COLLECTION"]

    # Connect to MongoDB
    client = MongoClient(uri)
    db = client[database_name]
    collection = db[collection_name]

    # Fetch all documents
    documents = list(collection.find())

    # Remove _id field
    for doc in documents:
        doc.pop("_id", None)

    # Convert to DataFrame
    df = pd.DataFrame(documents)
    return df

