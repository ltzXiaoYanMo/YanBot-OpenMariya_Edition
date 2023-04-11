import os

from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.connection.config import config
from graia.broadcast import Broadcast
from graia.saya import Saya
from loguru import logger

import botmanager

saya = create(Saya)
bcc = create(Broadcast)
app = Ariadne(
    connection=config(
        botmanager.bot_config('bot_qq'),  
        botmanager.bot_config('verifyKey'),  
    ),
)
with saya.module_context():
    for root, dirs, files in os.walk("./modules", topdown=False):
        for name in files:
            module = os.path.join(root, name).replace('\\', '.').replace('./', '').replace('/', '.').split('.')
            if '__pycache__' in module:
                continue
            if module[1] == 'NO_USE':
                continue
            module = '.'.join(module)[:-3]
            logger.info(f'{module} 将被载入')
            saya.require(module)

for module, channel in saya.channels.items():
    logger.info(f"module: {module}")
    logger.info(f"name: {channel.meta['name']}")
    logger.info(f"author: {' '.join(channel.meta['author'])}")
    logger.info(f"description: {channel.meta['description']}")

logger.success('启动成功辣！')
app.launch_blocking()
