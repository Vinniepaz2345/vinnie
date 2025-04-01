from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern='/start'))
    async def start(event):
        await event.respond("Welcome! Type /menu to see available commands.")
