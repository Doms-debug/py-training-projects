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

@app.get("/")
def read_root():
    """
    Root endpoint returning a simple health check message.
    """
    return {"status": "ok", "message": "Bookmarks API is running"}