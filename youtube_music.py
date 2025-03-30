import os
import requests
import yt_dlp
from telethon import events

def download_youtube_audio(video_url):
    """Downloads YouTube audio and returns the file path"""
    output_path = "downloads"
    os.makedirs(output_path, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        file_name = f"{output_path}/{info['title']}.mp3"
        return file_name if os.path.exists(file_name) else None

def register(client):
    @client.on(events.NewMessage(pattern='/ytmp3 (.+)'))
    async def youtube_audio(event):
        video_url = event.pattern_match.group(1)
        await event.respond("🔎 Downloading YouTube audio...")

        file_path = download_youtube_audio(video_url)

        if file_path:
            await event.respond("✅ Download complete! Uploading...")
            await event.respond(file=file_path)  # Sending file to user
            os.remove(file_path)  # Delete file after sending
        else:
            await event.respond("❌ Failed to download audio!")