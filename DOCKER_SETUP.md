# Docker Build and Run Instructions for Fridge Whisperer

## Prerequisites
- Docker installed on your system
- Docker Compose installed (usually comes with Docker Desktop)

## Quick Start with Docker Compose (Recommended)

1. **Start all services:**
   ```bash
   docker-compose up --build
   ```

2. **Access the services:**
   - Dashboard: http://localhost:8501
   - PantryPal API: http://localhost:8000
   - SmartSuggest API: http://localhost:8001
   - PantryPal Docs: http://localhost:8000/docs
   - SmartSuggest Docs: http://localhost:8001/docs

3. **Stop all services:**
   ```bash
   docker-compose down
   ```

4. **Stop and remove volumes (clean restart):**
   ```bash
   docker-compose down -v
   ```

## Build Individual Services

### PantryPal Service
```bash
cd pantrypal-service
docker build -t pantrypal:latest .
docker run -p 8000:8000 -e DATABASE_URL=postgresql://postgres:postgres@host.docker.internal:5432/fridge_db pantrypal:latest
```

### SmartSuggest Service
```bash
cd smartsuggest-service
docker build -t smartsuggest:latest .
docker run -p 8001:8001 -e DATABASE_URL=postgresql://postgres:postgres@host.docker.internal:5432/fridge_db smartsuggest:latest
```

### Dashboard
```bash
cd dashboard
docker build -t dashboard:latest .
docker run -p 8501:8501 dashboard:latest
```

## Common Issues and Solutions

### Issue: Container exits immediately after build
**Solution:** Check logs with `docker logs <container-id>` to see the error.

### Issue: Database connection fails
**Solution:** 
- Ensure PostgreSQL is running
- Check DATABASE_URL environment variable
- For local development, use `host.docker.internal` instead of `localhost`
- For docker-compose, use the service name (e.g., `postgres`)

### Issue: Port already in use
**Solution:** 
- Check if another service is using the port: `netstat -ano | findstr :8000`
- Stop the conflicting service or change the port mapping

### Issue: Import errors or module not found
**Solution:** 
- Make sure you're building from the correct directory
- Check that requirements.txt includes all dependencies
- Rebuild without cache: `docker build --no-cache -t <image-name> .`

### Issue: Changes not reflecting
**Solution:** 
- Rebuild the image: `docker-compose up --build`
- For development, use volume mounts (already configured in docker-compose.yml)

## Environment Variables

### PantryPal & SmartSuggest
- `DATABASE_URL`: PostgreSQL connection string (default: AWS RDS for production)

### Dashboard
- `PANTRYPAL_URL`: URL to PantryPal service
- `SMARTSUGGEST_URL`: URL to SmartSuggest service

## Database Setup

The docker-compose.yml includes a PostgreSQL container. Tables are created automatically when the services start.

To manually run migrations:
```bash
# For PantryPal
docker-compose exec pantrypal alembic upgrade head

# For SmartSuggest
docker-compose exec smartsuggest alembic upgrade head
```

## Development Mode

The docker-compose.yml is configured for development with:
- Auto-reload on code changes
- Volume mounts for live editing
- Exposed ports for debugging

## Production Deployment

For production:
1. Remove volume mounts from docker-compose.yml
2. Remove `--reload` flag from uvicorn commands
3. Use production-grade database (AWS RDS as configured in database.py)
4. Set proper environment variables
5. Use a reverse proxy (nginx) for SSL/TLS

## Logs

View logs for all services:
```bash
docker-compose logs -f
```

View logs for specific service:
```bash
docker-compose logs -f pantrypal
docker-compose logs -f smartsuggest
docker-compose logs -f dashboard
```
