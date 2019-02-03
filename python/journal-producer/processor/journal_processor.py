from processor import file_operations

class JournalProcessor:
    def __init__(self, files):
        self.files = files

    def start(self):
        for file in self.files:
            file_operations.stream_file_as_json(file)