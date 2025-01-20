from sqlmodel import Session

from models import Question


def get_questions(db: Session):
    questions = db.query(Question).order_by(Question.create_date.desc()).all()

    return questions