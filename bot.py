import os
import importlib
from telethon import TelegramClient, events
from config import api_id, api_hash, bot_token
from handlers.menu import menu_handler

# Initialize bot
client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

# Automatically load all plugins
for filename in os.listdir("plugins"):
    if filename.endswith(".py"):
        module_name = f"plugins.{filename[:-3]}"
        module = importlib.import_module(module_name)
        if hasattr(module, "register"):
            module.register(client)

@client.on(events.CallbackQuery)
async def callback_handler(event):
    await menu_handler(event)  # Handle menu button clicks

print("Bot is running...")
client.run_until_disconnected()