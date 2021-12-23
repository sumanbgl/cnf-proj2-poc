from kafka import KakfaConsumer

TOPIC_NAME = 'orders'

consumer = KakfaConsumer(TOPIC_NAME)

for message in consumer:
    print(message)
