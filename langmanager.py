from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import At
from graia.ariadne.message.parser.base import DetectPrefix, MatchContent
from graia.ariadne.model import Group
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import botmanager

su = botmanager.bot_config('su')
lang = {
    "zh_cn": (" Bot默认语言已更改为简体中文(中国大陆)", " 默认语言已是简体中文(中国大陆)，无需更改"),
    "zh_hk": (" Bot語言已更改為繁體中文（中華人民共和國香港特別行政區）", " 默認語言已是繁體中文（中華人民共和國香港特別行政區），無需更改"),
    "en_us": (" Now bot default language is English(United States)", " Bot default language is English(United States) now,Don't need Change"),
    "fr_fr": (" Maintenant bot par défaut langue est Français(République française)", " Bot par défaut langue est  Français(République française),Pas besoin changer"),
    "ru_ru": (" теперь Язык бота по умолчанию российской(Российская Федерация)", " Язык бота по умолчанию российской(Российская Федерация) сейчас. Не нужно изменить"),
    "es_es": (" Ahora el idioma predeterminado del bot es Español(Reino de España)", " El idioma predeterminado del bot es Español(Reino de España),no necesita cambiar"),
    "ja_jp": (" ボットのデフォルト言語が日本語(日本)になりました", " ボットのデフォルト言語は日本語(日本)になりました,変更する必要はありません"),
    "ko_kr": (" 이제 봇 기본 언어는 한국어(대한민국)입니다.", " 봇 기본 언어는 이제 한국어(대한민국)이며 변경이 필요하지 않습니다.")
}
enable_lang = "zh_cn"

channel = Channel.current()


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage]
    )
)
async def change_lang(app: Ariadne, group: Group, event: GroupMessage, message: MessageChain = DetectPrefix("Lang --set-default-lang = ")):
    global enable_lang
    if str(message) in lang:
        if enable_lang != str(message):
            enable_lang = str(message)
            await app.send_message(
                group,
                MessageChain(At(event.sender.id), lang[enable_lang][0])
            )
        else:
            await app.send_message(group, MessageChain(At(event.sender.id),
                                                       lang[enable_lang][1]))
    else:
        await app.send_message(group, MessageChain(At(event.sender.id)," Cannot find the language"))


@channel.use(
    ListenerSchema(
        listening_events=[GroupMessage],
        decorators=[MatchContent("Lang --list-a")],
    )
)
async def Lang_list(app: Ariadne, group: Group, event: GroupMessage):
    if event.sender.id in su:
        await app.send_message(
            group,
            MessageChain(At(event.sender.id),
                         " Installed language:\n"
                         "Chinese Simplified(China Mainland/PRC)\n"
                         "English(United States)\n"
                         "French(French Republic)\n"
                         "Russian(Russian Federation)\n"
                         "Spanish(Spain)\n"
                         "Japanese(Japan)\n"
                         "Korean(Republic of Korea/South Korerea)\n"
                         "Chinese Chinese Traditional(PRC SAR HongKong)")
        )
    else:
        await app.send_message(group, MessageChain(At(event.sender.id), " You don't have check privileges"))
