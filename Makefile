# Define variables
IMAGE_NAME = webapp_pub_rtsp
CONTAINER_NAME = webapp_pub_rtsp

# Target to build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Target to run the Docker container
run:
	docker run -d -p 8081:5000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Target to stop and remove the Docker container
clean:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true
