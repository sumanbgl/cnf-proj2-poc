from kafka import KafaProducer

TOPIC_NAME = 'orders'
KAFKA_SERVER = 'localhost:9092'

producer = KakfaProducer(bootstrap_servers=KAFKA_SERVER)

order_info = '{"person_id":"5", "latitude":"90", "longitude":"100"}'

producer.send('orders',order_info)
producer.flush()


