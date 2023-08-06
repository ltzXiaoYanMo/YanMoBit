# 开源地址：https://github.com/ltzXiaoYanMo/YanBot_KHB_Edition
# 目前此功能还在开发中，敬请期待！
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import FriendMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

channel = Channel.current()
channel.name("打卡")
channel.description("诶诶诶，来打卡辣")
channel.author("ltzXiaoYanMo")
