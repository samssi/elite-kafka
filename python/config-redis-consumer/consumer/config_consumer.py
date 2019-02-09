import kafka
import redis
from consumerconfig import consumerconfig
import json
import time

REDIS_HOST = consumerconfig.read_redis_config()['redis_host']
REDIS_PORT = consumerconfig.read_redis_config()['redis_port']

BROKER_URI = consumerconfig.read_kafka_config()['broker_uri']
JOURNAL_TOPIC = consumerconfig.read_kafka_config()['journal_topic']
ENABLE_AUTO_COMMIT = consumerconfig.read_kafka_config()['enable_auto_commit']
AUTO_OFFSET_RESET = consumerconfig.read_kafka_config()['auto_offset_reset']
GROUP_ID = consumerconfig.read_kafka_config()['group_id']
CONSUMER_TIMEOUT_MS = int(consumerconfig.read_kafka_config()['consumer_timeout_ms'])
TOPIC = consumerconfig.read_kafka_config()['topic']
CONSUMER_WAIT_SEC = int(consumerconfig.read_kafka_config()['consumer_wait_sec'])

class ConfigRedisConsumer:
    def __init__(self):
        pass
        
    def start(self):
        self.redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        self.consumer = kafka.KafkaConsumer(bootstrap_servers=[BROKER_URI],
                                            enable_auto_commit=ENABLE_AUTO_COMMIT,
                                            auto_offset_reset=AUTO_OFFSET_RESET,
                                            group_id=GROUP_ID,
                                            consumer_timeout_ms=CONSUMER_TIMEOUT_MS)

        self.consumer.subscribe(TOPIC)
        self._consume()

    def _consume(self):
        print("Starting config consumer...")
        try:
            while True:
                for message in self.consumer:
                    message_json = self._parse_json_message(message)
                    if message_json is not None:
                        print(message_json)
                        self._put_to_redis(message_json)
                    
                time.sleep(CONSUMER_WAIT_SEC)

        except KeyboardInterrupt:
            self.consumer.close()
            print('Stopped consumer...')

    def _parse_json_message(self, message):
        try:
            return json.loads(message.value)

        except json.JSONDecodeError:
            print("error")
            return None

    def _put_to_redis(self, message_json):
        self.redis.set(message_json['key'], message_json['value'])