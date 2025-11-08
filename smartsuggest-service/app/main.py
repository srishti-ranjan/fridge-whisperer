from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, schemas, crud

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/suggestions/", response_model=schemas.Suggestion)
def create_suggestion(suggestion: schemas.SuggestionCreate, db: Session = Depends(get_db)):
    return crud.create_suggestion(db, suggestion)

@app.get("/suggestions/", response_model=list[schemas.Suggestion])
def read_suggestions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_suggestions(db, skip=skip, limit=limit)

@app.get("/suggestions/{suggestion_id}", response_model=schemas.Suggestion)
def read_suggestion(suggestion_id: int, db: Session = Depends(get_db)):
    db_obj = crud.get_suggestion(db, suggestion_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Suggestion not found")
    return db_obj

@app.put("/suggestions/{suggestion_id}", response_model=schemas.Suggestion)
def update_suggestion(suggestion_id: int, suggestion: schemas.SuggestionUpdate, db: Session = Depends(get_db)):
    updated = crud.update_suggestion(db, suggestion_id, suggestion)
    if not updated:
        raise HTTPException(status_code=404, detail="Suggestion not found")
    return updated

@app.delete("/suggestions/{suggestion_id}", status_code=204)
def delete_suggestion(suggestion_id: int, db: Session = Depends(get_db)):
    success = crud.delete_suggestion(db, suggestion_id)
    if not success:
        raise HTTPException(status_code=404, detail="Suggestion not found")
    return None

