# Install docker
sudo apt install docker.io
sudo apt install docker-compose

# Run all docker
sudo docker-compose up

# List running docker
sudo docker-compose ps

# Get a bash in a container
sudo docker-compose run nom_service bash
