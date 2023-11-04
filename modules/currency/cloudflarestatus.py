from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import requests
import json
channel = Channel.current()
channel.name("CloudFlare状态检测")
channel.description("CloudFlare Status Checker")
channel.author("ltzXiaoYanMo")

CloudStatus = 'https://www.cloudflarestatus.com/api/v2/status.json'

@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("!cfstatus")]
    )
)
async def status(app: Ariadne, group: Group):
    await app.send_message(
        group,
        requests.get(json.loads(requests.get(CloudStatus).text)['components'][0]['name']).text
    )
