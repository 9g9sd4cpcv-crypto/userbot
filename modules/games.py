from main import client
from telethon import events
import random

@client.on(events.NewMessage(pattern="/roll"))
async def roll(event):
    await event.reply(f"🎲 {random.randint(1,6)}")
