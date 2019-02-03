import json

def stream_file_as_json(file):
    with open(file, 'r') as file:
        try:
            for line in file:
                parsed = json.loads(line)
                json_string = json.dumps(parsed)
                send_to_kafka(json_string)
        finally:
            file.close()

def send_to_kafka(json_string):
    print(json_string)