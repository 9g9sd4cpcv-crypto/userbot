from main import client
from telethon import events

@client.on(events.NewMessage)
async def anti_link(event):
    if "http" in event.raw_text:
        await event.delete()
        await event.reply("🚫 Links not allowed")
