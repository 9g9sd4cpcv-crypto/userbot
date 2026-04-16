from main import client
from telethon import events, Button

@client.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.respond(
        "🔥 Control Panel 🔥",
        buttons=[
            [Button.text("👮 Admin"), Button.text("🎮 Games")],
            [Button.text("⚙️ Tools")]
        ]
    )
