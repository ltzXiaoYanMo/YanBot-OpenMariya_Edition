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

r = botmanager.sents_config('rand_sents_kr', lang='ko-kr')
channel = Channel.current()
channel.name("버전 쿼리")
channel.description("봇의 현재 버전 보기")
channel.author("ObsidianCatalina")
txt = "현재 마운트 버전은Mariya Stable 1.2.7\n"


@channel.use(

    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("버전 쿼리")]
    )
)
async def bot_version(app: Ariadne, group: Group, event: GroupMessage):
    if langmanager.enable_lang == "ko_kr":
        await app.send_message(group, MessageChain([txt, "------------\n", Plain(random.choice([r][0]))]))
    else:
        await app.send_group_message(group, MessageChain(At(event.sender.id),
                                                         " 이 언어(ko_kr)는 사용할 수 없습니다. 설치되어 있는지 확인한 경우 입력합니다.'Lang --set-default-lang = xx_xx'"))
