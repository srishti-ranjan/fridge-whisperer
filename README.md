# fridge-whisperer
Smart Grocery List
Fridge Whisperer is a scalable smart fridge management system built with Python microservices, Docker, and Kubernetes. It helps users track inventory, get personalized recommendations, and receive timely notifications.

# Microservices Include
1. **PantryPal** covers core inventory management for all items, supporting searches and tracking physical stock.​
2. **UseLogix** enables data-driven insights into usage, allowing for predictive restocking and consumption analysis.​
3. **SmartSuggest** uses data from PantryPal and UseLogix to drive shopping and recipe recommendations, enhancing user value.​
4. **PingMe** ensures operational responsiveness, keeping users informed about their inventory status without manual checks.​
5. **TasteTune** holds and applies the user's dietary information and taste profiles, ensuring personal relevance in all outputs.

# Tech Stack
1. Python (FastAPI/Flask)
2. PostgreSQL/MySQL (PantryPal)
3. MongoDB (SmartSuggest)
4. Docker, Kubernetes, Minikube
5. REST API (HTTP)

# Folder Structure
fridge-whisper/
│
├── pantry_pal/                # PantryPal Inventory Service (FastAPI)
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI app startup
│   │   ├── models.py         # SQLAlchemy/Pydantic models
│   │   ├── crud.py           # DB operations (create, read, delete)
│   │   ├── schemas.py        # Pydantic schemas
│   │   └── database.py       # DB connection/config
│   ├── requirements.txt      # Python dependencies for PantryPal
│   ├── Dockerfile            # For containerization
│   └── README.md             # Service-specific docs
│
├── smartsuggest/             # SmartSuggest Recommendation Service (FastAPI)
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI app startup
│   │   ├── models.py         # Suggestion DB models
│   │   ├── crud.py           # DB operations (insert/query/lookup)
│   │   ├── schemas.py        # Pydantic schemas
│   │   └── database.py       # DB connection/config
│   ├── requirements.txt      # Python dependencies for SmartSuggest
│   ├── Dockerfile            # For containerization
│   └── README.md             # Service-specific docs
│
├── dashboard/
│   ├── dashboard.py          # Streamlit dashboard code
│   ├── requirements.txt      # Streamlit dependencies
│   ├── Dockerfile            # Streamlit container (optional)
│   └── README.md
│
├── docker-compose.yml        # (Optional) For local setup/spinup
├── .gitignore
└── README.md                 # Top-level repo description and setup
