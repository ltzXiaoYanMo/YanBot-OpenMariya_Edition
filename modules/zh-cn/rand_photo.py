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

url = botmanager.bot_config('setuapi')
ban_group = botmanager.bot_config('ban_group')
ban_user = botmanager.bot_config('ban_user')
channel = Channel.current()
channel.name("随机涩图")
channel.description("就是随机涩图啊（恼）")
channel.author("ObsidianCatalina")


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("来份涩图")],
    )
)
async def setu(app: Ariadne, group: Group, event: GroupMessage):
    if langmanager.enable_lang == "zh_cn":
        if group.id in ban_group:
            await app.send_message(
                group,
                MessageChain(At(event.sender.id), " 抱歉，应开发者要求，此功能被禁止"))
        elif event.sender.id in ban_user:
            await app.send_message(group,
                                   MessageChain(At(event.sender.id), " 对不起，应开发者要求，您已被禁止使用此功能"))
        else:
            async with ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.read()
            await app.send_group_message(group, MessageChain(Image(data_bytes=data)))
    else:
        await app.send_group_message(group, MessageChain(At(event.sender.id),
                                                         " 此语言(zh_cn)不可用，如果确认安装了这个语言，请输入'Lang --set-default-lang = xx_xx'"))
