import requests
from telethon import events

def get_tiktok_download_link(video_url):
    API_URL = "https://snaptik.app/abc.php"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"url": video_url}

    response = requests.post(API_URL, headers=headers, data=data)

    if response.status_code == 200:
        return response.text  # Extract video link from response
    return None

def register(client):
    @client.on(events.NewMessage(pattern='/tiktok (.+)'))
    async def tiktok_download(event):
        video_url = event.pattern_match.group(1)
        await event.respond("🔎 Fetching TikTok video...")

        download_link = get_tiktok_download_link(video_url)

        if download_link:
            await event.respond(f"🎥 **TikTok Video**\n🔽 [Download Here]({download_link})")
        else:
            await event.respond("❌ Failed to fetch the video!")