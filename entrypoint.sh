#!/bin/bash

# Rodar as migrações do Alembic
alembic upgrade head

# Iniciar o Gunicorn
exec gunicorn -b 0.0.0.0:8000 --reload app:app