from pathlib import Path
import os
import paths
import re
from config import config

journal_file_pattern = "Journal.[0-9]{12}.[0-9]{2}.log"

def list_journal_files():
    process_directory = paths.process_directory()
    files = sorted(os.listdir(process_directory))
    
    journal_files = list(filter(lambda file : re.match(journal_file_pattern, file), files))
    return journal_files

def home_directory():
    return str(Path.home())

def process_directory():
    return config.read_journal_data_config()['process_directory']

def project_root_directory():
    return os.path.dirname(os.path.realpath(__file__))

def settings_file(filename):
    return f'{project_root_directory()}/settings/{filename}'
