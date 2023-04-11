import random
from datetime import datetime
from pathlib import Path
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Forward, ForwardNode, Image
from graia.ariadne.message.parser.base import MatchContent
from graia.ariadne.model import Group, Member
from graia.saya import Channel
from graia.saya.builtins.broadcast import ListenerSchema

channel = Channel.current()


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("菜单")],
    )
)
async def create_forward(app: Ariadne, group: Group, member: Member):
    
    fwd_nodeList = [
        ForwardNode(
            target=2946761346,
            name="TypeRelease10.3",
            time=datetime.now(),
            message=MessageChain(("菜单："))),
        
    ]  
    fwd_nodeList.append(
            ForwardNode(
                target=2946761346,
                name="TypeRelease10.3",
                
                time=datetime.now(),
                message=MessageChain("1.版本查询：查看机器人当前版本"),)
        )
    fwd_nodeList.append(
            ForwardNode(
                target=2946761346,
                name="TypeRelease10.3",
                
                time=datetime.now(),
                message=MessageChain("2.来份涩图：随机一张二次元图"),)
        )
    fwd_nodeList.append(
            ForwardNode(
                target=2946761346,
                name="TypeRelease10.3",
                time=datetime.now(),
                message=MessageChain("3.猜学生：碧蓝档案相关，随机一条学生语音"),)
        )
    fwd_nodeList.append(
            ForwardNode(
                target=2946761346,
                name="TypeRelease10.3",
                time=datetime.now(),
                message=MessageChain("4.Lang --set-default-lang = xx_xx：切换语言"),)
        )
    
    message = MessageChain(Forward(fwd_nodeList))
    await app.send_message(group, message)