from kafka import KafkaConsumer
consumer = KafkaConsumer('foobar', bootstrap_servers='reception:9092', auto_offset_reset='smallest')
for msg in consumer:
	print(msg)
