import os
from consumerconfig import consumerconfig

def project_root_directory():
    return os.path.dirname(os.path.realpath(__file__))

def settings_file(filename):
    return f'{project_root_directory()}/settings/{filename}'
