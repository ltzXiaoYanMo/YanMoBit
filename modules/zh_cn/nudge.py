# 2kbit Python Edition，2kbit的Python分支版本
# Copyright(C) 2022 Abjust 版权所有。

# 本程序是自由软件：你可以根据自由软件基金会发布的GNU Affero通用公共许可证的条款，即许可证的第3版或（您选择的）任何后来的版本重新发布它和/或修改它。。

# 本程序的发布是希望它能起到作用。但没有任何保证；甚至没有隐含的保证。本程序的分发是希望它是有用的，但没有任何保证，甚至没有隐含的适销对路或适合某一特定目的的保证。 参见 GNU Affero通用公共许可证了解更多细节。

# 您应该已经收到了一份GNU Affero通用公共许可证的副本。 如果没有，请参见<https://www.gnu.org/licenses/>。

# 致所有构建及修改2kbit代码片段的用户：作者（Abjust）并不承担构建2kbit代码片段（包括修改过的版本）所产生的一切风险，但是用户有权在2kbit的GitHub项目页提出issue，并有权在代码片段修复这些问题后获取这些更新，但是，作者不会对修改过的代码版本做质量保证，也没有义务修正在修改过的代码片段中存在的任何缺陷。

# 由ltzXiaoYanMo提供修复，但不确定是否其他bug

# Mirai输出:2023-07-30 20:44:55 V/Bot.1373892821: Event: NudgeEvent(from=NormalMember(2315049216), target=Bot(1373892821), subject=Group(904464532), action=戳了戳, suffix=)

from graia.ariadne.app import Ariadne
from graia.ariadne.event.mirai import NudgeEvent
from graia.ariadne.message.chain import MessageChain, Plain
from graia.ariadne.message.element import At
from graia.saya import Channel, Saya
from graia.saya.builtins.broadcast.schema import ListenerSchema
import globalvars

channel = Channel.current()
channel.name("戳一戳，你就知道！")
channel.description("你戳你m呢，你看你m呢，啊？")
channel.author("ltzXiaoYanMo")

saya = Saya.current()
channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[NudgeEvent]))
async def nudge(app: Ariadne, event: NudgeEvent):
    # 只检测被戳的是不是本机器人
    print(event.target)
    if event.target == globalvars.bot_qq and event.context_type == "group":
            await app.send_group_message(
                event.group_id,
                MessageChain(MessageChain(
                    [At(event.supplicant), Plain(" 这个沙冰吃柠檬，柠檬大冰人人吃，左吃吃tm右吃吃，吃得柠檬冰开化")]))
            )
