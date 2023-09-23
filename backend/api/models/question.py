from pydantic import BaseModel
from typing import List

class Question(BaseModel):
    questionID: str
    questionText: str
    difficultyLevel: str
    category: str
    subCategory: str
    tags: List[str]
    shortAnswer: str
    detailedAnswer: str
