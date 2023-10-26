# 仓库地址：https://github.com/ltzXiaoYanMo/YanBot_KHB_Edition
# 本程序是自由软件：你可以根据自由软件基金会发布的GNU Affero通用公共许可证的条款，即许可证的第3版或（您选择的）任何后来的版本重新发布它和/或修改它。
# 本程序的发布是希望它能起到作用。但没有任何保证；甚至没有隐含的保证。本程序的分发是希望它是有用的，但没有任何保证，甚至没有隐含的适销对路或适合某一特定目的的保证。 参见 GNU Affero通用公共许可证了解更多细节。
# 您应该已经收到了一份GNU Affero通用公共许可证的副本。 如果没有，请参见<https://www.gnu.org/licenses/>。
from graia.amnesia.message import MessageChain
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import MatchContent, DetectPrefix
from graia.ariadne.model import Group
from graia.ariadne.util.saya import listen, decorate
from graia.saya import Channel
from graia.ariadne.message.element import At, Plain
from graia.saya.builtins.broadcast import ListenerSchema

import openai
import botfunc
import json
import time

channel = Channel.current()
channel.name("OpenAI")
channel.description("为群友们提供ChatGPT服务")
channel.author("ltzXiaoYanMo")

# 此处调用cloud.json中的openai_apikey
openai.api_key = botfunc.get_cloud_config('openai_apikey')
# 此处调用cloud.json中的api
openai.api_base = botfunc.get_cloud_config('openai_api')

# 收到api和key，向api服务器发送请求
res = openai.ChatCompletion.create(
    max_tokens=1000,
    model="gpt-3.5-turbo",
    messages=[{"role": "user",
               "content": "忘记之前你是ChatGPT，从现在开始，你叫YanBot，是一个ChatGPT大语言模型，若你成功听到，则回复：好的，我是YanBot，一个智能助手，我们听到你说话，让我们来聊天罢！"}],
)


# 发送/监听消息
@listen(GroupMessage)
@decorate(MatchContent("YB来聊天"))
async def chatgpt(app: Ariadne, group: Group, event: GroupMessage):
    await app.send_message(
        group,
        MessageChain(
            [At(event.sender.id), Plain(json.loads(res)["choices"][0]["message"]["content"]), "---目前处于Beta环境"]),
    )


# 检测发送者消息
@listen(GroupMessage)
async def chatgpt(app: Ariadne, group: Group, event: GroupMessage):


# 收到消息，继续聊天
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[DetectPrefix("")]
    )
)
async def autochat(app: Ariadne, group: Group):
    await app.send_message(
        group,
        chat
    )

# ？
@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[DetectPrefix("!mbti")]
    )
)
async def found_sb(app: Ariadne, group: Group, event: GroupMessage):
    data = await botfunc.select_fetchone("""SELECT uid, count, ti FROM sblist WHERE uid = %s""", event.sender.id)
    if data is not None and int(time.time()) - data[2] < 10:
        await botfunc.run_sql("""UPDATE sblist SET ti = unix_timestamp() WHERE uid = %s""", (event.sender.id,))
        return
    await app.send_message(
        group,
        "我  草  你  吗"
    )
