# Makefile for Docker Compose

# Default target
bash:
	docker exec -it falcon-app /bin/bash


build:
	docker-compose build app

up:
	docker-compose up app

upbuild:
	docker-compose up app --build

restart:
	docker-compose restart app

down:
	docker-compose down

postgresdb:
	docker-compose exec db psql -U myuser -d mydatabase

test:
	ENVIRONMENT=test docker-compose up app -d
	make bash