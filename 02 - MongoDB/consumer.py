from kafka import KafkaConsumer
import json
# consumer

KafkaServer = 'localhost:9092'
topic = "mensajesTC2"
consumer = KafkaConsumer(bootstrap_servers='localhost:9092', value_deserializer=lambda m: json.loads(m.decode('utf-8')), auto_offset_reset='latest')
consumer.subscribe(topic)

while True:
    data = next(consumer)
    print(data.value)
    print(data)
