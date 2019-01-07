from kafka import KafkaConsumer
consumer = KafkaConsumer('msg_out', bootstrap_servers='reception:9092', auto_offset_reset='smallest')
for msg in consumer:
	print(msg)
