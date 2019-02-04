from kafka import KafkaConsumer
from journalconfig import config
import json

broker_uri = config.read_kafka_config()['broker_uri']

class JournalConsumer:
    def __init__(self):
        pass

    def start(self):
        print()
        consumer = KafkaConsumer(bootstrap_servers=[broker_uri],
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000)
        
        consumer.subscribe(['elite-journal'])

        for message in consumer:
            data = json.loads(message.value)
            print(f'{data}\n')

        consumer.close()