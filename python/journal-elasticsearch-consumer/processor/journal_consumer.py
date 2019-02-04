from kafka import KafkaConsumer
from journalconfig import config
from client import elasticsearch_client
import json

class JournalConsumer:
    def __init__(self):
        self.broker_uri = config.read_kafka_config()['broker_uri']
        self.elasticsearch_url = config.read_elasticsearch_config()['elasticsearch_url']
        self.elasticsearch_journal_index = config.read_elasticsearch_config()['elasticsearch_journal_index']

    def start(self):
        print()
        consumer = KafkaConsumer(bootstrap_servers=[self.broker_uri],
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000)
        
        consumer.subscribe(['elite-journal'])

        for message in consumer:
            data = json.loads(message.value)
            elasticsearch_client.post(f'{self.elasticsearch_url}/{self.elasticsearch_journal_index}/_doc', data)

        consumer.close()