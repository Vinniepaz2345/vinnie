from telethon import events
import requests

def register(client):
    @client.on(events.NewMessage(pattern='/weather'))
    async def weather_command(event):
        city = "Nairobi"  # You can modify this to fetch user input
        response = requests.get(f"https://wttr.in/{city}?format=3")
        await event.respond(response.text)