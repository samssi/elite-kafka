import configparser
import paths

parser = configparser.SafeConfigParser()
default_file = 'default.ini'
config_file = parser.read(paths.settings_file(default_file))
    
def read_kafka_config():
    return parser['kafka']

def read_redis_config():
    return parser['redis']