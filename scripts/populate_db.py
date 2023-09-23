import json
from database import db  # Importa il database dal modulo database

# Load sample data from the JSON file
with open("../data/sample_data.json", "r") as file:
    sample_data = json.load(file)

# Create or connect to a collection
collection = db["InterviewPrepHub"]

# Insert sample data into the collection
insert_result = collection.insert_many(sample_data)
print(f"Inserted {len(insert_result.inserted_ids)} documents")
