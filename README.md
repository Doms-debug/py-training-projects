# Python training projects
A monorepo containing Python projects ranging from basic CLI automation scripts to advanced microservices. This repository demonstrates software development, infrastructure automation, and basic data engineering skills.

# Repository structure
## 01_basic
* Bulk file renamer (os, pathlib, argparse)

* Asset price monitor (requests, json)

* Password generator (random, string)

* Log IP extractor (re, collections)

* Port scanner (socket)

## 02_intermediate
* Infra health checker (psutil, requests)

* Bookmarks REST API (FastAPI, SQLite, pydantic)

* Portfolio dashboard (Gradio, Pandas)

## 03_advanced
* AI-Powered log analyzer and alerting system (FastAPI, PostgreSQL, Docker, scikit-learn, GitHub Actions)

# Setup and installation
Each project requires an isolated virtual environment to manage dependencies properly.

# Clone this repository

1. Navigate to the target project directory

2. Create a virtual environment using:
```
python -m venv venv
```
3. Activate the virtual environment via:
```
pip install -r requirements.txt
```
4. Follow specific execution instructions located in the project-level README.md file

# Tech stack
Programming language: python3

APIs: FastAPI, requests

Data and ML: Pandas, scikit-learn

Frontend / Visualization: Streamlit

DevOps and infra: Docker, Docker Compose, GitHub Actions

Databases: SQLite, PostgreSQL