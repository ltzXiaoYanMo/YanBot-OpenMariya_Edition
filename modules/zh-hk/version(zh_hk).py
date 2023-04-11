import random
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.element import Plain
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import botmanager
import langmanager

r = botmanager.sents_config('rand_sents_hk', lang='zh-hk')
channel = Channel.current()
channel.name("版本查詢")
channel.description("查看機器人當前版本")
channel.author("ObsidianCatalina")
txt = "當前裝載版本為Mariya Stable 1.2.7\n"


@channel.use(

    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("版本查詢")]
    )
)
async def bot_version(app: Ariadne, group: Group, event: GroupMessage):
    if langmanager.enable_lang == "zh_hk":
        await app.send_message(group, MessageChain([txt, "------------\n", Plain(random.choice([r][0]))]))
    else:
        await app.send_group_message(group, MessageChain(At(event.sender.id),
                                                         " 此語言（zh_hk）不可用，如果確認安裝了這個語言，請輸入'Lang --set-default-lang = xx_xx'"))
