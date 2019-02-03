from kafka import KafkaProducer
from processor.journal_processor import JournalProcessor
import paths

def main():
    journalProcessor = JournalProcessor(paths.list_journal_files())
    journalProcessor.start()
    

if __name__ == "__main__":
    main()