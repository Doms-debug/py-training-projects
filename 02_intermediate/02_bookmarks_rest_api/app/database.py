from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Create a local Sql
SQLALCHEMY_DATABASE_URL = "sqlite:///./bookmarks.db"

# check_same_thread is required only for SQLite in FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()