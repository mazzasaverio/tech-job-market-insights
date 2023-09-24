from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routers import questions
import json
import os
from db.database import db

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict the origins for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(questions.router)



@app.get("/")
async def read_root():
    """
    A simple home page for the API.
    
    Returns:
        dict: Welcome message and API information.
    """
    return {"message": "Welcome to TechJobMarketInsights API", "info": "Navigate to /docs for API documentation"}



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
