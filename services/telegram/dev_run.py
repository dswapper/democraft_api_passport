import asyncio
from bot.__main__ import bot_pooling

import logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

alchemy_logger = logging.getLogger('sqlalchemy.engine')
alchemy_logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    asyncio.run(bot_pooling())