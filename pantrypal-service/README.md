# PantryPal Microservice

This is a FastAPI-based microservice for managing pantry inventory items.

## Features

- Full CRUD API for pantry items
- Interactive API docs at `/docs`
- Easy to run locally or on EC2

## Quickstart

1. Clone the repo:
git clone git@github.com:srishti-ranjan/fridge-whisperer.git
cd fridge-whisperer/pantrypal-service

2. Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Run the app:
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

5. Access the API docs:
http://<EC2-Public-IP>:8000/docs

## Endpoints

- `GET /items` - List all items
- `POST /items` - Add a new item
- `PUT /items/{item_id}` - Update an item
- `DELETE /items/{item_id}` - Delete an item

## License

MIT

