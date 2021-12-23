from kafka import KafkaConsumer
import json

TOPIC_NAME = 'orders'

consumer = KafkaConsumer(TOPIC_NAME,
                        value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    data = message.value
    print(data)
