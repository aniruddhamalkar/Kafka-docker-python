from kafka import KafkaProducer
from time import sleep
import json
from datetime import datetime

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10, 1))
producer.send('youtube', b'Hello kafka')
now = datetime.now()
current_time = now.strftime("%d/%m/%Y %H:%M:%S")
for i in range(10):
    message = "Message {}".format(str(datetime.now().time()))
    producer.send('youtube', json.dumps(message).encode('utf-8'))
    sleep(2)
    print("message sent", i)
