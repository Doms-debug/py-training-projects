from fastapi import FastAPI

app = FastAPI(
    title="Bookmarks API",
    description="REST API for managing URL bookmarks",
    version="0.1.0"
)

@app.get("/")
def read_root():
    """
    Root endpoint returning a simple health check message.
    """
    return {"status": "ok", "message": "Bookmarks API is running"}