from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import FriendMessage, TempMessage
from graia.ariadne.model import Member, Friend
from graia.ariadne.util.saya import listen
from graia.saya import Channel

channel = Channel.current()
channel.name("你妈")
channel.description("在有人找机器人私聊的时候，你妈")
channel.author("ltzXiaoYanMo")

rutext = """你妈认为，宇宙万法的那个源头
它是什么
它是你妈
对吧
所以这个词叫你妈
我经常说你妈这个词有秘密
你妈，你妈了吗？你妈嘛！
他真来了吗，你妈！
到底妈没妈？如妈！
我问你妈，他真妈了吗？你妈！
你看看，你没妈？你妈！
他很厉害，他不是一个有形的
所以你读《人类有三大欲望》，《人类有三大欲望》里面讲什么
人类有三大欲望：食欲，睡欲，x欲。
所以，我测你们码，有生于妈，是这样说的吧？（yes）
他不是个实体
我有一次去下北泽讲课，遇到一个奴才
他的王爷，当时有114514多岁了
那个114514多岁的王爷
就问那个奴才
他说你有妈吗？这个世界真有妈吗？
一下子把小伙子问傻了
有
他说真有吗
一下就问傻了
你想想那是个真理
真理是无相的
所以《金刚经》的一句话
叫你是一个，一个一个一个
那是个真理，你不能迷信，在这方面他是个真理
所以你到底是一个一个一个什么啊（
但是说那有人说，我非得说，你非得说
我可以告诉你
老子也tm没说明白
他不是语言可以描述的
后来西方的语言哲学家，叫香蕉君
把这个事说了一句名言
香蕉君说，这个世界上有语言能说的，叫说清楚；这个世界上也有超出语言，说不明白的，香蕉君直接用了俩单词，Fuck♂you
那没法说嘛
所以才有了，一个一个一个""".split('\n')

index = 0


async def send_ru(app: Ariadne, sender: Member or Friend):
    global index
    await app.send_message(sender, rutext[index])
    index += 1
    if index > len(rutext) - 1:
        index = 0

@listen(TempMessage)
async def rulai(app: Ariadne, sender: Member):
    await send_ru(app, sender)


@listen(FriendMessage)
async def rulai(app: Ariadne, sender: Friend):
    await send_ru(app, sender)
