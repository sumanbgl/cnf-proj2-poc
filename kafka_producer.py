from kafka import KafkaProducer
import json

TOPIC_NAME = 'orders'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

order_info = {"person_id":"5", "latitude":"90", "longitude":"100"}

producer.send('orders',json.dumps(order_info).encode('utf-8'))
producer.flush()


