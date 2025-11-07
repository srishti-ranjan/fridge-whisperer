from sqlalchemy.orm import Session
from . import models, schemas

def get_item(db: Session, item_id: int):
    return db.query(models.PantryItem).filter(models.PantryItem.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PantryItem).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.PantryItemCreate):
    db_item = models.PantryItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, update_data: schemas.PantryItemUpdate):
    db_item = get_item(db, item_id)
    if not db_item:
        return None
    for field, value in update_data.dict(exclude_unset=True).items():
        setattr(db_item, field, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = get_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
        return True
    return False
