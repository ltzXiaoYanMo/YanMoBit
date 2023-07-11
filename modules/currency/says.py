from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage, ActiveGroupMessage
from graia.ariadne.event.mirai import GroupRecallEvent
from graia.ariadne.message import Source
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import botfunc

channel = Channel.current()
channel.name("says")
channel.description("照搬KHB的says（")
channel.author("ltzXiaoYanMo")


@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def echo(app: Ariadne, group: Group, source: Source, message: MessageChain = DetectPrefix("/says ")):
    if not str(message).startswith('/says'):
        m: ActiveGroupMessage = await app.send_group_message(
            group,
            message,
        )
        botfunc.r.hset('says', source.id, m.source.id)


@channel.use(ListenerSchema(listening_events=[GroupRecallEvent]))
async def echo(app: Ariadne, group: Group, event: GroupRecallEvent):
    if botfunc.r.hexists("says", event.message_id):
        await app.recall_message(botfunc.r.hget("says", event.message_id), group)
