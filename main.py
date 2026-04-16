from telethon import TelegramClient
from config import api_id, api_hash

client = TelegramClient("session", api_id, api_hash)

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
