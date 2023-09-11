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
    MessageChain(os.system)