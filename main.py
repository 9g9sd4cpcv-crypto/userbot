from telethon import TelegramClient
from config import api_id, api_hash

from telethon.sessions import StringSession
import os

client = TelegramClient(
    StringSession(os.getenv("STRING_SESSION")),
    api_id,
    api_hash
)

# import modules
import modules.welcome
import modules.admin
import modules.xp
import modules.ui
import modules.tools
import modules.games
import modules.moderation

client.start()
print("🔥 Userbot Running...")
client.run_until_disconnected()
