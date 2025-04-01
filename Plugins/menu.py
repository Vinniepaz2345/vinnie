import os
import asyncio
from telethon import events, Button

def register(client):
    @client.on(events.NewMessage(pattern='/menu'))
    async def menu_command(event):
        # Ensure plugins folder exists
        if not os.path.exists("plugins"):
            await event.respond("No commands available.")
            return

        # Scan plugins for commands
        commands = [f"/{file[:-3]}" for file in os.listdir("plugins") if file.endswith(".py")]
        
        if not commands:
            await event.respond("No commands available.")
            return

        # Arrange buttons in a grid (2 per row)
        buttons = [commands[i:i+2] for i in range(0, len(commands), 2)]
        buttons = [[Button.inline(cmd, cmd.encode()) for cmd in row] for row in buttons]

        # Send the video
        video_msg = await event.respond("📜 **Available Commands:**", file="/data/data/com.termux/files/home/telegram_bot/gathuo.mp4")
        
        # Send menu with inline buttons
        menu_msg = await event.respond("📜 **Available Commands:**", buttons=buttons)

        # Countdown before deletion
        countdown_msg = await event.respond("⏳ Menu will delete in 30 seconds...")

        for i in range(30, 0, -5):
            await asyncio.sleep(5)
            await countdown_msg.edit(f"⏳ Menu will delete in {i} seconds...")

        # Delete all messages after countdown
        await menu_msg.delete()
        await countdown_msg.delete()
        await video_msg.delete()

    @client.on(events.CallbackQuery())
    async def menu_handler(event):
        data = event.data.decode("utf-8")
        await event.edit(f"You selected: {data}")
