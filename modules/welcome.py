from main import client
from telethon import events

@client.on(events.ChatAction)
async def welcome(event):
    if event.user_joined or event.user_added:
        user = await event.get_user()
        await event.reply(f"""
✨ Welcome {user.first_name} ✨

📌 Follow rules
🔥 Stay active
🏆 Earn XP
""")
