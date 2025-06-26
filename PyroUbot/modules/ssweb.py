import os
import datetime
import requests
from PyroUbot import *

__MODULE__ = "ss ᴡᴇʙ ᴘᴄ"
__HELP__ = """
<b>✮ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ss ᴡᴇʙ pc ✮</b>

<blockquote><b>perintah :
<code>{0}ssweb</code> link
untuk screenshot website pc</b></blockquote>
"""

def get_ssweb_image(url):
    api_url = "https://api.botcahx.eu.org/api/tools/ssweb"
    params = {
        "url": url,
        "device": "desktop",
        "apikey": "Biyy"
    }
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            return None
    except requests.exceptions.RequestException:
        return None

@PY.UBOT("ssweb")
async def screenshot_handler(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.reply_text("<b><i>MANA URL NYA!</i></b>")
        return

    url = args[1].strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    await message.reply_text("<b><i>PROSES SS PAKAI PC KINGZ ♛</i></b>")

    image_data = get_ssweb_image(url)
    if not image_data:
        await message.reply_text("<b><i>Gagal mengambil screenshot.</i></b>")
        return

    filepath = f"img2p.jpeg"
    with open(filepath, "wb") as file:
        file.write(image_data)

    await client.send_photo(message.chat.id, filepath, caption="**__Nih Kingz Gambarnya Sudah Di Screenshot Pakai Pc.__**")
    os.remove(filepath)
    
