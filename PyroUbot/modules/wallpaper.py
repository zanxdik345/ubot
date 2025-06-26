from PyroUbot import *
import random
import requests
from pyrogram.enums import *
from pyrogram import *
from pyrogram.types import *
from io import BytesIO

__MODULE__ = "ᴡᴀʟʟᴘᴀᴘᴇʀ"
__HELP__ = """
<b>♛ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴡᴀʟʟᴘᴀᴘᴇʀ ♛</b>

<blockquote><b>perintah :
<code>{0}wallpp</code> [Query]
ᴜɴᴛᴜᴋ ᴍᴇɴᴄᴀʀɪ ᴡᴀʟʟᴘᴀᴘᴇʀ/ɢᴀᴍʙᴀʀ

✮ Query ✮
   卍 ᴛᴇᴋɴᴏʟᴏɢɪ
   卍 ᴀᴇsᴛʜᴇᴛɪᴄ
   卍 ᴋᴀᴛᴀᴋᴀᴛᴀ   
   卍 ʜᴇᴋᴇʀ   
   卍 ᴛᴇᴋɴᴏʟᴏɢɪ
   卍 ᴀɴᴊɪɴɢ     
   卍 ʜᴘ 
   卍 ɢᴀᴍᴇʀ 
   卍 ᴘʀᴏɢᴀᴍɪɴɢ  
   卍 ᴄʜᴜᴋʏ 
   卍 ᴋᴜᴄɪɴɢ  
"""

URLS = {
    "teknologi": "https://api.botcahx.eu.org/api/wallpaper/teknologi?apikey=Boyy",
    "aesthetic": "https://api.botcahx.eu.org/api/wallpaper/aesthetic?apikey=Boyy",
    "katakata": "https://api.botcahx.eu.org/api/wallpaper/katakata?apikey=Boyy",
    "heker": "https://api.botcahx.eu.org/api/wallpaper/hacker?apikey=Boyy",
    "anjing": "https://api.botcahx.eu.org/api/wallpaper/anjing?apikey=Boyy",
    "hp": "https://api.botcahx.eu.org/api/wallpaper/wallhp?apikey=Boyy",
    "gamer": "https://api.botcahx.eu.org/api/wallpaper/gaming?apikey=Boyy",
    "progaming": "https://api.botcahx.eu.org/api/wallpaper/programing?apikey=Boyy",
    "chuky": "https://api.botcahx.eu.org/api/wallpaper/boneka-chucky?apikey=Boyy",
    "kucing": "https://api.botcahx.eu.org/api/wallpaper/kucing?apikey=Boyy",
    }


@PY.UBOT("wallpp")
@PY.TOP_CMD
async def _(client, message):
    # Extract query from message
    query = message.text.split()[1] if len(message.text.split()) > 1 else None
    
    if query not in URLS:
        valid_queries = ", ".join(URLS.keys())
        await message.reply(f"<emoji id=5215204871422093648>❌</emoji> Query tidak valid. Gunakan salah satu dari: {valid_queries}.")
        return

    processing_msg = await message.reply("<emoji id=4943239162758169437>🤩</emoji> Processing...")
    
    try:
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        response = requests.get(URLS[query])
        response.raise_for_status()
        
        photo = BytesIO(response.content)
        photo.name = 'image.jpg'
        
        await client.send_photo(message.chat.id, photo)
        await processing_msg.delete()
    except requests.exceptions.RequestException as e:
        await processing_msg.edit_text(f"<emoji id=5215204871422093648>❌</emoji> Gagal mengambil gambar anime Error: {e}")
