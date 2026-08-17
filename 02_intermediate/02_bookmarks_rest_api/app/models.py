from sqlalchemy import Column, Integer, String
from app.database import Base

class DBBookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    url = Column(String)
    description = Column(String, nullable=True)