import asyncio
import importlib
import os
from pyrogram import idle
from Maxroid.Plugins import ALL_MODULES
from Maxroid.core.logger import LOGGER
from Maxroid.core.clients import xemishra

async def install():
    LOGGER.info("[•] Loading Modules...")
    for module in ALL_MODULES:
        importlib.import_module("Maxroid.Plugins." + module)
    LOGGER.info(f"[•] Loaded {len(ALL_MODULES)} Modules.")

    LOGGER.info("[•] Refreshing Directories...")
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")
    LOGGER.info("[•] Directories Refreshed.")
    await xemishra.start()
    await idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(install())
    LOGGER.error("stop")
