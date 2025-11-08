from sqlalchemy.orm import Session
from .models import Suggestion
from .schemas import SuggestionCreate, SuggestionUpdate
from datetime import datetime

# CREATE
def create_suggestion(db: Session, suggestion: SuggestionCreate):
    db_obj = Suggestion(
        input_items=suggestion.input_items,
        suggested_items=suggestion.suggested_items,
        score=suggestion.score,
        created_at=datetime.utcnow()
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# READ ALL
def get_suggestions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Suggestion).offset(skip).limit(limit).all()

# READ ONE
def get_suggestion(db: Session, suggestion_id: int):
    return db.query(Suggestion).filter(Suggestion.id == suggestion_id).first()

# UPDATE
def update_suggestion(db: Session, suggestion_id: int, suggestion: SuggestionUpdate):
    db_obj = get_suggestion(db, suggestion_id)
    if not db_obj:
        return None
    for attr, value in suggestion.dict(exclude_unset=True).items():
        setattr(db_obj, attr, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

# DELETE
def delete_suggestion(db: Session, suggestion_id: int):
    db_obj = get_suggestion(db, suggestion_id)
    if not db_obj:
        return False
    db.delete(db_obj)
    db.commit()
    return True

