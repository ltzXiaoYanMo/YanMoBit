
from aiohttp import ClientSession
from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage, FriendMessage
from graia.ariadne.event.mirai import NewFriendRequestEvent, BotInvitedJoinGroupRequestEvent, MemberJoinRequestEvent, \
    MemberCardChangeEvent, GroupRecallEvent, MemberLeaveEventKick, MemberLeaveEventQuit, MemberJoinEvent
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At, Plain, Image
from graia.ariadne.model import Group
from graia.broadcast import Broadcast
from graia.saya import Channel, Saya
from graia.saya.builtins.broadcast import ListenerSchema
from modules import globalvars

saya = Saya.current()
channel = Channel.current()
bcc = create(Broadcast)

# 侦测加群请求
@channel.use(ListenerSchema(listening_events=[MemberJoinRequestEvent]))
async def join_request(event: MemberJoinRequestEvent):
    if (globalvars.blocklist != [] and globalvars.blocklist.__contains__(
            f"{event.source_group}_{event.supplicant}")) or (
            globalvars.g_blocklist != [] and globalvars.g_blocklist.__contains__(event.supplicant)):
        await event.reject()

# 侦测改名
@channel.use(ListenerSchema(listening_events=[MemberCardChangeEvent]))
async def card_change(app: Ariadne, event: MemberCardChangeEvent, group: Group):
    if not event.current == "":
        try:
            await app.send_message(
                group,
                MessageChain(
                    f"QQ号：{event.member.id}\n原昵称：{event.origin}\n新昵称：{event.current}"),
            )
        except:
            print("群消息发送失败")

# 侦测撤回
@channel.use(ListenerSchema(listening_events=[GroupRecallEvent]))
async def recall_detect(app: Ariadne, event: GroupRecallEvent, group: Group):
    messageChain = (At(event.operator.id), Plain(" 撤回啥了？让我看看！"))
    print(event.operator.permission)
    if not event.operator.permission == "ADMINISTRATOR" and not event.operator.permission == "OWNER":
        try:
            await app.send_message(
                group,
                MessageChain(messageChain),
            )
        except:
            print("群消息发送失败")

# 侦测踢人
@channel.use(ListenerSchema(listening_events=[MemberLeaveEventKick]))
async def kick_detect(app: Ariadne, event: MemberLeaveEventKick, group: Group):
    try:
        await app.send_message(
            group,
            MessageChain(
                f"{event.member.name} ({event.member.id}) 被踢出去辣，好似捏~"),
        )
    except:
        print("群消息发送失败")


# 侦测退群
@channel.use(ListenerSchema(listening_events=[MemberLeaveEventQuit]))
async def quit_detect(app: Ariadne, event: MemberLeaveEventQuit, group: Group):
    try:
        await app.send_message(
            group,
            MessageChain(
                f"{event.member.name} ({event.member.id}) 退群力，我们为他感到惋惜（？）"),
        )
    except:
        print("群消息发送失败")


# 侦测入群
@channel.use(ListenerSchema(listening_events=[MemberJoinEvent]))
async def join_detect(app: Ariadne, event: MemberJoinEvent, group: Group):
    messageChain = (At(event.member.id), Plain(" 来辣！"))
    try:
        await app.send_message(
            group,
            MessageChain(messageChain),
        )
    except:
        print("群消息发送失败")