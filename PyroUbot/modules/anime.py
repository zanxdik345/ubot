from PyroUbot import *
import random
import requests
from pyrogram.enums import *
from pyrogram import *
from pyrogram.types import *
from io import BytesIO

__MODULE__ = "ᴀɴɪᴍᴇ"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴀɴɪᴍᴇ 』</b>

<b>⌲ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}anime [query]</code>

<b>Query:</b> <b>keneki</b>,
    <b>megumin/b>,
    <b>yotsuba</b>,
    <b>shinomiya</b>,
    <b>yumeko</b>,
    <b>tsunade</b>,
    <b>kagura</b>,
    <b>madara</b>,
    <b>itachi</b>,
    <b>akira</b>,
    <b>toukachan</b>,
    <b>cicho</b>,
    <b>sasuke</b></blockquote>
"""

URLS = {
    "keneki": "https://api.botcahx.eu.org/api/anime/keneki?apikey=Biyy",
    "megumin": "https://api.botcahx.eu.org/api/anime/megumin?apikey=Biyy",
    "yotsuba": "https://api.botcahx.eu.org/api/anime/yotsuba?apikey=Biyy",
    "shinomiya": "https://api.botcahx.eu.org/api/anime/shinomiya?apikey=Biyy",
    "yumeko": "https://api.botcahx.eu.org/api/anime/yumeko?apikey=Biyy",
    "tsunade": "https://api.botcahx.eu.org/api/anime/tsunade?apikey=Biyy",
    "kagura": "https://api.botcahx.eu.org/api/anime/kagura?apikey=Biyy",
    "madara": "https://api.botcahx.eu.org/api/anime/madara?apikey=Biyy",
    "itachi": "https://api.botcahx.eu.org/api/anime/itachi?apikey=Biyy",
    "akira": "https://api.botcahx.eu.org/api/anime/akira?apikey=Biyy",
    "toukachan": "https://api.botcahx.eu.org/api/anime/toukachan?apikey=Biyy",
    "cicho": "https://api.botcahx.eu.org/api/anime/chiho?apikey=Biyy",
    "sasuke": "https://api.botcahx.eu.org/api/anime/sasuke?apikey=Biyy"
}

@PY.UBOT("anime")
@PY.TOP_CMD
async def _(client, message):
    # Extract query from message
    query = message.text.split()[1] if len(message.text.split()) > 1 else None
    
    if query not in URLS:
        valid_queries = ", ".join(URLS.keys())
        await message.reply(f"Query tidak valid. Gunakan salah satu dari: {valid_queries}.")
        return

    processing_msg = await message.reply("Processing Kingz...")
    
    try:
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        response = requests.get(URLS[query])
        response.raise_for_status()
        
        photo = BytesIO(response.content)
        photo.name = 'image.jpg'
        
        await client.send_photo(message.chat.id, photo)
        await processing_msg.delete()
    except requests.exceptions.RequestException as e:
        await processing_msg.edit_text(f"Gagal mengambil gambar anime Error: {e}")
