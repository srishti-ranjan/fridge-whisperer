from sqlalchemy.orm import Session
from .models import Suggestion
from .schemas import SuggestionCreate
from datetime import datetime

def create_suggestion(db: Session, item: SuggestionCreate):
    db_suggestion = Suggestion(**item.dict(), created_at=datetime.utcnow())
    db.add(db_suggestion)
    db.commit()
    db.refresh(db_suggestion)
    return db_suggestion

def get_suggestions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Suggestion).offset(skip).limit(limit).all()
