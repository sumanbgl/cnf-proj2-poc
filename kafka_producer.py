from kafka import KafkaProducer
import json

TOPIC_NAME = 'orders'
KAFKA_SERVER = 'localhost:9092'

producer = KakfaProducer(bootstrap_servers=KAFKA_SERVER, 
                        value_serializer=lambda v : dumps(v).encode('utf-8'))

order_info = {"person_id":"5", "latitude":"90", "longitude":"100"}

producer.send('orders', value=order_info)
producer.flush()


