from pymongo import MongoClient # type: ignore
import json
import os

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create/use the database
db = client["projects2"]

# Create/use the collection
collection = db["projects_info"]

# Path to your  file
file_path = os.path.join(os.path.dirname(__file__), "Doc_unstructured_1.txt")

# Load JSON data
with open(file_path, "r") as f:
    data = json.load(f)

# Insert documents
collection.insert_many(data)

print("Data inserted successfully into MongoDB.")
