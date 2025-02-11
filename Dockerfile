# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o script de entrypoint para o container
COPY entrypoint.sh /entrypoint.sh

# Tornar o script executável
RUN chmod +x /entrypoint.sh

# Definir o script como entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Expor a porta 8000 para o mundo exterior
EXPOSE 8000