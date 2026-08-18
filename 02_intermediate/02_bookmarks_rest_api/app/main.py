from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, HttpUrl
from typing import List, Optional

from app import models
from app.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookmarks API")

# --- Pydantic models ---
class BookmarkCreate(BaseModel):
    title: str
    url: HttpUrl
    description: Optional[str] = None

class Bookmark(BookmarkCreate):
    id: int
    
    # Enables reading data directly from SQLAlchemy ORM models
    model_config = {"from_attributes": True}

# --- Database Dependency ---
def get_db():
    """Creates a new database session per request and closes it afterwards."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- API Endpoints ---
@app.get("/bookmarks", response_model=List[Bookmark])
def get_bookmarks(db: Session = Depends(get_db)):
    return db.query(models.DBBookmark).all()

@app.post("/bookmarks", response_model=Bookmark, status_code=201)
def create_bookmark(bookmark: BookmarkCreate, db: Session = Depends(get_db)):
    # Convert Pydantic model to SQLAlchemy ORM model
    db_bookmark = models.DBBookmark(
        title=bookmark.title,
        url=str(bookmark.url),
        description=bookmark.description
    )
    
    # Save to db
    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)
    
    return db_bookmark

@app.delete("/bookmarks/{bookmark_id}", status_code=204)
def delete_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    """
    Delete a bookmark by its ID.
    """
    db_bookmark = db.query(models.DBBookmark).filter(models.DBBookmark.id == bookmark_id).first()

    if db_bookmark is None:
        raise HTTPException(status_code=404, detail="Bookmark not found")
        
    db.delete(db_bookmark)
    db.commit()
    
    return None