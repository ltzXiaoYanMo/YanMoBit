from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import DetectPrefix
from graia.ariadne.model import Group
from graia.ariadne.util.saya import listen
from graia.saya import Channel

import botfunc

channel = Channel.current()
channel.name("管理员")
channel.description("加管理，没啥好说的")
channel.author("ltzXiaoYanMo")


@listen(GroupMessage)
async def add_admin(app: Ariadne, group: Group, event: GroupMessage, message: MessageChain = DetectPrefix("添加管理")):
    admins = await botfunc.get_all_admin()
    if event.sender.id not in admins:
        return
    try:
        await botfunc.run_sql("INSERT INTO admin(uid) VALUES (%s)", (int(str(message)),))
    except Exception as err:
        await app.send_message(group, f"寄！{err}")
    else:
        await app.send_message(group, "Oh♂Yeah!")


@listen(GroupMessage)
async def del_admin(app: Ariadne, group: Group, event: GroupMessage, message: MessageChain = DetectPrefix("删除管理")):
    admins = await botfunc.get_all_admin()
    if event.sender.id not in admins:
        return
    try:
        await botfunc.run_sql("DELETE FROM admin WHERE uid = %s", (int(str(message)),))
    except Exception as err:
        await app.send_message(group, f"寄！{err}")
    else:
        await app.send_message(group, "Fu♂ck you!")
