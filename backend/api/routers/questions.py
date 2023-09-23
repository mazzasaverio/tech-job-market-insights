from fastapi import APIRouter, HTTPException, Path, Query
from api.models.question import Question
from api.db.database import db
from typing import List, Optional
import os

router = APIRouter()

collection_name = os.getenv("COLLECTION_NAME", "InterviewPrepHub")
collection = db[collection_name]

@router.get("/question-distinct-fields")
def get_distinct_fields():
    """
    Retrieve distinct categories, sub-categories, and difficulty levels.

    Returns:
        dict: A dictionary containing arrays of distinct categories, sub-categories, and difficulty levels.
    """
    distinct_fields = {
        "categories": list(db[collection_name].distinct("category")),
        "subCategories": list(db[collection_name].distinct("subCategory")),
        "difficultyLevels": list(db[collection_name].distinct("difficultyLevel"))
    }
    return distinct_fields


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


@router.get("/questions", response_model=List[Question])
def get_questions(skip: int = Query(0, alias="start"), 
                  limit: int = Query(10, alias="count"),
                  category: Optional[str] = None,
                  subCategory: Optional[str] = None,
                  difficultyLevel: Optional[str] = None):
    """
    Retrieve a list of questions from the database with optional filters.
    
    Args:
        skip (int): The number of records to skip.
        limit (int): The maximum number of records to return.
        category (str, optional): Filter by category.
        subCategory (str, optional): Filter by subcategory.
        difficultyLevel (str, optional): Filter by difficulty level.
    
    Returns:
        list: A list of questions.
    """
    filters = {}
    if category:
        filters["category"] = category
    if subCategory:
        filters["subCategory"] = subCategory
    if difficultyLevel:
        filters["difficultyLevel"] = difficultyLevel

    questions_cursor = collection.find(filters).skip(skip).limit(limit)
    questions = list(questions_cursor)
    return questions




