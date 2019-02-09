import redis

REDIS_HOST = "localhost"
REDIS_PORT = "6379"

class RedisConnector(metaclass=Singleton):
    def __init__(self):
        self.connection = redis.Redis(host=REDIS_HOST,
                                      port=REDIS_PORT)

    def get(self, key):
        return self.connection.get('foo')

    def put(self, key, value):
        return self.connection.set(key, value)