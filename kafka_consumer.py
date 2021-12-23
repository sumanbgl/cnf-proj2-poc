from kafka import KafaConsumer
import json

TOPIC_NAME = 'orders'

consumer = KakfaConsumer(TOPIC_NAME,
                        value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    data = message.value
    print(data)
