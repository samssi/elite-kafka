from processor.journal_consumer import JournalConsumer
import paths

def main():
    journalConsumer = JournalConsumer()
    journalConsumer.start()
    

if __name__ == "__main__":
    main()