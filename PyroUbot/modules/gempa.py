import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "ɢᴇᴍᴘᴀ"
__HELP__ = """
<blockquote><b>『 ɢᴇᴍᴘᴀ 』</b>

  <b>➢ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}gempa</code> 
   <i>penjelasan:</b> cek info sekitar gempa bmkg</i></blockquote>
"""

@PY.UBOT("gempa")
async def stalkig(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Processing...")
    chat_id = message.chat.id
    url = f"https://api.botcahx.eu.org/api/search/gempa?apikey=Biyy"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hasil = data['result']['result']
            lintang = hasil['Lintang']
            bujur = hasil['Bujur']
            magnitude = hasil['Magnitudo']
            kedalaman = hasil['Kedalaman']
            potensi = hasil['Potensi']
            wilayah = hasil['Wilayah']
            tanggal = hasil['tanggal']
            jam = hasil['jam']
            photoUrl = f"https://warning.bmkg.go.id/img/logo-bmkg.png"
            caption = f"""
<blockquote><b>╭─ •  「 <b>Info Gempa Terkini</b> 」
│  ◦ <b>Magnitude: <code>{magnitude}</code></b>
│  ◦ <b>Kedalaman: <code>{kedalaman}</code></b>
│  ◦ <b>Koordinat: <code>{bujur}, {lintang}</code></b>
│  ◦ <b>Waktu: <code>{tanggal}, {jam}</code></b>
│  ◦ <b>Lokasi: <code>{wilayah}</code></b>
│  ◦ <b>Potensi: <code>{potensi}</code></b>
╰──── • 
</blockquote></b>
"""
            photo_path = wget.download(photoUrl)
            await client.send_photo(chat_id, caption=caption, photo=photo_path)
            if os.path.exists(photo_path):
                os.remove(photo_path)
            
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} No 'result' key found in the response.")
    
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} Request failed: {e}")
    
    except Exception as e:
        await jalan.edit(f"{ggl} An error occurred: {e}")
