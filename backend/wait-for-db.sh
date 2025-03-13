#!/bin/sh
# Wait until PostgreSQL is ready using pg_isready
while ! pg_isready -h db -p 5432 -q; do
  sleep 1
  echo "Waiting for PostgreSQL..."
done
echo "PostgreSQL is ready - starting application"