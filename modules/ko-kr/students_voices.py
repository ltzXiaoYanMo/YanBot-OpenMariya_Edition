import random
from graiax import silkcoder
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At, Voice
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import langmanager
import botmanager

v = botmanager.students_voices('voice_paths')
channel = Channel.current()
channel.name("블루 아카이브 학생 추측")
channel.description("학생을 추측하기 위해 목소리를 들어보세요.")
channel.author("ObsidianCatalina")


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("학생 추측")],
    )
)
async def linux(app: Ariadne, group: Group, event: GroupMessage):
    voice_bytes = await silkcoder.async_encode(random.choice(v), ios_adaptive=True)
    if langmanager.enable_lang == "ko_kr":
        await app.send_group_message(group, MessageChain(Voice(data_bytes=voice_bytes)))
    else:
        await app.send_group_message(group, MessageChain(At(event.sender.id), " 죄송합니다,이 기능은 해당 국가에서 지원되지 않습니다"))
