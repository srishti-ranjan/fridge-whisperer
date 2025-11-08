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

@app.post("/suggest", response_model=schemas.Suggestion)
def get_suggestion(req: schemas.SuggestionCreate, db: Session = Depends(get_db)):
    return crud.create_suggestion(db, req)

@app.get("/suggestions", response_model=list[schemas.Suggestion])
def list_suggestions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_suggestions(db, skip, limit)
