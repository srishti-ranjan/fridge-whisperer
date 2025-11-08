# app/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base
from datetime import datetime

class Suggestion(Base):
    __tablename__ = "suggestions"
    id = Column(Integer, primary_key=True, index=True)
    input_items = Column(String, nullable=False)
    suggested_items = Column(String, nullable=False)
    score = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
