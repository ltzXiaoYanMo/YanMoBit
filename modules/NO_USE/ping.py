from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

import os

channel = Channel.current()
channel.name("Ping")
channel.description("PingPing你的")
channel.author("ltzXiaoYanMo")

result=os.system(MessageChain)
if result:
    MessageChain(os.system.ping(MessageChain))
    result = os.system(f"ping {MessageChain}")

# 检测群聊中的ping后面的IP/域名，直接使用os模块中的ping此域名/IP
@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def ping(app: Ariadne, group: Group, message: MessageChain):
    if message.has(DetectPrefix):
        return
    if message.has(MessageChain.At):
        return
    if message.has(MessageChain.Plain):
        if message.has(MessageChain.Plain, lambda m: m.text.startswith("ping")):
            return
        if message.has(MessageChain.Plain, lambda m: m.text.startswith("Ping")):
            return