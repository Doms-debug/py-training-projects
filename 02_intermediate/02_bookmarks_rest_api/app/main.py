from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import List, Optional

app = FastAPI(
    title="Bookmarks API",
    description="REST API for managing URL bookmarks",
    version="0.1.0"
)

# Model for incoming data 
class BookmarkCreate(BaseModel):
    title: str
    url: HttpUrl
    description: Optional[str] = None

# Model for outgoing data
class Bookmark(BookmarkCreate):
    id: int

# In-memory database simulation
bookmarks_db: List[Bookmark] = []
current_id = 1

@app.get("/")
def read_root():
    """
    Root endpoint returning a simple health check message.
    """
    return {"status": "ok", "message": "Bookmarks API is running"}


@app.get("/bookmarks", response_model=List[Bookmark])
def get_bookmarks():
    """
    Retrieve all stored bookmarks.
    """
    return bookmarks_db

@app.post("/bookmarks", response_model=Bookmark, status_code=201)
def create_bookmark(bookmark: BookmarkCreate):
    """
    Create a new bookmark. 
    FastAPI will automatically validate the incoming JSON against BookmarkCreate.
    """
    global current_id
    
    # Convert incoming data to a dictionary and assign an ID
    new_bookmark = Bookmark(id=current_id, **bookmark.model_dump())
    
    # Save to dummy db
    bookmarks_db.append(new_bookmark)
    current_id += 1
    
    return new_bookmark