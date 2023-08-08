# 开源地址：https://github.com/ltzXiaoYanMo/YanBot_KHB_Edition
# 目前此功能还在开发中，敬请期待！
# Mirai输出:2023-08-08 16:10:53.617 | INFO     | graia.ariadne.model:log:82 - 1373892821: [RECV][Universe（确信）(310896029)] fuckworld(2315049216) -> 测试消息
from graia.ariadne.event.message import GroupMessage
from graia.saya import Channel, Saya
from graia.ariadne.model import Group
from graia.ariadne.util.saya import listen, decorate
from graia.ariadne.message.element import At, Plain
from graia.saya.builtins.broadcast.schema import ListenerSchema

import time
import os
import botfunc

channel = Channel.current()
channel.name("打卡")
channel.description("诶诶诶，来打卡辣")
channel.author("ltzXiaoYanMo")

saya = Saya.current()
channel = Channel.current()

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def echo(app: Ariadne, group: Group, source: Source, message: MessageChain = DetectPrefix("YB打卡")):
    print(event.target)
    if event.target == globalvars.bot_qq and event.context_type == "group":
            await app.send_group_message(
                event.group_id,
                MessageChain(MessageChain(
                    [At(event.supplicant), Plain(" 打卡成功辣!")]))
            )