from fastapi import APIRouter
from fastapi.params import Depends
from sqlmodel import Session

from database import SessionLocal, get_db
from domain.question import question_schema, question_crud
from models import Question

router = APIRouter(
    prefix="/api/question"
)

@router.get("/", response_model=list[question_schema.Question])
async def get_questions(db : Session = Depends(get_db) ):
    questions = question_crud.get_questions(db)

    return questions
