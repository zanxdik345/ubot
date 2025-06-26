import asyncio
import random

from PyroUbot import *

__MODULE__ = "ᴄᴇᴋᴄᴀɴᴛɪᴋ"
__HELP__ = """<blockquote><b>**「 BANTUAN UNTUK MODULE CEK CANTIK 」**

♛ **ᴘᴇʀɪɴᴛᴀʜ: .cekcantik**
卍 **ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴄᴀɴᴛɪᴋ ɴᴀᴍᴀ ᴏʀᴀɴɢ**</b></blockquote>"""


@PY.UBOT("cekcantik")
@PY.TOP_CMD
async def cekkhodam(client, message):
    try:
        nama = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
        if not nama:
            await message.edit("<blockquote><b>ɴᴀᴍᴀɴʏᴀ ᴍᴀɴᴀ ᴍʙᴀᴋ</b></blockquote>")
            return

        def pick_random(options):
            return random.choice(options)

        hasil = f"""
 <b>✮ ʜᴀsɪʟ ᴄᴇᴋ ᴄᴀɴᴛɪᴋ:</b>
<blockquote><b>╭───────────────────────
├ •ɴᴀᴍᴀ : {nama}
├ •ᴄᴀɴᴛɪᴋ : {pick_random(['ɢᴀ sᴇʙᴇʀᴀᴘᴀ', 'ᴅɪᴋɪᴛ', 'ʙᴀɴʏᴀᴋ', 'sᴇᴛᴇɴɢᴀʜ', 'sᴇᴘᴇʀᴀᴘᴀᴛ', 'sᴇ ᴛᴇᴛᴇ','sᴇ ᴊᴇᴍʙᴜᴛ','ᴛᴇғᴏs'])}
├ •ɴɢᴇʀɪ ʙᴇᴛ ᴊɪʀ
╰────────────────────────</b></blockquote>       
      """
        await message.edit(hasil)
    except BaseException:
        pass
