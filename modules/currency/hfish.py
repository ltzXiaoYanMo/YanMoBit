from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import requests
import json
import botfunc

channel = Channel.current()
channel.name("HFish")
channel.description("HFish攻击报告")
channel.author("ltzXiaoYanMo")

url = botfunc.get_cloud_config('hfish_apikey')

payload = json.dumps({
  "start_time": 0,
  "end_time": 0,
  "intranet": 0,
  "threat_label": [
    "Scanner"
  ]
})
headers = {
  'Content-Type': 'application/json'
}


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("!hfish")]
    )
)
async def status(app: Ariadne, group: Group):
    await app.send_message(
        group,
        requests.request("POST", url, headers=headers, data=payload)
    )
