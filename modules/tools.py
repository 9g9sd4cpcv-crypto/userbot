from main import client
from telethon import events

@client.on(events.NewMessage(pattern="/alive"))
async def alive(event):
    await event.reply("✅ Bot is alive!")

@client.on(events.NewMessage(pattern="/id"))
async def id(event):
    await event.reply(f"🆔 {event.sender_id}")
