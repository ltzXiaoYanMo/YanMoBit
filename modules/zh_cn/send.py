# 项目Github源码:https://github.com/ltzXiaoYanMo/YanBot_KHB_Edition

# Mirai输出日志:023-07-31 12:09:17.762 | INFO | graia.ariadne.model:log:82 - 1373892821: [RECV][PythonGarbage(2315049216)] -> 1

from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

import globalvars

channel = Channel.current()
channel.name("发送私聊")
channel.description("貌似本质上就是为了私聊Bot制作人员？")
channel.author("ltzXiaoYanMo")

@channel.use(ListenerSchema(listening_events=[FriendMessage]))
async def friend_message(app: Ariadne, event: FriendMessage):
    if event.sender.id != globalvars.owner_qq:
        await app.send_friend_message(
            globalvars.owner_qq,
            MessageChain(
                Plain(f"消息来自：{event.sender.nickname} ({event.sender.id})\n消息内容：") + event.message_chain
            )
        )
        await app.send_friend_message(
            globalvars.owner_qq,
            MessageChain(
                "你可以使用!send <目标QQ> <消息>来发送私聊消息"
            )
        )
    elif event.sender.id == globalvars.owner_qq and event.message_chain.display.startswith("!send"):
        result = event.message_chain.removeprefix("!send ").split(" ")
        if len(result) >= 2:
            results = ""
            for i in range(1, len(result) - 1):
                if i == 1:
                    results = result[i]
                else:
                    results = results + " " + result[i]
            await app.send_friend_message(int(str(result[0])), results)
