import requests
import json
import pprint

address='Address'

request = requests.get(f'https://ipinfo.io/{address}/json/').json()

pprint.pprint(request)
