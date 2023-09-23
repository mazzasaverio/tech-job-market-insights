from fastapi import APIRouter, HTTPException, Path, Query
from api.models.question import Question
from api.db.database import db
from typing import List
import os

router = APIRouter()

# Retrieve the MongoDB collection
collection_name = os.getenv("COLLECTION_NAME", "InterviewPrepHub")
print(f"Collection name: {collection_name}")
collection = db[collection_name]
print(f"Collection: {collection}")

@router.get("/questions", response_model=List[Question])
def get_questions(skip: int = Query(0, alias="start"), limit: int = Query(10, alias="count")):
    """
    Retrieve a list of questions from the database.
    
    Args:
        skip (int): The number of records to skip.
        limit (int): The maximum number of records to return.
    
    Returns:
        list: A list of questions.
    """
    questions_cursor = collection.find().skip(skip).limit(limit)
    questions = list(questions_cursor)
    return questions

@router.get("/questions/{questionID}", response_model=Question)
def get_question_by_id(questionID: str = Path(..., title="The ID of the question to get")):
    """
    Retrieve a specific question by its ID.
    
    Args:
        questionID (str): The ID of the question to retrieve.
        
    Returns:
        dict: The question data.
    """
    question = collection.find_one({"_id": questionID})
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@router.post("/questions", response_model=Question)
def add_question(question: Question):
    """
    Add a new question to the database.
    
    Args:
        question (Question): The question data to add.
        
    Returns:
        dict: The added question data.
    """
    insert_result = collection.insert_one(question.model_dump())
    question.id = insert_result.inserted_id
    return question.model_dump()
