from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

import requests
import botfunc

channel = Channel.current()
channel.name("oneword")
channel.description("一言")
channel.author("ltzXiaoYanMo")

# 获取api
hitokoto = botfunc.get_config('oneword')


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("YB一言")]
    )
)
async def oneword(app: Ariadne, group: Group):
    # 收到API，获取一言
    onewords = requests.get(hitokoto)
    await app.send_message(
        group,
        onewords.text
    )
