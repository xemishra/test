from pyrogram import Client, filters
from pyrogram.types import Message
from Maxroid.core.clients import(
    Maxroid,
    xemishra,
)

@Maxroid.on_message(filters.command("vc"))
async def join_voice_chat(client: Client, message: Message):
    try:
        await xemishra.join_group_call(
            chat_id=message.chat.id,
            stream_type="audio",
        )
        await message.reply("Joined the voice chat!")
    except:
        await message.reply("Please use this command in a group with a voice chat.")
