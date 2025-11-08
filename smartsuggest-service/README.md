# SmartSuggest Microservice

A FastAPI-based microservice for smart recipe and suggestion features.

## Features

- API for smart suggestions
- Interactive API docs at `/docs`
- Easy to run locally or on EC2

## Quickstart

1. Clone the repo and enter the service directory.
2. Create and activate a virtual environment.
3. Install dependencies.
4. Run the app with Uvicorn.
5. Access the API docs at `/docs`.

## Folder Structure

smartsuggest-service/
├── README.md
├── requirements.txt
├── alembic.ini
├── alembic/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
├── test_connection.py
