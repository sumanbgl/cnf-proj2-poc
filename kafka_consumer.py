from kafka import KafkaConsumer
from json import loads

TOPIC_NAME = 'orders'

consumer = KafkaConsumer(TOPIC_NAME,
                        value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    data = message.value
    print(data)
