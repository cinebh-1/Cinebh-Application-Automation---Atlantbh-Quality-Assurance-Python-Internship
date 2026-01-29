# Official Playwright image with Python + browsers installed
FROM mcr.microsoft.com/playwright/python:v1.57.0-jammy

# Prevent Python buffering (better logs in CI)
ENV PYTHONUNBUFFERED=1


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers (safe even if image already has them)
RUN playwright install --with-deps


COPY . .

CMD ["python", "-m", "pytest", "tests/UI_tests", "-s"]

