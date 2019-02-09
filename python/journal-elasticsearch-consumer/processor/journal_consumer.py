from kafka import KafkaConsumer
from journalconfig import config
from client import elasticsearch_client
import json
import time

class JournalConsumer:
    def __init__(self):
        self.broker_uri = config.read_kafka_config()['broker_uri']
        self.elasticsearch_url = config.read_elasticsearch_config()['elasticsearch_url']
        self.elasticsearch_journal_index = config.read_elasticsearch_config()['elasticsearch_journal_index']
        self.consumer = KafkaConsumer(bootstrap_servers=[self.broker_uri],
                                      enable_auto_commit=True,
                                      auto_offset_reset='earliest',
                                      group_id='journal-es-consumer',
                                      consumer_timeout_ms=1000)
        

    def start(self):
        self.consumer.subscribe(['elite-journal'])

        try:
            while True:
                for message in self.consumer:
                    print("Consuming messages...")
                    data = json.loads(message.value)
                    response_status_code = elasticsearch_client.post(f'{self.elasticsearch_url}/{self.elasticsearch_journal_index}/_doc', data).status_code
                    print(f'{message}: {response_status_code}')

                time.sleep(5)

        except KeyboardInterrupt:
            self.consumer.close()
            print('Stopped consumer...')
        