# Prerequisites
## Download files 
>`./reception/download.sh`

## Install docker
>`sudo apt install docker.io`
>`sudo apt install docker-compose`

# Run the application
>`sudo ./launch.sh`
Open your application on `http://localhost:8081/`

# Commands to run dockers
Here a list of commands to use dockers.

## Build all docker
>`sudo docker-compose build`

## Run all docker
>`sudo docker-compose up`

## List running docker
>`sudo docker-compose ps`

## Get a bash in a container
>`sudo docker-compose exec nom_service bash`
