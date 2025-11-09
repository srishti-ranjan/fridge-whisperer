@echo off
echo Stopping all containers...
docker-compose down -v

echo.
echo Cleaning Python cache files...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
del /s /q *.pyc 2>nul
del /s /q *.pyo 2>nul

echo.
echo Rebuilding images without cache...
docker-compose build --no-cache

echo.
echo Starting services...
docker-compose up
