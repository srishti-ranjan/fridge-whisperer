# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Install streamlit and requests
RUN pip install --no-cache-dir streamlit requests pandas

# Copy dashboard code
COPY dashboard.py .

# Expose port 8501 for Streamlit
EXPOSE 8501

# Command to run Streamlit
CMD ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
