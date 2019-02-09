from consumerconfig import consumerconfig
from consumer import config_consumer

def main():
    pass
    
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

if __name__ == "__main__":
    configConsumer = config_consumer.ConfigRedisConsumer()
    configConsumer.start()