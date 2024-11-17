import os
import time
import asyncio
from Maxroid.core.logger import LOGGER
from Maxroid.core.clients import(
    Maxroid,
    UserBot,
)

StartTime = time.time()

async def install():
    os.system("clear")
    LOGGER.info(
        "[•] starting... "
    )
    await Maxroid.start()
    LOGGER.info(
        "[•] starting......."
    )
    await UserBot.start()
    LOGGER.info(
        "[•] starting............"
    )
    try:
        await UserBot.join_chat("Maxroid")
        await UserBot.join_chat("MaxroidChat")
    except:
        pass
    LOGGER.info(
        "[•] Started !!"
    )

asyncio.get_event_loop().run_until_complete(install())
