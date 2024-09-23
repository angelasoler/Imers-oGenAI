#!/usr/bin/env python3.10

import sys
import requests
import json
import wikitextparser as wtp

result_file =  "nome_da_busca.wiki"

def put_on_file(result):
    file = open(result_file, "w")
    file.write(result)
    file.close

def search_term(research):
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srsearch': research
    }
    response = requests.get(f'http://pt.wikipedia.org/w/api.php', params=params)
    if (response.status_code != 200):
        print(f'Unsuccesful request')
        sys.exit(1)

    API_Data = response.json()

    try:
        ret = API_Data['query']['search'][0]['snippet']
    except (KeyError, IndexError):
        print("Term not found")
        sys.exit(1)

    result = wtp.parse(ret)
    put_on_file(result.plain_text())

if __name__ == "__main__":
    if (len(sys.argv) > 2 or len(sys.argv) == 1):
        print('Use: ./request_wikipedia.py "<research>"')
        sys.exit(1)
    search_term(sys.argv[1])

