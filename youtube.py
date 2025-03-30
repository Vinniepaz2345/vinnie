import requests
from telethon import events

API_KEY = "AIzaSyCHUplM_3G0nhcM5cAGb50RmSh26t9T1FE"  # Replace with your YouTube API key
SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

def register(client):
    @client.on(events.NewMessage(pattern='/youtube (.+)'))
    async def youtube_search(event):
        query = event.pattern_match.group(1)
        params = {
            "part": "snippet",
            "q": query,
            "key": API_KEY,
            "maxResults": 1,
            "type": "video"
        }

        response = requests.get(SEARCH_URL, params=params)
        data = response.json()

        if not data["items"]:
            await event.respond("❌ No videos found!")
            return

        video = data["items"][0]
        title = video["snippet"]["title"]
        video_id = video["id"]["videoId"]
        link = f"https://www.youtube.com/watch?v={video_id}"

        await event.respond(f"🎬 **{title}**\n🔗 {link}")