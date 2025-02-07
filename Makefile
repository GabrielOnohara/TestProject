# Makefile for Docker Compose

# Default target
bash:
	docker exec -it falcon-app /bin/bash


build:
	docker-compose build app

up:
	docker-compose up app --build

restart:
	docker-compose restart app

# Optional target to stop and remove containers
down:
	docker-compose down

postgresdb:
	docker-compose exec db psql -U myuser -d mydatabase