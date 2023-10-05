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

# 检测群聊中的ping后面的IP/域名，直接使用os模块中的ping此域名/IP
@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def ping(app: Ariadne, group: Group, message: MessageChain):
    if message.has(DetectPrefix):
        if message.has(DetectPrefix("ping ")):
            MessageChain(message.create(at=group.id, message=os.system(MessageChain)))

# 收到消息，回复ping结果
@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def on_message(app: Ariadne, group: Group, message: MessageChain):
    MessageChain(message.replace("ping"))