# Makefile

# Define the image name
IMAGE_NAME = berndverst/falcon

# Define the port mapping
HOST_PORT = 8080
CONTAINER_PORT = 80

# Default target
.PHONY: run

run:
	docker run -it -p $(HOST_PORT):$(CONTAINER_PORT) $(IMAGE_NAME)