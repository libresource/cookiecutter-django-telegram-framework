#!/bin/bash

set -e  # Остановить выполнение при ошибке

echo "🧩 Installing dependencies..."
pip install -r requirements.txt
pip install -r dev-requirements.txt

echo "🐘 Starting PostgreSQL via Docker Compose..."
docker compose up -d pg

echo "⏳ Waiting for PostgreSQL to be ready..."
sleep 10  # при необходимости заменить на healthcheck или wait-for-it

echo "🧬 Applying migrations..."
python manage.py migrate

echo "👤 Creating admin user..."
python manage.py create_admin

echo "✅ Running tests with coverage..."
make coverage

echo "🔍 Running linter..."
make lint

echo "🎉 Done!"
