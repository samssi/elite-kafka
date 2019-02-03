from kafka import KafkaProducer
from journalconfig import config
import json

kafka_config = config.read_kafka_config()
broker_uri = kafka_config['broker_uri']
elite_journal_topic = kafka_config['journal_topic']

producer = KafkaProducer(bootstrap_servers=[broker_uri])

def stream_file_as_json(file):
    with open(file, 'r') as file:
        try:
            for line in file:
                parsed = json.loads(line)
                json_string = json.dumps(parsed).encode('utf-8')
                send_to_kafka(json_string)
        finally:
            file.close()

def send_to_kafka(json_string):
    print(f'Sending to topic "{elite_journal_topic}": {json_string}')    
    producer.send(elite_journal_topic, json_string)