# 项目地址：https://github.com/ltzXiaoYanMo/YanBot_KHB_Edition

from graia.ariadne.app import Ariadne
from graia.ariadne.message.chain import MessageChain, Plain
from graia.saya import Channel, Saya
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()
channel.name("帮助！")
channel.description("这Bot怎么用啊！")
channel.author("ltzXiaoYanMo")

@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        inline_dispatchers=[CoolDown(0.1)],
        decorators={DetectPrefix("官方网站，请前往https://bot.ymbot.top")},
    )
)
async def setu(app: Ariadne, group: Group, message: MessageChain):
    await app.send_message(
        group,
        MessageChain(f"KHB网站：https://bot.khbit.cn"),
    )