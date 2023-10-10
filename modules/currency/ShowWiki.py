from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import DetectPrefix
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.ariadne.model import Group

channel = Channel.current()
channel.name("ShowWiki")
channel.description("傻鸟，不会用看这里")
channel.author("ltzXiaoYanMo")

@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[DetectPrefix("YBwiki")]
    )
)
async def wiki(app: Ariadne, group: Group):
    await app.send_message(
        group,
        "wiki:https://bot.ymbot.top"
    )