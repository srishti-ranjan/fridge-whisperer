# Clean and Rebuild Docker Containers Script
# Run this in PowerShell

Write-Host "Stopping all containers..." -ForegroundColor Yellow
docker-compose down -v

Write-Host "`nCleaning Python cache files..." -ForegroundColor Yellow
Get-ChildItem -Path . -Recurse -Directory -Filter __pycache__ -Force | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
Get-ChildItem -Path . -Recurse -File -Include *.pyc,*.pyo -Force | Remove-Item -Force -ErrorAction SilentlyContinue

Write-Host "`nRebuilding images without cache..." -ForegroundColor Yellow
docker-compose build --no-cache

Write-Host "`nStarting services..." -ForegroundColor Green
docker-compose up
