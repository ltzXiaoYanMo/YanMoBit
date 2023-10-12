# 本文件仅为作为测试连通性连接
import requests

# https为一言api
koto = requests.get('https://v1.hitokoto.cn/?c=f&encode=text')

print(koto.text)
