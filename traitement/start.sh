#!/bin/bash
/opt/flink/bin/start-cluster.sh
bin/flink run -c tr.MainTraitement /code/traitement-1.0-SNAPSHOT.jar
