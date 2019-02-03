def stream_file_as_json(file):
    with open(file, 'r') as file:
        try:
            for line in file:
                print(line)
        finally:
            file.close()