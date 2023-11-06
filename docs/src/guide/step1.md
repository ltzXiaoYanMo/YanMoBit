---
title: 第 1 步：环境搭建
icon: info
---

本篇主要写了如何搭建必须的环境

# 观前须知

## 你知道你在看什么

这是 **部署文档** ，如果你是使用者，请移步 [使用指南 💡](/demo/)

## 你知道应该如何搜索

你知道如何正确选择并使用搜索引擎，如果不会也没有关系，我专门为此写了 [一篇文章](/question/how-to-search) 教你如何选择并使用搜索引擎

若您已经学会如何正确选择并使用搜索引擎，那么恭喜您！

若您已经学会如何正确选择并使用搜索引擎但仍然不熟练，没有关系，在本篇文档所有要求使用搜索引擎的部分，我都会附上一个“建议使用的关键词”，您可以直接复制这些关键词并搜索，以帮助您练习如何使用搜索引擎

# 必须有的

本小节默认你会安装如下软件：（请不要直接安装，读完再安装，有些提示在文章后面）

- Git
- Redis
- ~~MySQL~~（现已支持SQLite）
- MCL（这个工具可以自动帮你安装以下软件，详见后文）
  - Java
  - Mirai
  - MAH (Mirai-API-HTTP)
- Python
  - pdm

如果你不会安装，请自行学会使用搜索引擎后搜索 `xxx 安装`

比如 `Git 安装` ，

## 关于 Java、Mirai、MAH（MCL） 的安装

请参考 [GraiaX 文档的这个部分](https://graiax.cn/before/install_mirai.html)

## 关于 Redis、MySQL 的安装

如果你跟我一样 ~~非常懒~~ 那么你可以选择使用 Docker 安装，~~Redis请不要设置密码（记得堵好端口）~~ 现在没啥必要了

MySQL 建议使用 8.0.31 （我测试时使用的版本，当然也兼容 5.7 版本，你可以看心情选择）

Redis 建议使用支持 LFU 的版本，即 Redis 4.0 及以后（建议使用最新版本）

安装完 Redis 之后务必在配置文件中将缓存机制设置为 LFU

## 关于 Python 的安装

```text
Python Version >= 3.9
```

安装 pdm：

```shell
pip install pdm
```

## 如果你遇到 *pip下载慢* / *安装报错* / *找不到pip* / *Python版本错误*

您不会自己百度一下吗？

当你遇到报错时，不要慌，寻找重要信息复制粘贴到搜索引擎即可
比如 `'pip' 不是内部或外部命令，也不是可运行的程序或批处理文件。`

当你遇到一些问题时，你可以简短、抽象地描述问题，比如 `pip 慢`

# 下载 YMB 源码

```shell
git clone https://github.com/ltzXiaoYanMo/YanMoBit.git
```
国内加速
```bash
git clone https://gitee.com/ltzXiaoYanMo/YanMoBit.git
```

请务必使用 `git clone` 否则更新起来会很麻烦

如果 git 报错，通常是因为网络问题，请自行搜索 `git clone 加速`

# 依赖安装

```shell
pdm install
```

## 开发
```bash
pip install -r requirements.txt
```
就好辣！
