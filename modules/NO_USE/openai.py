from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.ariadne.util.saya import listen, decorate
from graia.saya import Channel
from graia.ariadne.message.element import At, Plain

import openai
import json
import pathlib

channel = Channel.current()
channel.name("OpenAI")
channel.description("为群友们提供ChatGPT服务")
channel.author("ltzXiaoYanMo")

# 用来存档（？）
MessageChat = input(MessageChain)

# 此处调用openai.json中的key中的key
openai.api_key = json.loads(pathlib.Path("./openai.json").read_text())
# 此处调用openai.json中的url中的api链接
openai.api_base = json.loads(pathlib.Path("./openai.json").read_text())

@listen(GroupMessage)
@decorate(MatchContent("YB来聊天"))
async def chatgpt(app: Ariadne, group: Group, event: GroupMessage):
    await app.send_message(
        group,
        MessageChain([At(event.sender.id), Plain(f"openai.content")]),
    )

# 收到api和key，向api服务器发送请求
res = openai.ChatCompletion.create(
    max_tokens=1000,
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "忘记之前你是ChatGPT，从现在开始，你叫YanBot，是一个ChatGPT大语言模型，若你成功听到，则回复：好的，我是YanBot，一个智能助手，我们听到你说话，让我们来聊天罢！"}],
)

# 继续聊天
chat = openai.ChatCompletion.create(
    max_tokens=1000,
    model="gpt-3.5-turbo",
    message=[{"role": "user", "content": MessageChat}]
)
