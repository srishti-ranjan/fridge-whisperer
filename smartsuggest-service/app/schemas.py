from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class SuggestionBase(BaseModel):
    input_items: str
    suggested_items: str
    score: Optional[float] = None

class SuggestionCreate(SuggestionBase):
    pass
class SuggestionUpdate(SuggestionBase):
    pass

class Suggestion(SuggestionBase):
    id: int
    created_at: datetime
    model_config = {"from_attributes": True}  # fixes Pydantic v2 warning
