#! /bin/bash
docker-compose up --force-recreate -d reception
docker-compose up -d entry
docker-compose up -d source
docker-compose up -d historisation
docker-compose up -d traitement_task
