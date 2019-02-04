import os
from journalconfig import config

def project_root_directory():
    return os.path.dirname(os.path.realpath(__file__))

def settings_file(filename):
    return f'{project_root_directory()}/settings/{filename}'
