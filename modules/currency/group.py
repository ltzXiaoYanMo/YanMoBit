from graia.ariadne.app import Ariadne
from graia.ariadne.event.mirai import MemberJoinRequestEvent, \
    MemberCardChangeEvent, GroupRecallEvent, MemberLeaveEventKick, MemberLeaveEventQuit, MemberJoinEvent
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At, Plain
from graia.ariadne.model import Group, MemberPerm
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

import globalvars

channel = Channel.current()
channel.name("检测群聊")
channel.description("你的群聊很珍贵，需要很好地保护（？）")
channel.author("ltzXiaoYanMo")


# 侦测加群请求
@channel.use(ListenerSchema(listening_events=[MemberJoinRequestEvent]))
async def join_request(event: MemberJoinRequestEvent):
    if ((not globalvars.blocklist and f"{event.source_group}_{event.supplicant}" in globalvars.blocklist) or
            (not globalvars.g_blocklist and event.supplicant in globalvars.g_blocklist)):
        await event.reject()


# 侦测改名
@channel.use(ListenerSchema(listening_events=[MemberCardChangeEvent]))
async def card_change(app: Ariadne, event: MemberCardChangeEvent, group: Group):
    if event.current != "":
        await app.send_message(
            group,
            MessageChain(
                f"QQ号：{event.member.id}\n原昵称：{event.origin}\n新昵称：{event.current}"),
        )


# 侦测撤回
@channel.use(ListenerSchema(listening_events=[GroupRecallEvent]))
async def recall_detect(app: Ariadne, event: GroupRecallEvent, group: Group):
    if event.operator.permission not in [MemberPerm.Administrator, MemberPerm.Owner]:
        await app.send_message(
            group,
            MessageChain(At(event.operator.id), Plain(" 撤回啥了？让我看看！")),
        )


# 侦测踢人
@channel.use(ListenerSchema(listening_events=[MemberLeaveEventKick]))
async def kick_detect(app: Ariadne, event: MemberLeaveEventKick, group: Group):
    await app.send_message(
        group,
        MessageChain(
            f"{event.member.name} ({event.member.id}) 被踢出去辣，好似捏~"),
    )


# 侦测退群
@channel.use(ListenerSchema(listening_events=[MemberLeaveEventQuit]))
async def quit_detect(app: Ariadne, event: MemberLeaveEventQuit, group: Group):
    await app.send_message(
        group,
        MessageChain(
            f"{event.member.name} ({event.member.id}) 退群力，我们为他感到惋惜（？）"),
    )


# 侦测入群
@channel.use(ListenerSchema(listening_events=[MemberJoinEvent]))
async def join_detect(app: Ariadne, event: MemberJoinEvent, group: Group):
    await app.send_message(
        group,
        MessageChain(At(event.member.id), Plain(" 来辣！")),
    )
