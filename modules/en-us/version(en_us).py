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

r = botmanager.sents_config('rand_sents_en', lang='en-us')
channel = Channel.current()
channel.name("ver_check")
channel.description("check bot version")
channel.author("ObsidianCatalina")
txt = "Now the bot version is Mariya Stable 1.2.7\n"


@channel.use(

    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("ver_check")]
    )
)
async def bot_version(app: Ariadne, group: Group, event: GroupMessage):
    if langmanager.enable_lang == "en_us":
        await app.send_message(group, MessageChain([txt, "------------\n", Plain(random.choice([r][0]))]))
    else:
        await app.send_group_message(group, MessageChain(At(event.sender.id),
                                                         " The language(es_es) is not available.If you installed it,you can type 'Lang --set-default-lang = xx_xx'"))
