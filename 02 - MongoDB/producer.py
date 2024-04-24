import json
from kafka import KafkaProducer
from datetime import datetime
from time import sleep
from random import choice

kafkaServer = 'localhost:9092'
topic = 'mensajesTC2'
producer = KafkaProducer(bootstrap_servers=kafkaServer, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

randomValues = [1, 2, 3, 4, 5, 6, 7]
while True:
    randomValues = choice(randomValues)
    data = {
        "test_data": {
            "randomValues" : randomValues
        },
        'timestamp': str(datetime.now()),
        'value_status': 'alto' if randomValues > 4 else 'bajo'
    }
    print(data)
    producer.send(topic, data)
    producer.flush()
    sleep(2)