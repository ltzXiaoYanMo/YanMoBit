# cloud.json到底怎么填
```json
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
  "openai_apikey": ""
```

这是cloud.json的配置文件，我们目前仅需要填写MySQL Redis设置即可

## MySQL
    
### MySQL_Pwd
数据库的密码

### MySQL_Port
数据库的端口

### MySQL_Host
数据库的IP地址，默认为localhost（本地环回地址）

### MySQL_db
数据库的名称

## Redis

### Redis_Host
Redis的IP地址，默认为localhost（本地环回地址）

### Redis_port
Redis的端口

### Redis_Pwd
Redis的密码

## OpenAI
 
### openai_api
chatgpt的api服务器

### openai_apikey
chatgpt的api服务器的key
