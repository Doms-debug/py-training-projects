# Bookmarks REST API
A RESTful API built with FastAPI for managing URL bookmarks. It uses SQLite for persistent local storage, SQLAlchemy as the ORM and Pydantic for strict data validation.

## Features
* Provides endpoints to create, retrieve, and delete bookmarks
* Validates incoming URLs automatically using Pydantic
* Stores data persistently in a local SQLite database
* Generates interactive API documentation automatically via Swagger UI

## Setup and Installation
* Navigate to the project directory
* Create a virtual environment using `python -m venv venv`
* Activate the virtual environment
* Install the required dependencies using `pip install -r requirements.txt`

## Usage
Start the local ASGI development server using Uvicorn. The `--reload` flag ensures the server restarts automatically when code changes are detected.

```bash
uvicorn app.main:app --reload

Enjoy