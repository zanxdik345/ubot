from pyrogram import Client, filters
import requests
import asyncio
from PyroUbot import *

__MODULE__ = "ᴛᴡɪᴛᴛᴇʀ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴡɪᴛᴛᴇʀ ⦫</b>
<blockquote><b>
⎆ Perintah :
ᚗ <code>{0}twit</code> link video twitter
⊶ Mendownload Music Yang Di Inginkan.</b></blockquote>
"""

async def get_twitter_video(url):
    api_url = f"https://api.botcahx.eu.org/api/dowloader/twitter?url={url}&apikey=moire"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("status"):
            video_urls = data["result"]["url"]
            hd_url = video_urls[0].get("hd") if video_urls else None
            sd_url = video_urls[1].get("sd") if len(video_urls) > 1 else None
            return hd_url or sd_url
    return None

@PY.UBOT("twit")
async def twitter_download(client, message):
    if len(message.command) < 2:
        await message.reply_text("Gunakan format: /twitter <link_twitter>")
        return

    twitter_url = message.command[1]
    msg = await message.reply_text("Mengambil video, harap tunggu...")

    video_url = await get_twitter_video(twitter_url)

    if video_url:
        await msg.edit("Mengirim video...")
        await message.reply_video(video_url, caption="Berikut video yang Anda minta.")
    else:
        await msg.edit("Gagal mengambil video. Pastikan link benar atau coba lagi nanti.")
