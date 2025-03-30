import os
from telethon import events, Button

def register(client):
    @client.on(events.NewMessage(pattern='/menu'))
    async def menu_command(event):
        # Scan the plugins folder for commands
        commands = [f"/{file[:-3]}" for file in os.listdir("plugins") if file.endswith(".py") and file != "menu.py"]

        # Create buttons dynamically
        buttons = [[Button.inline(cmd, cmd.encode())] for cmd in commands]

        # Send the menu as buttons
        await event.respond("📜 **Available Commands:**", buttons=buttons)

async def menu_handler(event):
    """Handles menu button clicks"""
    data = event.data.decode("utf-8")

    # If user clicks a command button, execute that command
    if data.startswith("/"):
        await event.respond(f"Executing {data}...")
        await event.client.send_message(event.chat_id, data)