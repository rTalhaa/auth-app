FROM python:3.9-slim

# Install PostgreSQL client for health checks
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY wait-for-db.sh .
RUN chmod +x wait-for-db.sh

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["./wait-for-db.sh", "flask", "run"]