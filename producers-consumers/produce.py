from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='172.17.0.1:9092')
for _ in range(100):
	producer.send('foobar', b'some_message_bytes')

