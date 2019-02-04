import requests

def post(url, json):
    try:
        response = requests.post(url, json=json)
        return response
    
    except requests.exceptions.RequestException as re:
        print(str(re))