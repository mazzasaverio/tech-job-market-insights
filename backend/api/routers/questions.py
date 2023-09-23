from fastapi import APIRouter
from api.models.question import Question

router = APIRouter()

@router.get("/questions")
def get_questions():
    return []

@router.get("/questions/{questionID}")
def get_question_by_id(questionID: str):
    return {}

@router.post("/questions")
def add_question(question: Question):
    return {}
