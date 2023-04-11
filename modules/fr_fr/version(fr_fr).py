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

r = botmanager.sents_config('rand_sents_fr', lang='fr-fr')
channel = Channel.current()
channel.name("ver_vérifier")
channel.description("vérifier bot version")
channel.author("ObsidianCatalina")
txt = "maintenant le bot version est Mariya Bêta 1.0.0\n"


@channel.use(

    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("ver_vérifier")]
    )
)
async def bot_version(app: Ariadne, group: Group, event: GroupMessage):
    if langmanager.enable_lang == "fr_fr":
        await app.send_message(group, MessageChain([txt, "------------\n", Plain(random.choice([r][0]))]))
    else:
        await app.send_group_message(group, MessageChain(At(event.sender.id),
                                                         " La Langue(fr_fr) est non disponible si vous Installé il,tu pouvoir type 'Lang --set-default-lang = xx_xx'"))
