docker-compose exec traitement_task bash

bin/flink run -c tr.MainTraitement /code/traitement-1.0-SNAPSHOT.jar
