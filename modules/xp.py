from main import client
from telethon import events

xp_db = {}

@client.on(events.NewMessage)
async def xp_system(event):
    user = event.sender_id
    xp_db[user] = xp_db.get(user, 0) + 1

@client.on(events.NewMessage(pattern="/rank"))
async def rank(event):
    xp = xp_db.get(event.sender_id, 0)
    level = xp // 10
    await event.reply(f"🏆 XP: {xp}\n🎯 Level: {level}")
