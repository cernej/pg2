import sys
import requests
import json


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} prefix')
        sys.exit()

    prefix = sys.argv[1]
    print(f'Download models for prefix: {prefix}')

    response = requests.get(f'https://data.carnewschina.com/suggest?q={prefix}')

    if not response.ok:
        print(f'Nastala chyba: {response.status_code}')
        sys.exit()
    
    data = json.loads(response.text)
    for model in data['models']:
        print(model['name'])