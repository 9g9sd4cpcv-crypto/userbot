from main import client
from telethon import events
from config import OWNER_ID

@client.on(events.NewMessage(pattern="/ban"))
async def ban(event):
    reply = await event.get_reply_message()
    await event.client.edit_permissions(event.chat_id, reply.sender_id, view_messages=False)

@client.on(events.NewMessage(pattern="/banall"))
async def banall(event):
    if event.sender_id != OWNER_ID:
        return await event.reply("❌ Only Owner")

    users = await event.client.get_participants(event.chat_id)
    for user in users:
        await event.client.edit_permissions(event.chat_id, user.id, view_messages=False)
