import random
import requests

api_list = ['http://api.qemao.com/api/yulu/?type=2', 'http://api.qhsou.com/api/zuan.php']

choose = random.choice(api_list)

data = requests.get(choose)

print(data.text)
