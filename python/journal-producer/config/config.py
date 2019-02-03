import configparser
import paths
parser = configparser.SafeConfigParser()

def read_journal_data_config():
    parser.read(paths.settings_file('default.ini'))
    return parser['journal-data']
    