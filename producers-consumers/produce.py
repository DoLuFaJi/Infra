from kafka import KafkaProducer
# 172.18.0.1
producer = KafkaProducer(bootstrap_servers='reception:9092')
for _ in range(100):
	future = producer.send('foobar', 'biite'.encode('utf8'))
	result = future.get(timeout=60)
	print(result)

metrics = producer.metrics()
print(metrics)
