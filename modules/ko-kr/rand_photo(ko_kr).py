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
channel.name("랜덤 ACG 사진")
channel.description("그냥 임의의 ACG 플롯")
channel.author("ObsidianCatalina")


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("랜덤 ACG 사진")],
    )
)
async def setu(app: Ariadne, group: Group, event: GroupMessage):
    if langmanager.enable_lang == "ko_kr":
        if group.id in ban_group:
            await app.send_message(
                group,
                MessageChain(At(event.sender.id),
                             " 죄송합니다만 개발자의 요청에 따라 이 기능은 비활성화되었습니다."))
        elif event.sender.id in ban_user:
            await app.send_message(group, MessageChain(At(event.sender.id),
                                                       " 죄송합니다. 개발자의 요청에 따라 이 기능이 차단되었습니다."))
        else:
            async with ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.read()
            await app.send_group_message(group, MessageChain(Image(data_bytes=data)))

    else:
        await app.send_group_message(group, MessageChain(At(event.sender.id),
                                                         " 언어 (ko_kr)를 설치 한 경우 사용할 수 없습니다, 당신은 입력 할 수 있습니다 'Lang --set-default-lang = xx_xx'"))
