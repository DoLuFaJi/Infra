from kafka import KafkaConsumer
consumer_out = KafkaConsumer('msg_out', bootstrap_servers='reception:9092', auto_offset_reset='smallest')
consumer_in = KafkaConsumer('msg_in', bootstrap_servers='reception:9092', auto_offset_reset='smallest')
print("start")
for msg in consumer_out:
	print("my messag")
	print(msg)
print("end")

