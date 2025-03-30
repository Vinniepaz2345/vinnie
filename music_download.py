import requests
from telethon import events

API_KEY = "d1b64c95"
API_URL = "https://api.jamendo.com/v3.0/tracks/?client_id={}&format=json&limit=1&search={}"

def get_music_download_link(song_name):
    url = API_URL.format(API_KEY, song_name)
    response = requests.get(url)
    data = response.json()

    if data["headers"]["status"] == "success" and data["results"]:
        track = data["results"][0]
        return track["download"], track["name"], track["artist_name"]
    
    return None, None, None

def register(client):
    @client.on(events.NewMessage(pattern='/music (.+)'))
    async def music_download(event):
        song_name = event.pattern_match.group(1)
        await event.respond(f"🔎 Searching for **{song_name}**...")

        download_link, track_name, artist = get_music_download_link(song_name)

        if download_link:
            await event.respond(f"🎵 **{track_name}** by {artist}\n🔽 [Download Here]({download_link})")
        else:
            await event.respond("❌ No music found!")