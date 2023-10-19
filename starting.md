# 此篇文章年代较久远，可追溯到YanBot-Older时期，具体文章和现代YanBot有出入，此篇文章如有问题可提Issue
## 安装依赖

首先，YanBot的所有版本都以Python编写，且KHB的Python版本>=3.10，<del>OpenMariya的Python>=3.11且双方获取模块方式不一样，这里是KHB的方式</del>。OM的版本也没了（

我建议部署此Bot的时候，可以使用git此仓库（或者fork到自己仓库进行git clone）

安装git的方式：

Windows:
```PowerShell
winget install Git.Git
```
Debian/Ubuntu:
```bash
sudo apt-get install -y git
```

CentOS/Red Hat:
```bash
sudo yum install -y git
```
dnf:
```bash
sudo dnf install -y git
```
安装pdm，输入以下字符安装pdm
Windows:
```PowerShell
pip install pdm
```

Linux:
```bash
pip3 install pdm 
```
或
```bash
pip3.11 install pdm
```
若未安装pip，在此目录下输入:
Windows:
```bash
python get-pip.py
```
Linux：
```bash
python3 get-pip.py 或 pip3.11 get-pip.py
```
安装完毕后，进入YanBot的目录，输入pdm install（数据支持来自Bugji，也就是括弧）<del>里面的numba和支持库因源已停止更新</del>在最新版中已经完全支持Python3.11，且无需安装也能正常使用。所以打“X”也无需慌张。此刻你已经安装完毕了依赖。（若你未处于中国大陆，在使用pip安装完pdm之后，输入pdm config pypi.url https://pypi.org/simple来更换原版pip源）

## 安装QQBot支持-Mirai Console Loader

这个其实挺简单的，特别是Linux用户，iTXTech已经做出了一站式服务，你只需要在GitHub上找到MCL一键安装程序，且找到适用于你操作系统版本的程序即可完成安装。

### 安装Mirai Console Loader HTTP依赖-MAH（Mirai API HTTP）

因为QQBot的依赖是需要Mirai的模块-MAH，所以我们需要去GitHub处找到MAH的Java程序文件，也就是.jar文件。安装在MCL的plugin目录中，启动MCL，使MAH创建配置文件。

创建完成后，你可以在config目录中找到MAH的配置文件，也就是net.mamoe.mirai-api-http。根据GraiaX的文档中，我们需要打开setting.yaml文件。且更改为以下字符： 
```yaml
adapters:
- http
- ws
debug: false
enableVerify: true
verifyKey: GraiaxVerifyKey # 你可以自己设定，这里作为示范
singleMode: false
cacheSize: 4096
adapterSettings:
http:
    host: localhost
    port: 8080
    cors: [*]
ws:
    host: localhost
    port: 8080
    reservedSyncId: -1
```
则MAH的配置文件部署完毕。

## 配置YanBot
    
YanBot与KuoHuBit的配置其实都很简单，都是更改cloud.json和config.yaml。最新版本当中需运行main.py才可出现cloud.json文件。<del>不然怎么会说基于KuoHuBit呢。</del>

这边注意下，cloud.json仅支持MySQL，<del>用户也仅支持root</del>，在新版中已经支持其他用户；config.yaml的色图功能需在/modules/zh-cn/setu.py和/modules/zh-cht/setu.py这俩Python可执行文件删除即可关闭。

在最新版的YanBot当中，你需要在globalvars.py填写bot_qq和owner_qq这两个必要数据

## 配置结束，启动和使用YanBot

打开Mirai登录你的QQ号即可，但前提在启动MCL前，你看到了以下字符 

```mirai
2022-07-04 19:11:11 I/Mirai HTTP API: ********************************************************
2022-07-04 19:11:12 I/http adapter: >>> [http adapter] is listening at http://localhost:8080
2022-07-04 19:11:12 I/ws adapter: >>> [ws adapter] is listening at ws://localhost:8080
2022-07-04 19:11:12 I/Mirai HTTP API: Http api server is running with verifyKey: GraiaxVerifyKey
2022-07-04 19:11:12 I/Mirai HTTP API: adaptors: [http,ws]
2022-07-04 19:11:12 I/Mirai HTTP API: ********************************************************
```
此处无需完全一样

如果看见，则成功启动了MAH。

在YanBot的设置中，也只需要控制台中输入以下字符

Windows：
```PowerShell
pdm run python main.py
```
Linux：
```bash
pdm run python3 main.py 或 pdm run python3.11 main.py
```

如果出现SUCCESS，则成功与Mirai连接。
