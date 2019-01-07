#! /bin/bash
docker-compose up --force-recreate -d reception
docker-compose up -d entry
docker-compose up -d source
