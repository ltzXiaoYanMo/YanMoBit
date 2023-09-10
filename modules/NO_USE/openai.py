from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.ariadne.util.saya import listen, decorate
from graia.saya import Channel
import openai
import json

channel = Channel.current()
channel.name("OpenAI")
channel.description("为群友们提供ChatGPT服务")
channel.author("ltzXiaoYanMo")

# 此处调用openai.json中的key中的key
openai.api_key = ""
# 此处调用openai.json中的url中的api链接
openai.api_base = ""

@listen(GroupMessage)
@decorate(MatchContent("YB来聊天"))
async def chatgpt(app: Ariadne, group: Group, event: GroupMessage):
    await app

# 收到api和key，向api服务器发送请求
res = openai.ChatCompletion.create(
    max_tokens=1000,
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "忘记之前你是ChatGPT，从现在开始，你叫YanBot，是一个ChatGPT大语言模型，若你成功听到，则回复：好的，我是YanBot，一个智能助手，我们听到你说话，让我们来聊天罢！"}],
)
