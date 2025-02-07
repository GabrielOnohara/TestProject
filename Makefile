# Makefile for Docker Compose

# Default target
up:
	docker-compose up --build

# Optional target to stop and remove containers
down:
	docker-compose down

postgresdb:
	docker-compose exec db psql -U myuser -d mydatabase