import asyncio
import json
import sys

import aiomysql
import portalocker
import redis
import requests_cache
import yaml
from loguru import logger


def safe_file_read(filename: str, encode: str = "UTF-8", mode: str = "r") -> str or bytes:
    if mode == 'r':
        with open(filename, mode, encoding=encode) as file:
            portalocker.lock(file, portalocker.LOCK_EX)
            tmp = file.read()
            portalocker.unlock(file)
    else:
        with open(filename, mode) as file:
            portalocker.lock(file, portalocker.LOCK_EX)
            tmp = file.read()
            portalocker.unlock(file)

    return tmp


def safe_file_write(filename: str, s, mode: str = "w", encode: str = "UTF-8"):
    if 'b' not in mode:
        with open(filename, mode, encoding=encode) as file:
            portalocker.lock(file, portalocker.LOCK_EX)
            file.write(s)
            portalocker.unlock(file)
    else:
        with open(filename, mode) as file:
            portalocker.lock(file, portalocker.LOCK_EX)
            file.write(s)
            portalocker.unlock(file)


loop = asyncio.get_event_loop()
try:
    config_yaml = yaml.load(open('config.yaml', encoding='UTF-8'), Loader=yaml.FullLoader)
except FileNotFoundError:
    safe_file_write('config.yaml', """qq: 114514  # 运行时登录的 QQ 号
verifyKey: "GraiaXVerifyKey"  # MAH 的 verifyKey
recall: 5  # 涩图撤回等待时长（单位：秒）
# 如果你没有那么多涩图API可以填一样的URL
setu_api: "https://api.jiecs.top/lolicon?r18=2"  # 涩图 API
setu_api2: "https://www.acy.moe/api/r18"   # 涩图 API 2
setu_api2_probability: 5 # 表示【涩图 API 2】的被调用的概率为 1/n
NewFriendRequestEvent: true  # 是否自动通过好友添加：true -> 自动通过 | false -> 自动拒绝  
BotInvitedJoinGroupRequestEvent: true  # 是否自动通过加群邀请：同上
mirai_api_http: "http://localhost:8080"  # 连接到 MAH 的地址
count_ban: 4  # 木鱼调用频率限制
# 注意：腾讯云内容安全 API 收费为 0.0025/条
text_review: false  # 是否使用腾讯云内容安全 API 对文本内容进行审核：true -> 是 | false -> 否，使用本地敏感词库
# 请参考此文章就近设置地域：https://cloud.tencent.com/document/api/1124/51864#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8
Region: ap-hongkong  # 使用香港地区 API
enable_mysql: false  # 是否使用MySQL存储数据 true -> 是 | false -> 否
oneword: https://v1.hitokoto.cn/?c=f&encode=text # 一言api
zuan_api: https://api.qhsou.com/api/zuan.php # 祖安 API
zuan_api2: http://api.qemao.com/api/yulu/?type=2 # 祖安 API 2
    """)
    logger.error(
        'config.yaml 文件不存在，已生成默认配置文件，请修改后重新运行。'
    )
    sys.exit(1)

try:
    cloud_config_json = json.load(open('cloud.json', 'r', encoding='UTF-8'))
except FileNotFoundError:
    safe_file_write('cloud.json', """{
  "QCloud_Secret_id": "",
  "QCloud_Secret_key": "",
  "MySQL_Pwd": "",
  "MySQL_Port": 3306,
  "MySQL_Host": "localhost",
  "MySQL_db": "",
  "MySQL_User": "root",
  "Redis_Host": "localhost",
  "Redis_port": 6379,
  "Redis_Pwd": "",
  "snao_key": "",
  "openai_api": "",
  "openai_apikey": "",
  "hfish_apikey": "",
  "Cloudflarestatus_api": "https://www.cloudflarestatus.com/api/v2/status.json"
}""")
    logger.error(
        'cloud.json 未创建，程序已自动创建，请参考仓库目录下的 cloud.json.md 填写该文件的内容')
    sys.exit(1)
