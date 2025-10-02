# Python runtime
FROM python:3.11-slim

# Faster, smaller builds
ENV PIP_NO_CACHE_DIR=1 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app

# Install deps first (better caching)
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy service code
COPY . .

# Default port (change if your app uses a different one)
EXPOSE 8001

# Run with uvicorn (adjust module if needed, e.g. app.main:app)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
