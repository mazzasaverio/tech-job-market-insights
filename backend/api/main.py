from fastapi import FastAPI, HTTPException
from api.routers import questions
import json
import os
from api.db.database import db

app = FastAPI()

app.include_router(questions.router)

@app.get("/load-sample-data")
async def load_sample_data():
    try:
        # Get the path to the JSON file
        json_path = os.path.join(os.path.dirname(__file__), "data", "sample_data.json")
        
        with open(json_path, "r") as file:
            sample_data = json.load(file)
        
        collection_name = os.getenv("COLLECTION_NAME", "InterviewPrepHub")
        collection = db[collection_name]
        
        insert_result = collection.insert_many(sample_data)
        
        return {"message": f"Inserted {len(insert_result.inserted_ids)} documents"}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
