from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SuggestionRequest(BaseModel):
    ingredients: list[str]

@app.post("/suggest")
def get_suggestions(req: SuggestionRequest):
    # Dummy logic for demo
    return {"suggestions": ["Omelette", "Pasta", "Salad"]}

