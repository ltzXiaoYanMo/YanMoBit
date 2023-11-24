from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.element import Plain, At, Image
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

import random

channel = Channel.current()
channel.name("fuckflsq")
channel.description("源钻你有妈吗？")
channel.author("ltzXiaoYanMo")

hahaha = './img/'
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[DetectPrefix("每日乐子")]
    )
)
async def fuckflsq(app: Ariadne, group: Group):
    await app.send_group_message(
        group.subject,
        MessageChain([At(group.supplicant), Plain(f" {random.choice(hahaha)}")])
    )