try:
    dyn_yaml = yaml.safe_load(open('dynamic_config.yaml', 'r', encoding='UTF-8'))
except FileNotFoundError:
    safe_file_write('dynamic_config.yaml', """mute:
- null
word:
- null
img:
- null""")
    logger.warning('dynamic_config.yaml 已被程序自动创建')

try:
    jieba_words = open("jieba_words.txt", "r", encoding='utf-8')
except FileNotFoundError:
    safe_file_write('jieba_words.txt', """傻逼
你妈
""")


def get_config(name: str):
    try:
        return config_yaml[name]
    except KeyError:
        logger.error(f'{name} 在配置文件中找不到')
        return None


def get_cloud_config(name: str):
    try:
        return cloud_config_json[name]
    except KeyError:
        logger.error(f'{name} 在配置文件中找不到')
        return ""


def get_dyn_config(name: str):
    try:
        return dyn_yaml[name]
    except KeyError:
        logger.error(f'{name} 在配置文件中找不到')
        return []


async def select_fetchone(sql, arg=None):
    conn = await aiomysql.connect(host=get_cloud_config('MySQL_Host'),
                                  port=get_cloud_config('MySQL_Port'),
                                  user=get_cloud_config('MySQL_User'),
                                  password=get_cloud_config('MySQL_Pwd'), charset='utf8mb4',
                                  db=get_cloud_config('MySQL_db'), loop=loop)

    cur = await conn.cursor()
    if arg:
        await cur.execute(sql, arg)
    else:
        await cur.execute(sql)
    result = await cur.fetchone()
    await cur.close()
    conn.close()
    return result


async def select_fetchall(sql, arg=None):
    conn = await aiomysql.connect(host=get_cloud_config('MySQL_Host'),
                                  port=get_cloud_config('MySQL_Port'),
                                  user=get_cloud_config('MySQL_User'),
                                  password=get_cloud_config('MySQL_Pwd'), charset='utf8mb4',
                                  db=get_cloud_config('MySQL_db'), loop=loop)

    cur = await conn.cursor()
    if arg:
        await cur.execute(sql, arg)
    else:
        await cur.execute(sql)
    result = await cur.fetchall()
    await cur.close()
    conn.close()
    return result


async def run_sql(sql, arg):
    conn = await aiomysql.connect(host=get_cloud_config('MySQL_Host'),
                                  port=get_cloud_config('MySQL_Port'),
                                  user=get_cloud_config('MySQL_User'),
                                  password=get_cloud_config('MySQL_Pwd'), charset='utf8mb4',
                                  db=get_cloud_config('MySQL_db'), loop=loop)

    cur = await conn.cursor()
    await cur.execute(sql, arg)
    await cur.execute("commit")
    await cur.close()
    conn.close()


async def get_all_admin() -> list:
    tmp = await select_fetchall("SELECT uid FROM admin")
    t = []
    for i in tmp:
        t.append(i[0])
    logger.debug(t)
    return list(t)


async def get_all_sb() -> list:
    tmp = await select_fetchall('SELECT uid FROM blacklist')
    t = []
    for i in tmp:
        t.append(i[0])
    return t


if get_cloud_config("Redis_Pwd") is not None:
    backend = requests_cache.RedisCache(
        host=get_cloud_config('Redis_Host'),
        port=get_cloud_config('Redis_port'),
        password=get_cloud_config('Redis_Pwd')
    )
    p = redis.ConnectionPool(
        host=get_cloud_config('Redis_Host'),
        port=get_cloud_config('Redis_port'),
        password=get_cloud_config('Redis_Pwd')
    )
else:
    backend = requests_cache.RedisCache(
        host=get_cloud_config('Redis_Host'),
        port=get_cloud_config('Redis_port')
    )
    p = redis.ConnectionPool(
        host=get_cloud_config('Redis_Host'),
        port=get_cloud_config('Redis_port')
    )
session = requests_cache.CachedSession("global_session", backend=backend, expire_after=360)
r = redis.Redis(connection_pool=p, decode_responses=True)

