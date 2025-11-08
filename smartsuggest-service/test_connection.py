from sqlalchemy import create_engine

# Use your RDS credentials and endpoint
engine = create_engine(
    'postgresql+psycopg2://fridge:fridge-whisperer@smartsuggest-db.ct800oqi6unc.ap-south-1.rds.amazonaws.com:5432/smartsuggest_db'
)
try:
    with engine.connect() as conn:
        print("Successfully connected to PostgreSQL RDS!")
except Exception as e:
    print("Failed to connect:", e)

