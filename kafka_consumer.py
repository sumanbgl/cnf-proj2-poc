from kafka import KafkaConsumer


TOPIC_NAME = 'items'

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    text = message.decode('utf-8')
    print (text)
