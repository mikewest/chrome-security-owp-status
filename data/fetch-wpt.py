import requests
import json
from pprint import pprint

response = requests.get('https://wpt.fyi/api/run?browser=chrome&sha=latest')
data = json.loads(response.content)

response = requests.get(data['results_url'])
data = json.loads(response.content)

summary = {}
for k, v in data.items():
    directory = k[1:k.find('/', 1)]
    if (directory not in summary):
        summary[directory] = [0,0]
    summary[directory][0] += v[0]
    summary[directory][1] += v[1]

pprint(summary)
