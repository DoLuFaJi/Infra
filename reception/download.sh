#! /bin/bash
wget http://apache.crihan.fr/dist/kafka/2.1.0/kafka_2.11-2.1.0.tgz
tar -xzf kafka_2.11-2.1.0.tgz
mv kafka_2.11-2.1.0 ./reception/kafka_2.11-2.1.0
rm kafka_2.11-2.1.0.tgz

