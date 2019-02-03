import configparser
import paths

parser = configparser.SafeConfigParser()
default_file = 'default.ini'

def read_journal_data_config():
    parser.read(paths.settings_file(default_file))
    return parser['journal-data']
    
def read_kafka_config():
    parser.read(paths.settings_file(default_file))
    return parser['kafka']