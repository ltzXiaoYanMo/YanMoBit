# 项目地址：https://github.com/ltzXiaoYanMo/YanBot_KHB_Edition
from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import MentionMe
from graia.ariadne.util.saya import listen
from graia.saya import Channel
from graia.ariadne.message.element import Plain, At

channel = Channel.current()
channel.name("帮助！")
channel.description("这Bot怎么用啊！")
channel.author("ltzXiaoYanMo")

@listen(MentionMe)
async def help(app: Ariadne, event: GroupMessage):
    await app.send_group_message(
        MessageChain(MessageChain(
            [At(event.supplicant), Plain(" 前往https://bot.ymbot.top查看教程")]))
    )