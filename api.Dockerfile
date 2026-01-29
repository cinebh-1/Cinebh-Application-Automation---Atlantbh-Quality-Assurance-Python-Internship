FROM python:3.11-slim

WORKDIR /tests

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy test code
COPY . .

# Default command: API tests only
CMD ["python", "-m", "pytest", "tests/API_tests", "-s"]
