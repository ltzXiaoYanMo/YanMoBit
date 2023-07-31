# 项目Github源码:https://github.com/ltzXiaoYanMo/YanBot_KHB_Edition

# Mirai输出日志:023-07-31 12:09:17.762 | INFO | graia.ariadne.model:log:82 - 1373892821: [RECV][PythonGarbage(2315049216)] -> 1

from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage, FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At, Plain, Image
from graia.broadcast import Broadcast
from graia.saya import Channel, Saya
from graia.saya.builtins.broadcast import ListenerSchema
from modules import globalvars

saya = Saya.current()
channel = Channel.current()
bcc = create(Broadcast)

channel = Channel.current()
channel.name("发送私聊")
channel.description("貌似本质上就是为了私聊Bot制作人员？")
channel.author("ltzXiaoYanMo")

# @channel.use(ListenerSchema(listening_events=[FriendMessage])) 源自2kbit-py
@channel.use(ListenerSchema(listening_events=[GroupMessage, NudgeEvent]))
async def friend_message(app: Ariadne, event: FriendMessage):
    if not event.sender.id == globalvars.owner_qq:
        messageChain = (Plain(f"消息来自：{event.sender.nickname} ({event.sender.id})\n消息内容："))
        for message in event.message_chain:
            messageChain.__add__(message)
        await app.send_friend_message(globalvars.owner_qq, messageChain)
        await app.send_friend_message(
            globalvars.owner_qq,
            MessageChain(
                "你可以使!send <目标QQ> <消息>来发送私聊消息"
            )
        )
    elif event.sender.id == globalvars.owner_qq and event.message_chain.startswith("!send"):
        result = event.message_chain.removeprefix("!send ").split(" ")
        if len(result) >= 2:
            try:
                results = ""
                for i in range (1, len(result) - 1):
                    if i == 1:
                        results = result[i]
                    else:
                        results = results + " " + result[i]
                try:
                    await app.send_friend_message(int(str(result[0])), results)
                except:
                    await app.send_friend_message(event.sender.id, "私聊消息发送失败")
            except:
                await app.send_friend_message(event.sender.id, "参数错误")
