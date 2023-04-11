from aiohttp import ClientSession
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Image, At
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import botmanager
import langmanager

url = botmanager.bot_config('setuapi1')
ban_group = botmanager.bot_config('ban_group')
ban_user = botmanager.bot_config('ban_user')
channel = Channel.current()
channel.name("Photo acg aléatoire")
channel.description("Juste photo acg aléatoire")
channel.author("ObsidianCatalina")


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("acg_aléatoire")],
    )
)
async def setu(app: Ariadne, group: Group, event: GroupMessage):
    if langmanager.enable_lang == "fr_fr":
        if group.id in ban_group:
            await app.send_message(
                group,
                MessageChain(At(event.sender.id),
                             " Désolé, ce groupe a désactivé la fonctionnalité. Parce que chez les développeurs exigent"))
        elif event.sender.id in ban_user:
            await app.send_message(group, MessageChain(At(event.sender.id),
                                                       " Désolé, vous avez été interdit d'utiliser cette fonctionnalité. Parce que chez les développeurs exigent"))
        else:
            async with ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.read()
            await app.send_group_message(group, MessageChain(Image(data_bytes=data)))

    else:
        await app.send_group_message(group, MessageChain(At(event.sender.id),
                                                         " La Langue(fr_fr) est non disponible si vous Installé il,tu pouvoir type 'Lang --set-default-lang = xx_xx'"))
