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
        decorators=[DetectPrefix("官方KHB网站：https://bot.khbit.cn")],
    )
)
async def setu(app: Ariadne, group: Group, message: MessageChain):
    await app.send_message(
        group,
        MessageChain(f"若你想查看修改版的，请前往https://bot.ymbot.top"),
    )