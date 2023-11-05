import requests
import json

CloudStatus = 'https://www.cloudflarestatus.com/api/v2/status.json'

print(requests.get(CloudStatus).json()['status'])
