# Fridge Whisperer - Docker Setup Complete! 🎉

## ✅ What Was Fixed

Your project was missing Dockerfiles entirely. I've created a complete Docker setup including:

1. **Dockerfiles Created:**
   - `pantrypal-service/Dockerfile` - For inventory management API
   - `smartsuggest-service/Dockerfile` - For recommendation API
   - `dashboard/Dockerfile` - For Streamlit dashboard
   
2. **Docker Compose Configuration:**
   - `docker-compose.yml` - Orchestrates all services with PostgreSQL database
   
3. **Database Configuration Fixed:**
   - Updated both `database.py` files to support environment variables
   - Now works with both local Docker and AWS RDS
   
4. **Import Path Fixed:**
   - Fixed relative imports in `pantrypal-service/app/main.py`

## 🚀 How to Run

### Option 1: Using Docker Compose (Recommended)
```powershell
# From the project root directory
docker-compose up --build
```

This will start:
- PostgreSQL database (port 5432)
- PantryPal service (port 8000)
- SmartSuggest service (port 8001)
- Dashboard (port 8501)

Access the dashboard at: http://localhost:8501

### Option 2: Build Individual Services
```powershell
# Build PantryPal
cd pantrypal-service
docker build -t pantrypal:latest .

# Build SmartSuggest
cd ..\smartsuggest-service
docker build -t smartsuggest:latest .

# Build Dashboard
cd ..\dashboard
docker build -t dashboard:latest .
```

## 🔧 Common Issues & Solutions

### If containers exit immediately:
```powershell
# Check logs
docker logs <container-name>
# or with docker-compose
docker-compose logs -f
```

### If database connection fails:
- The docker-compose.yml includes a PostgreSQL container
- Services wait for database health check before starting
- Database URL is automatically configured via environment variables

### If ports are already in use:
```powershell
# Check what's using the port
netstat -ano | findstr :8000
netstat -ano | findstr :8001
netstat -ano | findstr :8501

# Kill the process or change port in docker-compose.yml
```

### If changes don't reflect:
```powershell
# Rebuild without cache
docker-compose up --build --force-recreate

# Or rebuild specific service
docker-compose up --build pantrypal
```

## 📝 Key Configuration Details

### Environment Variables (in docker-compose.yml)
- `DATABASE_URL` - PostgreSQL connection for both services
- Services communicate via Docker network using service names

### Ports
- 5432 - PostgreSQL
- 8000 - PantryPal API
- 8001 - SmartSuggest API  
- 8501 - Streamlit Dashboard

### API Documentation
Once running, visit:
- http://localhost:8000/docs - PantryPal Swagger UI
- http://localhost:8001/docs - SmartSuggest Swagger UI

## 🛠️ Development Mode

The docker-compose.yml is configured for development:
- Volume mounts enabled for live code reloading
- `--reload` flag for uvicorn (auto-restart on changes)
- Source code mounted from host to container

## 🗄️ Database Migrations

Run migrations after first startup:
```powershell
# For PantryPal
docker-compose exec pantrypal alembic upgrade head

# For SmartSuggest
docker-compose exec smartsuggest alembic upgrade head
```

## 🧹 Clean Up

```powershell
# Stop all services
docker-compose down

# Stop and remove volumes (fresh start)
docker-compose down -v

# Remove all images
docker-compose down --rmi all
```

## 📚 Additional Documentation

See `DOCKER_SETUP.md` for more detailed instructions and troubleshooting.

## ⚠️ Note About Dashboard

The dashboard currently has hardcoded EC2 URLs. When running locally with docker-compose, you may need to update the URLs in `dashboard/dashboard.py`:

```python
# Change from:
PANTRYPAL_URL = "http://3.110.135.117:8000"
SMARTSUGGEST_URL = "http://13.235.76.165:8001"

# To (for local Docker):
PANTRYPAL_URL = "http://pantrypal:8000"
SMARTSUGGEST_URL = "http://smartsuggest:8001"

# Or use environment variables (better):
import os
PANTRYPAL_URL = os.getenv("PANTRYPAL_URL", "http://pantrypal:8000")
SMARTSUGGEST_URL = os.getenv("SMARTSUGGEST_URL", "http://smartsuggest:8001")
```

## 🎯 Next Steps

1. Run `docker-compose up --build` from the project root
2. Wait for all services to start (watch the logs)
3. Open http://localhost:8501 in your browser
4. Test the APIs at http://localhost:8000/docs and http://localhost:8001/docs

Enjoy your Fridge Whisperer! 🥗✨
