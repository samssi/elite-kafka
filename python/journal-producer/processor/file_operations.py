def read_file_as_json(file):
    print(f'Read: {file}')

    file = open(file, 'r')
    try:
        for line in file:
            print(line)
    finally:
        file.close()