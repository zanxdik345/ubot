import os
import platform
import subprocess
import sys
import traceback
from datetime import datetime
from io import BytesIO, StringIO
from PyroUbot.config import OWNER_ID
import psutil

from PyroUbot import *

async def cukimay(client, message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text(f"\nmau ngapain anjenk?\n")
        return
    command = get_arg(message)
    msg = await message.reply("memproses...", quote=True)
    if not command:
        return await msg.edit("noob")
    try:
        if command == "shutdown":
            await msg.delete()
            await handle_shutdown(message)
        elif command == "restart":
            await msg.delete()
            await handle_restart(message)
        elif command == "update":
            await msg.delete()
            await handle_update(message)
        else:
            await process_command(message, command)
            await msg.delete()
    except Exception as error:
        await msg.edit(error)

@PY.UBOT("sh")
async def _(client, message):
    await cukimay(client, message)

@PY.BOT("shell")
async def _(client, message):
    await cukimay(client, message)

@PY.CALLBACK("cb_restart")
async def cb_restart(client, callback_query):
    await callback_query.message.delete()
    os.system(f"kill -9 {os.getpid()} && python3 -m PyroUbot")

@PY.CALLBACK("cb_gitpull")
async def cb_gitpull(client, callback_query):
    await callback_query.message.delete()
    os.system(f"kill -9 {os.getpid()} && git pull && python3 -m PyroUbot")
    
async def handle_shutdown(message):
    await message.reply("✅ System berhasil dimatikan", quote=True)
    os.system(f"kill -9 {os.getpid()}")


async def handle_restart(message):
    await message.reply("✅ System berhasil direstart", quote=True)
    os.execl(sys.executable, sys.executable, "-m", "PyroUbot")


async def handle_update(message):
    out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
    if "Already up to date." in str(out):
        return await message.reply(out, quote=True)
    elif int(len(str(out))) > 4096:
        await send_large_output(message, out)
    else:
        await message.reply(f"```{out}```", quote=True)
    os.execl(sys.executable, sys.executable, "-m", "PyroUbot")


async def process_command(message, command):
    result = (await bash(command))[0]
    if int(len(str(result))) > 4096:
        await send_large_output(message, result)
    else:
        await message.reply(result)


async def send_large_output(message, output):
    with BytesIO(str.encode(str(output))) as out_file:
        out_file.name = "result.txt"
        await message.reply_document(document=out_file)


@PY.UBOT("eval")
async def _(client, message):
    if message.from_user.id != OWNER_ID:
        await message.reply_text(f"mau ngapain anjenk?")
        return
    if not get_arg(message):
        return
    TM = await message.reply_text("sebentar proses...")
    cmd = message.text.split(" ", maxsplit=1)[1]
    reply_to_ = message.reply_to_message or message
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = "OUTPUT:\n"
    final_output += f"{evaluation.strip()}"
    if len(final_output) > 4096:
        with BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file,
                caption=cmd[: 4096 // 4 - 1],
                disable_notification=True,
                quote=True,
            )
    else:
        await reply_to_.reply_text(final_output, quote=True)
    await TM.delete()



@PY.UBOT("trash")
@PY.TOP_CMD
async def _(client, message):
    if message.reply_to_message:
        try:
            if len(message.command) < 2:
                if len(str(message.reply_to_message)) > 4096:
                    with BytesIO(str.encode(str(message.reply_to_message))) as out_file:
                        out_file.name = "trash.txt"
                        return await message.reply_document(document=out_file)
                else:
                    return await message.reply(message.reply_to_message)
            else:
                value = eval(f"message.reply_to_message.{message.command[1]}")
                return await message.reply(value)
        except Exception as error:
            return await message.reply(str(error))
    else:
        return await message.reply("reply peꜱan anjenk!!")
