import requests
import json

CloudStatus = 'https://www.cloudflarestatus.com/api/v2/summary.json'

print(requests.get(json.loads(requests.get(CloudStatus).text)['components'][0]['name']))
